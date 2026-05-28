from src.engine import executar_missao


# Carrega o system prompt
with open("prompts/system_prompt.md", "r", encoding="utf-8") as file:
    system_prompt = file.read()


# Banner principal
print("=" * 50)
print("         MISSION CONTROL AI")
print("         MobilitySat Division")
print("=" * 50)


# Escolha do cenário
print("\nEscolha o cenário da missão:\n")

print("1 - Normal")
print("2 - Alerta")
print("3 - Crítico")
print("4 - Aleatório")


opcao = input("\nDigite a opção: ")


# Define modo
if opcao == "1":
    modo = "normal"

elif opcao == "2":
    modo = "alerta"

elif opcao == "3":
    modo = "critico"

else:
    modo = "aleatorio"


# Executa missão
telemetria, alertas, resposta = executar_missao(system_prompt, modo)


# Exibe telemetria
print("\n" + "=" * 50)
print("               TELEMETRIA")
print("=" * 50)

for chave, valor in telemetria.items():
    print(f"{chave}: {valor}")


# Exibe alertas
print("\n" + "=" * 50)
print("         ALERTAS OPERACIONAIS")
print("=" * 50)

for alerta in alertas:
    print(f"- {alerta}")


# Exibe análise da IA
print("\n" + "=" * 50)
print("           ANÁLISE DA IA")
print("=" * 50)

print(f"\n{resposta}")


# Encerramento
input("\nPressione ENTER para encerrar...")