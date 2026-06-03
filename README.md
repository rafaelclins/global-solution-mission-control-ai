Mission Control AI — MobilitySat

Sistema de monitoramento operacional com IA generativa para análise contextual de telemetria espacial simulada, desenvolvido para a Global Solution 2026 da FIAP.

⸻

Integrantes

* Rafael Lins — RM: 570588
* Cauã Paes — RM: 569906
* João Pedro Soler — RM: 569725

⸻

Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema de análise operacional baseado em Inteligência Artificial capaz de interpretar telemetria espacial simulada e gerar diagnósticos contextualizados sobre o estado da missão.

A proposta foi desenvolvida dentro do contexto da Global Solution 2026 da FIAP, utilizando IA generativa para análise de riscos operacionais em sistemas orbitais voltados para mobilidade inteligente e infraestrutura terrestre.

O sistema simula:

* coleta de telemetria
* análise de alertas operacionais
* interpretação contextual via IA
* avaliação de impactos terrestres da missão

⸻

Sobre a Missão MobilitySat

A MobilitySat é uma missão orbital fictícia criada para monitoramento de sistemas de posicionamento e sincronização utilizados em:

* logística autônoma
* agricultura de precisão
* rastreamento de frotas
* navegação inteligente
* mobilidade conectada

A missão possui foco operacional em integridade GNSS, estabilidade orbital e confiabilidade de sincronização.

⸻

Funcionalidades Implementadas

* Geração de telemetria simulada
* Sistema de alertas operacionais
* Cenários pré-definidos de missão
* Integração com IA generativa via OpenRouter
* System Prompt contextualizado
* Análise operacional automatizada
* Diagnóstico técnico contextualizado
* Avaliação de impactos terrestres
* Interface CLI em terminal

⸻

Tecnologias Utilizadas

* Python 3.13
* OpenRouter API
* Meta Llama 3.1 8B Instruct
* python-dotenv
* PyCharm

⸻

Estrutura do Projeto

global-solution-mission-control-ai/
│
├── main.py
├── banner_ascii.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── assets/
│   ├── screenshot_banner.png
│   └── screenshot_analise.png
│
├── prompts/
│   └── system_prompt.md
│
└── src/
    ├── __init__.py
    ├── ai_client.py
    ├── telemetria.py
    ├── alertas.py
    ├── engine.py
    └── ui.py

⸻

Funcionamento do Sistema

O sistema segue o seguinte fluxo operacional:

telemetria
→ alertas operacionais
→ montagem de contexto
→ análise da IA
→ diagnóstico da missão

A IA recebe:

* telemetria atual
* alertas detectados
* contexto da missão
* impactos terrestres relacionados

Com base nessas informações, ela produz uma análise operacional contextualizada.

⸻

Cenários Implementados

Cenário	Descrição
Normal	Operação estável dentro dos parâmetros esperados
Alerta	Instabilidade moderada detectada
Crítico	Múltiplas falhas operacionais simultâneas
Aleatório	Telemetria gerada dinamicamente

⸻

Parâmetros de Telemetria

O sistema simula:

* nível de energia
* temperatura operacional
* precisão GNSS
* sincronização orbital

Esses parâmetros são utilizados para gerar alertas e alimentar a análise contextual da IA.

⸻

Impacto Terrestre

A missão MobilitySat possui relação direta com sistemas críticos utilizados na Terra.

Falhas operacionais podem impactar:

* rotas logísticas automatizadas
* agricultura de precisão
* sincronização de transporte inteligente
* navegação autônoma
* rastreamento de veículos

⸻

Instalação

Clone o repositório:

git clone https://github.com/rafaelclins/global-solution-mission-control-ai

Acesse a pasta do projeto:

cd global-solution-mission-control-ai

Instale as dependências:

pip install -r requirements.txt

⸻

Configuração da API

Crie um arquivo .env na raiz do projeto:

OPENROUTER_API_KEY=sua_chave_aqui

⸻

Execução

Execute o sistema com:

python main.py

⸻

Exemplo de Fluxo

=== MISSION CONTROL AI ===
Escolha o cenário da missão:
1 - Normal
2 - Alerta
3 - Crítico
4 - Aleatório

O sistema gera:

* telemetria
* alertas operacionais
* análise contextual da IA

⸻

Exemplo de Análise

CRÍTICO: perda significativa de precisão GNSS.
Impactos potenciais:
- falhas logísticas
- erros de navegação autônoma
- comprometimento agrícola

⸻

Adaptações da Implementação

O projeto de referência apresentava uma interface CLI baseada em comandos. Durante o desenvolvimento, optamos por utilizar um fluxo baseado em cenários pré-definidos (Normal, Alerta, Crítico e Aleatório).

Essa decisão foi tomada para facilitar a demonstração dos diferentes estados operacionais da missão MobilitySat, permitindo validar de forma objetiva os alertas gerados e as análises produzidas pela IA.

A arquitetura principal proposta foi mantida, incluindo:

* classe MissionEngine
* geração de telemetria simulada
* sistema de alertas
* integração com IA generativa
* System Prompt contextualizado
* análise operacional automatizada

⸻

Segurança

* A API Key é armazenada via variável de ambiente
* O arquivo .env não é enviado ao GitHub
* O projeto utiliza .gitignore para proteção de credenciais

⸻

Limitações

O sistema possui foco acadêmico e operacional simulado.

Não representa:

* física espacial real
* telemetria orbital científica
* sistemas espaciais reais

O objetivo principal é demonstrar:

* integração com IA generativa
* engenharia de contexto
* análise operacional automatizada
* interpretação de telemetria simulada

⸻

Demonstração

Vídeo demonstrativo do funcionamento do sistema:

https://youtube.com/shorts/-ermS08dZgY?si=XE66iO8xhddlBbKk

O vídeo apresenta:

* inicialização do sistema
* seleção de cenários operacionais
* geração de telemetria simulada
* detecção de alertas
* análise contextual realizada pela IA

⸻

Repositório

GitHub do projeto:

https://github.com/rafaelclins/global-solution-mission-control-ai