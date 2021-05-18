def ganador(player1, player2):
    player1 = player1.lower().strip()
    player2 = player2.lower().strip()
    if player1 == "tijera" and player2 == "papel":
        print("Ganó el jugador 1")
    elif player1 == "papel" and player2 == "piedra":
        print("Ganó el jugador 1")
    elif player1 == "piedra" and player2 == "tijera":
        print("Ganó el jugador 1")
    elif player2 == "tijera" and player1 == "papel":
        print("Ganó el jugador 2")
    elif player2 == "papel" and player1 == "piedra":
        print("Ganó el jugador 2")
    elif player2 == "piedra" and player1 == "tijera":
        print("Ganó el jugador 2")
    else:
        print("ingrese una opcion valida")


def run():
    print("""Bienvenido al Juego

    Ingrese Piedra, Papel o Tijera

    """)

    pl1 = input("Ingrese Opcion Jugador 1: ")
    pl2 = input("Ingrese Opcion Jugador 2: ")

    ganador(pl1, pl2)

if __name__ == "__main__":
    run()