def run ():
    print("este es mi primer programa para git")
    print("en esta es la prueba de git con ssh ")
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
