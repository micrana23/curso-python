#Ejercicio contador de productos

class Producto:

    #Atributo de clase
    contador_productos = 0

    #Constuctor
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        #Incrementamos el contador cada vez que se cree un producto
        Producto.contador_productos +=1

    #Método de clase
    @classmethod
    def total_productos(cls):
        return f"Total de productos creados: {cls.contador_productos}"
    
    #Método para calcular el valor total del stock
    def valor_total_stock(self):
        return self.precio * self.stock
    
    #Método para mostrar la información del producto
    def __str__(self):
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: {self.precio}\n"
            f"Stock: {self.stock}\n"
        )
# Lista donde almacenaremos los productos
productos = []

# Añadimos productos a la lista
productos.append(Producto("P001", "Portátil", 899, 2))
productos.append(Producto("P002", "Televisor", 500, 3))
productos.append(Producto("P003", "Teclado", 25, 6))

# Mostrar todos los productos
for producto in productos:
    print(producto)
    print("Valor total del stock:", producto.valor_total_stock(), "€")
    print("----------------")

#Mostrar número total de productos creados
print(Producto.total_productos())