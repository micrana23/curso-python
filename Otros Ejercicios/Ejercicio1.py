#Programa que imprime el nombre de un alumno, la nota y si está aprobado o no

class Estudiante:

    #Constructor 
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    #Método para mostrar los datos
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    
    #Método para indicar si ha aprobado
    def mostrar_resultado(self):
        if self.nota >=5:
            print("Ha aprobado")
        else:
            print("Ha suspendido")

#Crear objeto
alumno1 = Estudiante("Ana", 8)
#LLamar a los métodos
alumno1.imprimir()
alumno1.mostrar_resultado()

alumno2 = Estudiante("Juan", 4)
alumno2.imprimir()
alumno2.mostrar_resultado()



