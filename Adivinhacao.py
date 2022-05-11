import random

def jogar():

    print("################################")
    print("Bem Vindo no jogo de Adivinhação")
    print("################################")

    numero_secreto = random.randint(1, 100)
    chute = 0
    num_total = 0

    print("\nQual o nível de dificuldade você quer jogar ?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = input("\nDefina o Nível: ")

    if nivel.isnumeric():

        if(nivel == '1'):
            total = 15
        elif(nivel == '2'):
            total = 10
        elif(nivel == '3'):
            total = 5
        else:
            print("Você escolheu um nível errado, por isso o jogo vai atribuir tentativas a você.")
            total = random.randint (5, 8)
    else:
        print("Digitou algum caractere (PENALIDADE GRAVE) Jogo vai dá o Nível difícil a você.")
        total = 5


    while(total != 0 and chute != numero_secreto):

        print(f" Você tem {total} tantivas.")
        total -= 1
        num_total += 1
        chute = input("\nDigite um número entre 1 a 100 ")

        if chute.isnumeric():
            chute = int(chute)

            if(numero_secreto == chute):
                print(f"\nVocê Acertou na {num_total}° tentativa, parabéns!!")
            else:
                if(chute > numero_secreto):
                    print("\nVocê Errou, seu chute foi MAIOR que o número secreto.")
                else:
                    print("\nVocê Errou, seu chute foi MENOR que o número secreto.")
        else:
            print("\nNão é um número válido, digite apenas um número entre 1 a 100 para verificação.")
        if(total == 0):
            print("\nTentativas esgotadas, você perdeu!!")

    else:
        print("\nFim do Jogo.")

if(__name__ == '__main__'):
    jogar()
