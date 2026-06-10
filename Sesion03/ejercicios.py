#Ejercicio 1: Pedir la edad y mostrar los años cumplidos desde 1 hasta su edad
#Pedimos la edad al usuario
edad = int(input("Introduce tu edad: "))

#Mostramos los años cumplidos
for anio in range(1, edad +1):
    print(anio)

print("------------------------------------------")

#Ejercicio 2:Mostrar todos los numeros impares desde 1 hasta el número introducido por el usario
#Pedimos al usuario un número
numero = int(input("Introduce un número entero positivo: "))

#Recorremos los numeros impares
for impar in range(1, numero +1, 2):
    print(impar, end=", ")

print("------------------------------------------------")

