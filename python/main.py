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

                def finalizar():
                    print("*************************")
                    print("Gracias")

                    presentacion()
                    introducirdatos()
                    sumar()
                    restar()
                    finalizar()
        