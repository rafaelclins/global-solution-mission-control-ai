from banner_ascii import show_banner

from src.ui import show_menu
from src.engine import MissionEngine


# Banner inicial
show_banner()


# Interface inicial
show_menu()


# Inicializa engine da missão
engine = MissionEngine()


# Escolha do cenário
print("\nEscolha o cenário da missão:\n")

print("1 - Normal")
print("2 - Alerta")
print("3 - Crítico")
print("4 - Aleatório")


opcao = input("\nDigite a opção: ")


# Define cenário
if opcao == "1":
    modo = "normal"

elif opcao == "2":
    modo = "alerta"

elif opcao == "3":
    modo = "critico"

else:
    modo = "aleatorio"


# Executa missão
telemetria, alertas, resposta = engine.analyze(modo)


# TELEMETRIA
print("\n" + "=" * 50)
print("               TELEMETRIA")
print("=" * 50)

for chave, valor in telemetria.items():
    print(f"{chave}: {valor}")


# ALERTAS
print("\n" + "=" * 50)
print("         ALERTAS OPERACIONAIS")
print("=" * 50)

for alerta in alertas:
    print(f"- {alerta}")


# ANÁLISE DA IA
print("\n" + "=" * 50)
print("           ANÁLISE DA IA")
print("=" * 50)

print(f"\n{resposta}")


# Encerramento
input("\nPressione ENTER para encerrar...")