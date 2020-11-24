def run ():
    print("Esta es la calculadora de confianza")
    print("escoje la operacion que deseas realizar ")
    print('''
        para suma seleccione +
        para resta selecciones - ''')

    operator = str(input("seleciona la operacion "))

    if operator == "+":
        funcion_suma()
    elif operator == "-":
        funcion_resta()
    

def funcion_suma ():

    print("por favor registra los valores para realizar la suma")
    valor_1 = float(input("registra el primer valor "))
    valor_2 = float(input("registra el segundo valor "))
    suma = valor_1 + valor_2

    print(suma)

def funcion_resta ():

    print("por favor registrar los valores para realizar la suma")
    valor_1 = float(input("registre el primer valor"))
    valor_2 = float(input("registre el segundo valor"))
    resta = valor_1 - valor_2

    print(resta)


if __name__ == "__main__":
    run()
