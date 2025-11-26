import random

opcoes = ["pedra", "papel", "tesoura"]
pontuacao_usuario = 0
pontuacao_computador = 0

print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
print("Você terá 3 rodadas contra o computador.\n")

for rodada in range(1, 4):
    escolha_usuario = input(f"Rodada {rodada} - escolha (pedra/papel/tesoura): ").lower()
    escolha_computador = random.choice(opcoes)

    print(f"Computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!\n")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você venceu esta rodada!\n")
        pontuacao_usuario += 1
    else:
        print("Computador venceu esta rodada!\n")
        pontuacao_computador += 1

# Resultado final
print("Resultado final:")
print(f"Você venceu {pontuacao_usuario} rodadas.")
print(f"O computador venceu {pontuacao_computador} rodadas.")

if pontuacao_usuario > pontuacao_computador:
    print("🎉 Parabéns, você ganhou o jogo!")
elif pontuacao_usuario < pontuacao_computador:
    print("😢 O computador ganhou o jogo!")
else:
    print("🤝 O jogo terminou empatado!")

