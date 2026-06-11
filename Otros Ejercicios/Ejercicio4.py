#Crear una clase Libro y mostrar su información ademas de compararel número de páginas entre los libros
#para saber qué libro tiene más páginas

class Libro: 

    #Constructor
    def __init__(self, isbn, titulo, autor, paginas):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    #Metodo para mostrar la información del libro
    def imprimir(self):
        print("ISBN:", self.isbn)
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.paginas)

    #Método para comparar páginas con otro libro
    def comparar_paginas(self, otro_libro):
        if self.paginas > otro_libro.paginas:
            print(f"{self.titulo} tiene más páginas que {otro_libro.titulo}")

        elif self.paginas < otro_libro.paginas:
            print(f"{self.titulo} tiene menos páginas que {otro_libro.titulo}")

        else:
            print(f"{self.titulo} y {otro_libro.titulo} tienen el mismo número de páginas")

 #Creamos los objetos
libro1 = Libro(
    "9788401023522",
    "El Quijote",
    "Miguel de Cervantes",
     863
 )

libro2 = Libro(
     "9788420471839",
     "La sombra del viento",
     "Carlos Ruiz Zafón",
     864
 )

#imprimimos la información
libro1.imprimir()

print("-----------------------------------------------------------")

libro2.imprimir()

#Comparar los libros

libro1.comparar_paginas(libro2)

  

        

     