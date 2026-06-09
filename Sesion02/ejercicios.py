#Ejercicio 1: Mostrar números del 1 al 10
#Iniciamos en 1
numero = 1

#Mientras el numero sea menor o igual a 10
while numero <= 10:
    print(numero)
    #Incrementamos el numero en 1
    numero +=1

print("----------------------------------------------------------")

#Ejercicio 2: Mostrar números del 10 al 1
#iniciamos en 10
numero = 10

#Mientras el numero sea mayor o igual a 1
while numero >= 1:
    print(numero)
    #Restamos el numero en 1
    numero -=1

print("----------------------------------------------------------")

#Ejercicio 3: Mostrar tu nombre varias veces

#Pedimos un numero al usuario
veces = int(input("¿Cuántas veces quieres repetir tu nombre?"))

contador = 1

#Repetimos mientras el contador no supere el número indicado
while contador <= veces:
    print("Ana")

    contador +=1

print("----------------------------------------------------------")

#Ejercicio 4: Suma de los números del 1 al 100
#Variables
numero= 1
suma= 0

#Sumamos de 1 a 100
while numero <= 100:
    suma += numero
    numero += 1

print("La suma total es: ",suma)

print("----------------------------------------------------------")

#Ejercicio 5: Tabla de multiplicar
#Pedimos el numero
numero = int(input("Introduce un número: "))

multiplicador = 1

#Mostramos la tabla del 1 al 10
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)

    multiplicador +=1

print("----------------------------------------------------")

#Ejercicio 6: Números pares entre 2 y 10
#Empezamos en el 2
numero = 2

while numero <= 20:
    print(numero)

#Saltamos de 2 en 2
    numero += 2

print("----------------------------------------------------")

#Ejercicio 7: Contraseña correcta
contraseña= ""

#Mientras la contraseña no sea correcta
while contraseña != "python123":
    contraseña = input("Introduce la contraseña: ")

print("Acceso concedido")

print("----------------------------------------------------")

#Ejercicio 8: Adivinar el numero

#Guardamos el número secreto
numero_secreto = 5

#Valor inicial
numero = 0

#Mientras no acierte
while numero != numero_secreto:
    numero = int(input("Adivina el número secreto: "))

print("¡Has acertado!")

print("----------------------------------------------------")

#Ejercicio 9: Sumar números hasta introducir 0
#Iniciamos la suma
suma = 0

#Pedimos el primer número
numero = int(input("Introduce un número: " ))

while numero != 0:
    suma += numero
    numero = int(input("Introduce otro número: "))

print("La suma total es: ",suma)

print("----------------------------------------------------")

#Ejercicio 10: Contar cifras de un número
#Pedimos un número positivo
numero = int(input("Introduce un número entero positivo: "))

#Contador de cifraws
cifras= 0

while numero > 0:
    numero = numero // 10

    cifras +=1

print("El número tiene", cifras, "cifras")