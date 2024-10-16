import random

print("Seja bem vindo so random game")

numero_Escolhido = input("Digite seu numero: ")

if numero_Escolhido.isdigit():
    numero_Escolhido = int(numero_Escolhido)
else:
    print("Erro")
    quit()

random_number = random.randint(0, numero_Escolhido)

n_choices = 0

while True:
    resposta_user = input("Advinha o numero: ")

    if resposta_user.isdigit():
        resposta_user = int(resposta_user)
    else:
        print("Erro! por favor insere um numero")
        continue

    n_choices  = n_choices + 1

    if resposta_user == numero_Escolhido:
        print('Acertou')
        break
    elif resposta_user > random_number:
        print("Chutou alto. veja mais baixo...")
    else:
        print("chutou baixo, tente mais alto ")

print("n de tenativas: " + str(n_choices))
