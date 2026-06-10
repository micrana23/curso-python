class Triangulo:

    #Constructor
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    #Metodo para comprobar si es un triangulo valido
    def es_valido(self):
        return(
            self.lado1 + self.lado2 > self.lado3 and
            self.lado1 + self.lado3 > self.lado2 and
            self.lado2 + self.lado3 > self.lado1
        )
    
    #Metodo para mostrar el lado mayor
    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2,self.lado3)
        print("El lado mayor es:", mayor)
    
    #Método para mostrar el tipo de triángulo
    def tipo_triangulo(self):
        if not self.es_valido():
            print("No es un triángulo válido")
            return
        
        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triángulo equilatero")

        elif (
            self.lado1 == self.lado2 or
            self.lado1 == self.lado3 or
            self.lado2 == self.lado3
        ):
            print("Es un triángulo isosceles")
        
        else:
            print("Es n triángulo escaleno")

#crear objeto
triangulo= Triangulo(5, 5, 3)

#Mostramos la infrmacion
triangulo.lado_mayor()
triangulo.tipo_triangulo()




        