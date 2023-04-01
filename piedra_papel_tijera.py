import random


def verify(op1, op2):
    if op1 == 0 and op2 == 2 or op1 == 1 and op2 == 0 or op1 == 2 and op2 == 1:
        return op1
    return op2


options = ('piedra', 'papel', 'tijera')
print("\n¡¡Bienvenido al juego de Piedra, Papel o Tijera \n Te vas a enfretar al computador !!")
rounds = int(input('¿a cuantas victorias quieres jugar?\n'))
print("\n***** EMPECEMOS *****")

user_win = 0
computer_win = 0
round_count = 0
while True:
    round_count += 1
    print("RONDA: ", round_count)

    print(
        f'Puntos del usuario: {user_win}\nPuntos de la computadora: {computer_win}\n')
    user_option = input("Escoge: piedra, papel o tijera:\n").lower()

    if user_option not in options:
        print(f'{user_option} no es una opcion valida, por favor ingresa una valida')
        continue

    print("-"*25)
    computer_option = random.choice(options)
    print(
        f'\nTu opcion: {user_option} \nOpcion de la computadora: {computer_option}')

    if user_option == computer_option:
        print("Empate\n")
        continue

    op1 = options.index(user_option)
    op2 = options.index(computer_option)

    ganador = verify(op1, op2)
    print(f'\n{options[op1]} gana a {options[op2]}:')

    if op1 == ganador:
        print("*** GANO EL USUARIO ***")
        user_win += 1
    else:
        print("*** GANO LA COMPUTADORA ***")
        computer_win += 1

    if user_win == rounds or computer_win == rounds:
        break
