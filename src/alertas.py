def analisar_alertas(telemetria):

    alertas = []


    # Energia
    if telemetria["energia"] < 50:
        alertas.append("ALERTA: nível de energia abaixo do ideal.")


    # Temperatura
    if telemetria["temperatura"] > 70:
        alertas.append("CRÍTICO: superaquecimento detectado.")


    # Precisão GPS
    if telemetria["precisao_gps"] > 5:
        alertas.append("CRÍTICO: perda significativa de precisão GNSS.")


    # Sincronização
    if telemetria["sincronizacao"] == "instável":
        alertas.append("ALERTA: instabilidade na sincronização orbital.")


    # Nenhum alerta
    if not alertas:
        alertas.append("Sistema operando dentro da normalidade.")


    return alertas