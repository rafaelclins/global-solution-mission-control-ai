import random


# Cenário aleatório
def gerar_telemetria():

    telemetria = {
        "energia": random.randint(40, 100),
        "temperatura": random.randint(30, 85),
        "precisao_gps": round(random.uniform(0.5, 8.0), 2),
        "sincronizacao": random.choice([
            "estável",
            "instável"
        ])
    }

    return telemetria


# Cenário normal
def cenario_normal():

    return {
        "energia": 88,
        "temperatura": 42,
        "precisao_gps": 1.3,
        "sincronizacao": "estável"
    }


# Cenário de alerta
def cenario_alerta():

    return {
        "energia": 54,
        "temperatura": 68,
        "precisao_gps": 4.8,
        "sincronizacao": "instável"
    }


# Cenário crítico
def cenario_critico():

    return {
        "energia": 29,
        "temperatura": 82,
        "precisao_gps": 7.1,
        "sincronizacao": "instável"
    }