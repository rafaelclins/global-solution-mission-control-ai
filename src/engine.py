from src.telemetria import (
    gerar_telemetria,
    cenario_normal,
    cenario_alerta,
    cenario_critico
)

from src.alertas import analisar_alertas
from src.ai_client import ask_ai


class MissionEngine:

    def __init__(self):

        # Carrega system prompt
        with open("prompts/system_prompt.md", "r", encoding="utf-8") as file:
            self.system_prompt = file.read()

    def analyze(self, modo="aleatorio"):

        # Seleciona cenário
        if modo == "normal":
            telemetria = cenario_normal()

        elif modo == "alerta":
            telemetria = cenario_alerta()

        elif modo == "critico":
            telemetria = cenario_critico()

        else:
            telemetria = gerar_telemetria()

        # Analisa alertas
        alertas = analisar_alertas(telemetria)

        # Monta contexto operacional
        contexto = f"""
MISSÃO: MobilitySat

TELEMETRIA:
- Energia: {telemetria['energia']}%
- Temperatura: {telemetria['temperatura']}°C
- Precisão GPS: {telemetria['precisao_gps']} metros
- Sincronização: {telemetria['sincronizacao']}

ALERTAS:
{chr(10).join(alertas)}

Analise os riscos operacionais da missão,
os impactos terrestres
e sugira ações recomendadas.
"""

        # Consulta IA
        resposta = ask_ai(
            self.system_prompt,
            contexto
        )

        return telemetria, alertas, resposta