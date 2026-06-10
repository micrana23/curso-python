class Estudiante2:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre}\nNota: {self.nota}"
    
    def resultado (self):
        if self.nota >5:
            return "Ha aprobado"
        return "Ha suspendido"

estudiante1 = Estudiante2("Mario", 6)
print(estudiante1)
print(estudiante1.resultado())

estudiante2 = Estudiante2("Julio", 3)
print(estudiante2)
print(estudiante2.resultado())