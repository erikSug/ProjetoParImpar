import random

def par_impar():
    print("_" * 40)
    print(" Bem-vindo ao Jogo Par ou Ímpar")
    print("_" * 40)

    vitorias_usuario = 0
    vitorias_ia = 0

    while True:
        escolha_usuario = input(
            "\nEscolha [P]ar ou [I]mpar - [S] para sair: "
        ).strip().upper()

        if escolha_usuario == "S":
            print("\nSaindo do jogo...")
            break

        if escolha_usuario not in ["P", "I"]:
            print("Opção inválida! Digite P, I ou S.")
            continue

        try:
            numero_usuario = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue

        # A IA escolhe um número
        numero_ia = random.randint(0, 10)

        # Calcula a soma e verifica o resultado
        soma = numero_usuario + numero_ia
        resultado = "P" if soma % 2 == 0 else "I"
        resultado_texto = "PAR" if resultado == "P" else "ÍMPAR"

        print("_" * 40)
        print(f"Você jogou {numero_usuario} e a IA jogou {numero_ia}.")
        print(f"A soma foi {soma} ({resultado_texto}).")

        # Verifica quem venceu
        if escolha_usuario == resultado:
            print("Parabéns! Você ganhou esta rodada!")
            vitorias_usuario += 1
        else:
            print("A IA ganhou esta rodada!")
            vitorias_ia += 1

        print(
            f"Placar atual -> Você: {vitorias_usuario} | "
            f"IA: {vitorias_ia}"
        )
        print("=" * 40)

    # Placar final: aparece somente ao sair
    print("\nFim de jogo! Placar final:")
    print(f"Você: {vitorias_usuario} vitória(s)")
    print(f"IA: {vitorias_ia} vitória(s)")
    print("Obrigado por jogar!")
    print("=" * 40)


par_impar()