from src.telemetria import (
    gerar_telemetria,
    cenario_normal,
    cenario_alerta,
    cenario_critico
)

from src.alertas import analisar_alertas
from src.ai_client import ask_ai


def executar_missao(system_prompt, modo="aleatorio"):

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
    TELEMETRIA DA MISSÃO:

    Energia: {telemetria['energia']}%
    Temperatura: {telemetria['temperatura']}°C
    Precisão GPS: {telemetria['precisao_gps']} metros
    Sincronização: {telemetria['sincronizacao']}

    ALERTAS OPERACIONAIS:
    {chr(10).join(alertas)}

    Gere uma análise operacional da situação atual da missão.
    """


    # Envia para IA
    resposta = ask_ai(system_prompt, contexto)


    return telemetria, alertas, resposta