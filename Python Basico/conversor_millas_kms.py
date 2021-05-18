def mil_km():
    factor_milla = 1.609344
    millas = float(input("Ingrese la cantidad de Millas a Convertir: "))
    kilometros = millas * factor_milla
    kilometros = round(kilometros,2)
    print("el Equivalente en Kilometros es " + str(kilometros))

def km_mil():
    factor_milla = 1.609344
    kilometros = float(input("Ingrese la cantidad de Kilometros a Convertir: "))
    millas = kilometros / factor_milla
    millas = round(millas,2)
    print("el Equivalente en Millas es " + str(millas))

def run():
    opcion = int(input("""
    Bienvenido al conversor de medidas
   
    1 - Millas a Kilometros
    2 - Kilometros a Millas

    Seleccióne una Opción:
    """))
    if opcion == 1:
        mil_km()
    elif opcion == 2:
        km_mil()
    else:
        print("Opcion invalida")
        run()


if __name__ == "__main__":
    run()