# Mission Control AI — MobilitySat

Sistema de monitoramento operacional com IA generativa para análise contextual de telemetria espacial simulada, desenvolvido para a Global Solution 2026 da FIAP.

---

## Integrantes

* Rafael Lins — RM: 570588
* Cauã Paes — RM: 569906
* João Pedro Soler — RM: 569725

---

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema de análise operacional baseado em IA capaz de interpretar telemetria espacial simulada e gerar diagnósticos contextualizados sobre o estado da missão.

A proposta foi desenvolvida dentro do contexto da Global Solution 2026 da FIAP, utilizando IA generativa para análise de riscos operacionais em sistemas orbitais voltados para mobilidade inteligente e infraestrutura terrestre.

O sistema simula:

* coleta de telemetria
* análise de alertas operacionais
* interpretação contextual via IA
* impactos terrestres da missão

---

## Sobre a Missão MobilitySat

A MobilitySat é uma missão orbital fictícia criada para monitoramento de sistemas de posicionamento e sincronização utilizados em:

* logística autônoma
* agricultura de precisão
* rastreamento de frotas
* navegação inteligente
* mobilidade conectada

A missão possui foco operacional em integridade GNSS, estabilidade orbital e confiabilidade de sincronização.

---

## Funcionalidades Implementadas

* Geração de telemetria simulada
* Sistema de alertas operacionais
* Cenários pré-definidos de missão
* Integração com IA generativa via OpenRouter
* System prompt contextualizado
* Análise operacional automatizada
* Diagnóstico técnico contextualizado
* Impacto terrestre contextualizado
* Interface CLI em terminal

---

## Tecnologias Utilizadas

* Python 3.13
* OpenRouter API
* Meta Llama 3.1 8B Instruct
* python-dotenv
* PyCharm

---

## Estrutura do Projeto

```text
global-solution-mission-control-ai/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── prompts/
│   └── system_prompt.md
│
└── src/
    ├── ai_client.py
    ├── telemetria.py
    ├── alertas.py
    └── engine.py
```

---

## Funcionamento do Sistema

O sistema segue o seguinte fluxo operacional:

```text
telemetria
→ alertas operacionais
→ montagem de contexto
→ análise da IA
→ diagnóstico da missão
```

A IA recebe:

* telemetria atual
* alertas detectados
* contexto da missão
* impacto terrestre

Com base nisso, ela produz uma análise operacional contextualizada.

---

## Cenários Implementados

| Cenário   | Descrição                                        |
| --------- | ------------------------------------------------ |
| Normal    | Operação estável dentro dos parâmetros esperados |
| Alerta    | Instabilidade moderada detectada                 |
| Crítico   | Múltiplas falhas operacionais simultâneas        |
| Aleatório | Telemetria gerada dinamicamente                  |

---

## Parâmetros de Telemetria

O sistema simula:

* nível de energia
* temperatura operacional
* precisão GNSS
* sincronização orbital

Esses parâmetros são utilizados para gerar alertas e alimentar a análise contextual da IA.

---

## Impacto Terrestre

A missão MobilitySat possui relação direta com sistemas críticos utilizados na Terra.

Falhas operacionais podem impactar:

* rotas logísticas automatizadas
* agricultura de precisão
* sincronização de transporte inteligente
* navegação autônoma
* rastreamento de veículos

---

## Instalação

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd global-solution-mission-control-ai
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração da API

Crie um arquivo `.env` na raiz do projeto:

```env
OPENROUTER_API_KEY=minha_chave_aqui
```

---

## Execução

Execute o sistema com:

```bash
python main.py
```

---

## Exemplo de Fluxo

```text
=== MISSION CONTROL AI ===

Escolha o cenário da missão:

1 - Normal
2 - Alerta
3 - Crítico
4 - Aleatório
```

O sistema gera:

* telemetria
* alertas operacionais
* análise contextual da IA

---

## Exemplo de Análise

```text
CRÍTICO: perda significativa de precisão GNSS.

Impactos potenciais:
- falhas logísticas
- erros de navegação autônoma
- comprometimento agrícola
```

---

## Segurança

* A API Key é armazenada via variável de ambiente
* O arquivo `.env` não é enviado ao GitHub
* O projeto utiliza `.gitignore` para proteger credenciais

---

## Limitações

O sistema possui foco acadêmico e operacional simulado.

Não representa:

* física espacial real
* telemetria orbital científica
* sistemas espaciais reais

O objetivo principal é demonstrar:

* integração com IA
* engenharia de contexto
* análise operacional automatizada

---

## Demonstração

Vídeo demonstrativo:

> LINK_DO_VIDEO

---

## Repositório

GitHub do projeto:

> [LINK_DO_REPOSITORIO](https://github.com/rafaelclins/global-solution-mission-control-ai)
