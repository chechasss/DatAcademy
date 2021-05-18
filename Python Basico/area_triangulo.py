def area(base,altura):
    area_total = (base*altura)/2
    print("El área del triangulo es: " + str(area_total))

def run():
    base = int(input("Ingrese la longitud de la Base: "))
    altura = int(input("Ingrese la longitud de la altura: "))
    area(base,altura)

if __name__ == "__main__":
    run()