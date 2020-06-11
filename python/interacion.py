#realizar un programa que conste de una clase llamada alumno que tenga como atributo el numbre y la nota del alumno.
# definir los metodos para iniciar sus atibutos, imprimirlos y mostrar un mensaje con la nota y si ha aprobado o no.

class Alumno:
        
        def __init__(self):
            self.nombre = input("Nombre del Alumno: ")
            self.nota = input("Nota final: ")
            
        def imprimir(self):
            print("Alumno: ",self.nombre)
            print("Nota: ", self.nota)
            print("")
            
        def resultado(self):
            if int(self.nota) < 5:
                print("El alumno quedo reprobado")
            else:
                print("Felicidades usted ha pasado")
                
alumno1 = Alumno()
alumno1.imprimir()
alumno1.resultado()
    
    
