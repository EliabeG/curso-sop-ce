/** Reproduz os fixtures técnicos do suporte BAN-02; não é auditoria pedagógica.
 * Gerado a partir dos trechos executados em Node REPL em 2026-10-27.
 * Esta cópia em arquivo não havia sido executada no momento do registro r1.
 * Execução: node auditoria/termodinamica/evidencias/BAN-02/testar-validador-r1.mjs
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {validateInventory, validateSchema} from '../../inventario/validar-inventario.mjs';
const tmpBase=await fs.mkdtemp(path.join(os.tmpdir(),'ban02-validator-repro-'));
for(const dir of ['modulos','assets','snapshots','pareceres'])await fs.mkdir(path.join(tmpBase,dir),{recursive:true});
const fixtureArticles=[
  "<article id=\"q-e1-100\" class=\"questao\"><a href=\"#base\">Base</a><img src=\"../assets/a.svg\"/><ol class=\"q-alternativas\"><li>A</li><li>B</li><li>C</li></ol></article>",
  "<article id=\"aberto-e1-1\" data-inventario=\"e1\" data-banco=\"aberto\" data-formato=\"resposta_aberta\"><p>Argumente.</p></article>",
  "<article id=\"projeto-e1-1\" data-inventario=\"e1\" data-banco=\"projeto\" data-formato=\"projeto\"><p>Modele.</p></article>"
];
const fixtureHtml="<!DOCTYPE html><html><body><p id=\"base\">Base</p><article id=\"q-e1-100\" class=\"questao\"><a href=\"#base\">Base</a><img src=\"../assets/a.svg\"/><ol class=\"q-alternativas\"><li>A</li><li>B</li><li>C</li></ol></article>\n<article id=\"aberto-e1-1\" data-inventario=\"e1\" data-banco=\"aberto\" data-formato=\"resposta_aberta\"><p>Argumente.</p></article>\n<article id=\"projeto-e1-1\" data-inventario=\"e1\" data-banco=\"projeto\" data-formato=\"projeto\"><p>Modele.</p></article></body></html>";
const resourceData="<svg xmlns=\"http://www.w3.org/2000/svg\"><text>A</text></svg>";
const fixture={
  "schema_version": "1.1",
  "curso": "E1",
  "atualizado_em": "2026-10-27",
  "fonte": {
    "arquivo": "modulos/e1.html",
    "sha256": "bd715d89b5f19f933f725868f28dd36d7cb1d2f573790e00002e7b76178a0c83",
    "snapshot": "snapshots/e1.html"
  },
  "metodo": {
    "descricao": "Fixture",
    "limites": "Teste estrutural"
  },
  "itens": [
    {
      "id": "q-e1-100",
      "banco": "inicial",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "q-e1-100",
        "sha256_artigo": "34172b2a0d51f0176d87dd04e9af34a2b59fbb5f72a7ccba109a16c575a22fe4",
        "recursos": [
          {
            "arquivo": "assets/a.svg",
            "sha256": "9b1bf451cb83b1cf8aa7501c4d8378b191d1ecceaaec7be625d8ed4e5ecb7993"
          }
        ]
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "multipla_escolha",
        "comando": "Teste",
        "numero_alternativas": 3
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "aberto-e1-1",
      "banco": "aberto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "aberto-e1-1",
        "sha256_artigo": "ce8d68d7f1c438a5fb5446f03f059a97f61b4dd33e84816017ee08d702f285c1",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "resposta_aberta",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "projeto-e1-1",
      "banco": "projeto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "projeto-e1-1",
        "sha256_artigo": "44c5cb20db3c8ebdf0035f622ea4524f7106e910812f402b98dc3d23b5dc228c",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "projeto",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    }
  ]
};
const verifiedFixture={
  "schema_version": "1.1",
  "curso": "E1",
  "atualizado_em": "2026-10-27",
  "fonte": {
    "arquivo": "modulos/e1.html",
    "sha256": "bd715d89b5f19f933f725868f28dd36d7cb1d2f573790e00002e7b76178a0c83",
    "snapshot": "snapshots/e1.html"
  },
  "metodo": {
    "descricao": "Fixture",
    "limites": "Teste estrutural"
  },
  "itens": [
    {
      "id": "q-e1-100",
      "banco": "inicial",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "q-e1-100",
        "sha256_artigo": "34172b2a0d51f0176d87dd04e9af34a2b59fbb5f72a7ccba109a16c575a22fe4",
        "recursos": [
          {
            "arquivo": "assets/a.svg",
            "sha256": "9b1bf451cb83b1cf8aa7501c4d8378b191d1ecceaaec7be625d8ed4e5ecb7993"
          }
        ]
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "realizada",
        "evidencia_conferencia": "pareceres/fixture.md#verificações"
      },
      "formato": {
        "tipo": "multipla_escolha",
        "comando": "Teste",
        "numero_alternativas": 3
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "verificado",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": [],
        "evidencia_gabarito": "pareceres/fixture.md#verificações"
      }
    },
    {
      "id": "aberto-e1-1",
      "banco": "aberto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "aberto-e1-1",
        "sha256_artigo": "ce8d68d7f1c438a5fb5446f03f059a97f61b4dd33e84816017ee08d702f285c1",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "resposta_aberta",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "projeto-e1-1",
      "banco": "projeto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "projeto-e1-1",
        "sha256_artigo": "44c5cb20db3c8ebdf0035f622ea4524f7106e910812f402b98dc3d23b5dc228c",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "projeto",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    }
  ]
};
const adjustFixture={
  "schema_version": "1.1",
  "curso": "E1",
  "atualizado_em": "2026-10-27",
  "fonte": {
    "arquivo": "modulos/e1.html",
    "sha256": "bd715d89b5f19f933f725868f28dd36d7cb1d2f573790e00002e7b76178a0c83",
    "snapshot": "snapshots/e1.html"
  },
  "metodo": {
    "descricao": "Fixture",
    "limites": "Teste estrutural"
  },
  "itens": [
    {
      "id": "q-e1-100",
      "banco": "inicial",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "q-e1-100",
        "sha256_artigo": "34172b2a0d51f0176d87dd04e9af34a2b59fbb5f72a7ccba109a16c575a22fe4",
        "recursos": [
          {
            "arquivo": "assets/a.svg",
            "sha256": "9b1bf451cb83b1cf8aa7501c4d8378b191d1ecceaaec7be625d8ed4e5ecb7993"
          }
        ]
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "realizada",
        "evidencia_conferencia": "pareceres/fixture.md#verificações"
      },
      "formato": {
        "tipo": "multipla_escolha",
        "comando": "Teste",
        "numero_alternativas": 3
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "ajustes_obrigatorios",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": [],
        "evidencia_gabarito": "pareceres/fixture.md#verificações"
      }
    },
    {
      "id": "aberto-e1-1",
      "banco": "aberto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "aberto-e1-1",
        "sha256_artigo": "ce8d68d7f1c438a5fb5446f03f059a97f61b4dd33e84816017ee08d702f285c1",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "resposta_aberta",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "projeto-e1-1",
      "banco": "projeto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "projeto-e1-1",
        "sha256_artigo": "44c5cb20db3c8ebdf0035f622ea4524f7106e910812f402b98dc3d23b5dc228c",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_aplicavel"
      },
      "formato": {
        "tipo": "projeto",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    }
  ]
};
const mutationCases=[["ID duplicado",d=>d.itens.push(structuredClone(d.itens[0]))],
["artigo sem registro",d=>d.itens.pop()],
["registro extra inexistente",d=>{var x=structuredClone(d.itens[0]);x.id='q-e1-999';x.localizacao.fragmento=x.id;d.itens.push(x)}],
["hash artigo alterado",d=>d.itens[0].localizacao.sha256_artigo='0'.repeat(64)],
["hash fonte alterado",d=>d.fonte.sha256='0'.repeat(64)],
["recurso omitido",d=>d.itens[0].localizacao.recursos=[]],
["recurso hash alterado",d=>d.itens[0].localizacao.recursos[0].sha256='0'.repeat(64)],
["etapas divergentes",d=>d.itens[0].raciocinio.numero_etapas=2],
["nível sem justificativa",d=>d.itens[0].nivel.justificativa='  '],
["nível pendente",d=>d.itens[0].nivel.estimado='a_classificar'],
["campo desconhecido",d=>d.itens[0].errado=true],
["alternativas divergentes",d=>d.itens[0].formato.numero_alternativas=5],
["competência inválida",d=>d.itens[0].competencias=['C11']],
["banco divergente",d=>d.itens[0].banco='real'],
["relação inexistente",d=>{d.itens[0].exposicao_previa.estado='relacao_identificada';d.itens[0].exposicao_previa.relacoes=[{id_ou_ancora:'ausente',tipo:'relacao_tematica',evidencia:'Fixture'}]}],
["snapshot igual fonte",d=>d.fonte.snapshot=d.fonte.arquivo],
["caminho fora raiz",d=>d.itens[0].localizacao.recursos[0].arquivo='../segredo'],
["tipo formato inválido",d=>d.itens[1].formato.tipo='multipla_escolha'],
["fonte local inexistente",d=>d.itens[0].origem.fontes=[{rotulo:'Fixture',url:'modulos/ausente.html'}]],
["data impossível",d=>d.atualizado_em='2026-02-30']];
const newCases=[["realizada sem evidência",d=>delete d.itens[0].origem.evidencia_conferencia],
["verificado sem evidência",d=>delete d.itens[0].revisao.evidencia_gabarito],
["ajustes sem evidência",d=>{d.itens[0].revisao.gabarito='ajustes_obrigatorios';delete d.itens[0].revisao.evidencia_gabarito}],
["evidência vazia",d=>d.itens[0].origem.evidencia_conferencia='  '],
["evidência arquivo ausente",d=>d.itens[0].origem.evidencia_conferencia='pareceres/ausente.md'],
["evidência âncora ausente",d=>d.itens[0].revisao.evidencia_gabarito='pareceres/fixture.md#ausente'],
["evidência remota",d=>d.itens[0].origem.evidencia_conferencia='https://example.com/parecer'],
["evidência somente fragmento",d=>d.itens[0].origem.evidencia_conferencia='#base'],
["estado não enumerado",d=>d.itens[0].origem.conferencia_oficial='aprovado'],
["versão antiga",d=>d.schema_version='1.0'],
["evidência opcional inválida",d=>{d.itens[0].origem.conferencia_oficial='nao_aplicavel';d.itens[0].origem.evidencia_conferencia='pareceres/ausente.md'}]];
const resultados=[];
async function restore(){
 await fs.writeFile(path.join(tmpBase,'modulos/e1.html'),fixtureHtml);
 await fs.writeFile(path.join(tmpBase,'snapshots/e1.html'),fixtureHtml);
 await fs.writeFile(path.join(tmpBase,'assets/a.svg'),resourceData);
 await fs.writeFile(path.join(tmpBase,'pareceres/fixture.md'),'# Verificações\n\nFixture de teste, não é parecer.\n');
}
async function run(caso,inventory,esperado){
 const resultado=await validateInventory({rootDir:tmpBase,inventory});
 resultados.push({caso,esperado_ok:esperado,observado_ok:resultado.ok,passou:resultado.ok===esperado,erros:resultado.erros});
}
await restore();
await run('estado atual, ID longo, 3 opções, aberto e projeto',fixture,true);
await run('estados realizados/verificados com evidência Markdown existente',verifiedFixture,true);
await run('ajustes obrigatórios com evidência existente',adjustFixture,true);
for(const [nome,mudar]of mutationCases){const data=structuredClone(fixture);mudar(data);await run(nome,data,false);}
for(const [nome,mudar]of newCases){const data=structuredClone(verifiedFixture);mudar(data);await run(nome,data,false);}
await fs.writeFile(path.join(tmpBase,'assets/a.svg'),resourceData+'<!-- mudança de informação -->');
await run('recurso em disco mudou sem tocar HTML',fixture,false);
await restore();
await fs.writeFile(path.join(tmpBase,'modulos/e1.html'),fixtureHtml.replace('</body>','<article class="questao" id="q-e1-101"><p>Novo item</p></article></body>'));
await run('item novo adicionado ao HTML',fixture,false);
await restore();
await fs.writeFile(path.join(tmpBase,'snapshots/e1.html'),fixtureHtml+'x');
await run('snapshot modificado',fixture,false);
await restore();
const brokenHtml=fixtureHtml.replace('href="#base"','href="#ausente"');
await fs.writeFile(path.join(tmpBase,'modulos/e1.html'),brokenHtml);
await fs.writeFile(path.join(tmpBase,'snapshots/e1.html'),brokenHtml);
const brokenData={
  "schema_version": "1.0",
  "curso": "E1",
  "atualizado_em": "2026-10-27",
  "fonte": {
    "arquivo": "modulos/e1.html",
    "sha256": "9620eaec5928cfdb08e952d8e4013195adde3fe099ad55b23e1c829ffd605f22",
    "snapshot": "snapshots/e1.html"
  },
  "metodo": {
    "descricao": "Fixture",
    "limites": "Teste estrutural"
  },
  "itens": [
    {
      "id": "q-e1-100",
      "banco": "inicial",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "q-e1-100",
        "sha256_artigo": "9f313d2ca539eb93df0c1fba84a9c6ddfd5a3508d0de8fe77b2e5b13ec2d8f0d",
        "recursos": [
          {
            "arquivo": "assets/a.svg",
            "sha256": "9b1bf451cb83b1cf8aa7501c4d8378b191d1ecceaaec7be625d8ed4e5ecb7993"
          }
        ]
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_realizada"
      },
      "formato": {
        "tipo": "multipla_escolha",
        "comando": "Teste",
        "numero_alternativas": 3
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "aberto-e1-1",
      "banco": "aberto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "aberto-e1-1",
        "sha256_artigo": "ce8d68d7f1c438a5fb5446f03f059a97f61b4dd33e84816017ee08d702f285c1",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_realizada"
      },
      "formato": {
        "tipo": "resposta_aberta",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    },
    {
      "id": "projeto-e1-1",
      "banco": "projeto",
      "titulo": "Fixture técnica, sem classificação real",
      "localizacao": {
        "arquivo": "modulos/e1.html",
        "fragmento": "projeto-e1-1",
        "sha256_artigo": "44c5cb20db3c8ebdf0035f622ea4524f7106e910812f402b98dc3d23b5dc228c",
        "recursos": []
      },
      "origem": {
        "tipo": "fixture",
        "atribuicao": "Teste técnico",
        "identificadores": [],
        "fontes": [],
        "conferencia_oficial": "nao_realizada"
      },
      "formato": {
        "tipo": "projeto",
        "comando": "Teste",
        "numero_alternativas": 0
      },
      "competencias": [
        "C01"
      ],
      "vinculo_competencias": {
        "tipo": "apoio_fundamental",
        "alcance": "Fixture sem valor pedagógico"
      },
      "pre_requisitos": [
        "Fixture"
      ],
      "nivel": {
        "estimado": "iniciante",
        "justificativa": "Fixture técnica; não representa item do curso",
        "validacao_empirica": "nao_realizada"
      },
      "raciocinio": {
        "categoria": "reconhecimento",
        "etapas": [
          "Fixture"
        ],
        "numero_etapas": 1
      },
      "hipoteses": {
        "explicitadas": [],
        "implicitas": [],
        "limites": []
      },
      "exposicao_previa": {
        "estado": "desconhecida",
        "relacoes": [],
        "limite_da_verificacao": "Fixture"
      },
      "revisao": {
        "leitura": "enunciado_alternativas_comentarios_e_notas",
        "gabarito": "nao_auditado_em_BAN02",
        "ambiguidades_conhecidas": [],
        "encaminhamentos": []
      }
    }
  ]
};
brokenData.schema_version='1.1';
await run('href local quebrado mesmo com hashes atualizados',brokenData,false);
await restore();
const schema=JSON.parse(await fs.readFile(new URL('../../inventario/inventario.schema.json',import.meta.url),'utf8'));
const remoteEvidence=structuredClone(verifiedFixture);
remoteEvidence.itens[0].origem.evidencia_conferencia='https://example.com/parecer';
const schemaErrors=validateSchema(remoteEvidence,schema);
resultados.push({caso:'schema isolado rejeita evidência remota',esperado_ok:false,observado_ok:schemaErrors.length===0,passou:schemaErrors.length>0,erros:schemaErrors});
const passou=resultados.every(x=>x.passou);
console.log(JSON.stringify({natureza:'teste técnico, sem decisão de aceite',schema_version:fixture.schema_version,passou,total:resultados.length,fixtures_temporarios:tmpBase,resultados},null,2));
process.exitCode=passou?0:1;
