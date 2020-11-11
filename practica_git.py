def run ():
    print("este se cruza el cambio para git")
    print("en este narraremos nuestra esta historia en la programacion")
    print("este programa realiza suma de numeros ")
    funcion_suma()

def funcion_suma ():

    print("por favor registra los valores para realizar la suma")
    valor_1 = float(input("registra el primer valor "))
    valor_2 = float(input("registra el segundo valor "))
    suma = valor_1 + valor_2

    print(suma)



if __name__ == "__main__":
    run()