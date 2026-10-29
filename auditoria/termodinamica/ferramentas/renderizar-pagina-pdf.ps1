param([Parameter(Mandatory=$true)][string]$PdfPath,[Parameter(Mandatory=$true)][int]$PageNumber,[Parameter(Mandatory=$true)][string]$PngPath,[uint32]$ImageWidth=1800)
Add-Type -AssemblyName System.Runtime.WindowsRuntime -ErrorAction Stop
$null=[Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
$null=[Windows.Data.Pdf.PdfDocument,Windows.Data.Pdf,ContentType=WindowsRuntime]
$null=[Windows.Data.Pdf.PdfPageRenderOptions,Windows.Data.Pdf,ContentType=WindowsRuntime]
$null=[Windows.Storage.Streams.InMemoryRandomAccessStream,Windows.Storage.Streams,ContentType=WindowsRuntime]
$taskOperationMethod=[System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {$_.Name -eq 'AsTask' -and $_.IsGenericMethodDefinition -and $_.GetGenericArguments().Count -eq 1 -and $_.GetParameters().Count -eq 1} | Select-Object -First 1
function Wait-TaskOperation($Operation,[Type]$ResultType){
  $taskOperation=$taskOperationMethod.MakeGenericMethod($ResultType).Invoke($null,@($Operation))
  if(-not $taskOperation.Wait(30000)){throw 'Timeout na operação PDF'}
  return $taskOperation.Result
}
$sourceFile=Wait-TaskOperation ([Windows.Storage.StorageFile]::GetFileFromPathAsync($PdfPath)) ([Windows.Storage.StorageFile])
$pdfDocument=Wait-TaskOperation ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($sourceFile)) ([Windows.Data.Pdf.PdfDocument])
if($PageNumber -lt 1 -or $PageNumber -gt $pdfDocument.PageCount){throw 'Página fora do documento'}
$pdfPage=$pdfDocument.GetPage([uint32]($PageNumber-1))
$renderStream=New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
$renderOptions=New-Object Windows.Data.Pdf.PdfPageRenderOptions
$renderOptions.DestinationWidth=$ImageWidth
$renderAction=$pdfPage.RenderToStreamAsync($renderStream,$renderOptions)
$taskActionMethod=[System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {$_.Name -eq 'AsTask' -and -not $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.FullName -eq 'Windows.Foundation.IAsyncAction'} | Select-Object -First 1
$renderTask=$taskActionMethod.Invoke($null,@($renderAction))
if(-not $renderTask.Wait(30000)){throw 'Timeout na renderização PDF'}
$renderStream.Seek(0)
$readStream=[System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($renderStream)
$outputStream=[System.IO.File]::Open($PngPath,[System.IO.FileMode]::Create)
$readStream.CopyTo($outputStream)
$outputStream.Dispose()
$readStream.Dispose()
$pdfPage.Dispose()
[pscustomobject]@{Pdf=$PdfPath;Paginas=$pdfDocument.PageCount;Pagina=$PageNumber;Imagem=$PngPath;Largura=$ImageWidth} | ConvertTo-Json
