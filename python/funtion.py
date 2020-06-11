def presentacion():
    print("Programa para hacer operaciones Aritmeticas.")
    print("*********************************************")

def introducirdatos():
        global valor1
        global valor2
        valor1=int(input("Ingrese el primer valor:"))
        valor2=int(input("Ingrese el segundo valor:"))

def sumar():
            global suma
            suma = valor1 + valor2
            print("la suma es:", suma)
def restar():
                global resta
                resta = valor1 - valor2
                print ("el Valor de la resta es: ", resta)

def mult():
            global multip
            multip = valor1 * valor2
            print("la multiplicacion es:", multip)
def div():
                global divi
                if int(valor2 ==0):
                    print("La division por 0 no existe")
                else:
                    divi = valor1 / valor2
                    print ("el Valor de la division es: ", divi)


def finalizar():
                    print("*************************")
                    print("Gracias")

presentacion()
introducirdatos()
sumar()
restar()
mult()
div()
finalizar()
        