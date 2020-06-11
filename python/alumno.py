class Alumno:
        
        def __init__(self, nombre, nota):
            self.nombre = nombre
            self.nota = nota
            
        def imprimir(self):
            print("Alumno: ",self.nombre)
            print("Nota: ", self.nota)
            print("")
            
        def resultado(self):
            if self.nota < 5:
                print("El alumno quedo reprobado")
            else:
                print("Felicidades usted ha pasado")
                
alumno1 = Alumno("Armando", 3)
alumno2 = Alumno("Juan", 5)
alumno3 = Alumno("Antonio", 8)
    
alumno1.imprimir()
alumno1.resultado()
    
alumno2.imprimir()
alumno2.resultado()
    
alumno3.imprimir()
alumno3.resultado()
