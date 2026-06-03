# Mission Control AI — MobilitySat

Sistema de monitoramento operacional com IA generativa para análise contextual de telemetria espacial simulada, desenvolvido para a Global Solution 2026 da FIAP.

---

## Integrantes

- Rafael Lins — RM: 570588
- Cauã Paes — RM: 569906
- João Pedro Soler — RM: 569725

---

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um sistema de análise operacional baseado em Inteligência Artificial capaz de interpretar telemetria espacial simulada e gerar diagnósticos contextualizados sobre o estado da missão.

A proposta foi desenvolvida dentro do contexto da Global Solution 2026 da FIAP, utilizando IA generativa para análise de riscos operacionais em sistemas orbitais voltados para mobilidade inteligente e infraestrutura terrestre.

O sistema simula:

- Coleta de telemetria
- Análise de alertas operacionais
- Interpretação contextual via IA
- Avaliação de impactos terrestres da missão

---

## Sobre a Missão MobilitySat

A MobilitySat é uma missão orbital fictícia criada para monitoramento de sistemas de posicionamento e sincronização utilizados em:

- Logística autônoma
- Agricultura de precisão
- Rastreamento de frotas
- Navegação inteligente
- Mobilidade conectada

A missão possui foco operacional em integridade GNSS, estabilidade orbital e confiabilidade de sincronização.

---

## Funcionalidades Implementadas

- Geração de telemetria simulada
- Sistema de alertas operacionais
- Cenários pré-definidos de missão
- Integração com IA generativa via OpenRouter
- System Prompt contextualizado
- Análise operacional automatizada
- Diagnóstico técnico contextualizado
- Avaliação de impactos terrestres
- Interface CLI em terminal

---

## Tecnologias Utilizadas

- Python 3.13
- OpenRouter API
- Meta Llama 3.1 8B Instruct
- python-dotenv
- PyCharm

---

## Estrutura do Projeto

```text
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

- Telemetria atual
- Alertas detectados
- Contexto da missão
- Impactos terrestres relacionados

Com base nessas informações, ela produz uma análise operacional contextualizada.

---

## Cenários Implementados

| Cenário | Descrição |
|----------|----------|
| Normal | Operação estável dentro dos parâmetros esperados |
| Alerta | Instabilidade moderada detectada |
| Crítico | Múltiplas falhas operacionais simultâneas |
| Aleatório | Telemetria gerada dinamicamente |

---

## Parâmetros de Telemetria

O sistema simula:

- Nível de energia
- Temperatura operacional
- Precisão GNSS
- Sincronização orbital

Esses parâmetros são utilizados para gerar alertas e alimentar a análise contextual da IA.

---

## Impacto Terrestre

A missão MobilitySat possui relação direta com sistemas críticos utilizados na Terra.

Falhas operacionais podem impactar:

- Rotas logísticas automatizadas
- Agricultura de precisão
- Sincronização de transporte inteligente
- Navegação autônoma
- Rastreamento de veículos

---

## Capturas do Sistema

### Tela Inicial

![Tela Inicial](assets/screenshot_banner.png)

### Análise Operacional

![Análise Operacional](assets/screenshot_analise.png)

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/rafaelclins/global-solution-mission-control-ai
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
OPENROUTER_API_KEY=sua_chave_aqui
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

- Telemetria
- Alertas operacionais
- Análise contextual da IA

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

## Adaptações da Implementação

O projeto de referência apresentava uma interface CLI baseada em comandos. Durante o desenvolvimento, optamos por utilizar um fluxo baseado em cenários pré-definidos (Normal, Alerta, Crítico e Aleatório).

Essa decisão foi tomada para facilitar a demonstração dos diferentes estados operacionais da missão MobilitySat, permitindo validar de forma objetiva os alertas gerados e as análises produzidas pela IA.

A arquitetura principal proposta foi mantida, incluindo:

- Classe MissionEngine
- Geração de telemetria simulada
- Sistema de alertas
- Integração com IA generativa
- System Prompt contextualizado
- Análise operacional automatizada

---

## Segurança

- A API Key é armazenada via variável de ambiente
- O arquivo `.env` não é enviado ao GitHub
- O projeto utiliza `.gitignore` para proteção de credenciais

---

## Limitações

O sistema possui foco acadêmico e operacional simulado.

Não representa:

- Física espacial real
- Telemetria orbital científica
- Sistemas espaciais reais

O objetivo principal é demonstrar:

- Integração com IA generativa
- Engenharia de contexto
- Análise operacional automatizada
- Interpretação de telemetria simulada

---

## Demonstração

Vídeo demonstrativo do funcionamento do sistema:

https://youtube.com/shorts/-ermS08dZgY?si=XE66iO8xhddlBbKk

O vídeo apresenta:

- Inicialização do sistema
- Seleção de cenários operacionais
- Geração de telemetria simulada
- Detecção de alertas
- Análise contextual realizada pela IA

---

## Repositório

GitHub do projeto:

https://github.com/rafaelclins/global-solution-mission-control-ai