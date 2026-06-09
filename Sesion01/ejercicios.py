#Ejercicios con if


#Ejercico 1: Número positivo
#Pedimos al usuario que introduzca un número
numero = float(input("Introduce un número: "))

#Comprobamos si el número es mayor que 0
if numero > 0:
    #Comprobamos si el numero es mayor que 0
    print("El número es positivo")

print("--------------------------------------------------")

#Ejercicio 2: Mayor de edad
#Pedicmos al usuario que introduzca su edad
edad = int(input("Introduce tu edad: "))

#Comprobamos si es mayor de edad
if edad >= 18:
    print("Eres mayor de edad")

print("---------------------------------------------------")
          
#Ejercicio 3: Nota aprobada
#Pedimos al usuario que introduzca una nota
nota = float(input("Introduce una nota: "))

#Comprobamos si la nota es igual o mayor que 5
if nota >= 5:
    print("Aprobado")

print("--------------------------------------------------------")

#Ejercicios con if-else

#Ejercicio 4: Numero par o impar
#Pedimos al usuario que introduzca un numero entero
numero = int(input("Introduce un numero: "))

#Comprobamos si el resto de dividir 2 es 0
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

print("---------------------------------------------------------")

#Ejercico 5:n Acceso al sistema
#Pedimos al usuario que introduzca una contraseña
contraseña = input("Introduce una contraseña: ")

#Comprobamos que la contraseña sea correcta
if contraseña == "python123":
    print("Acceso concedido")
else:
    print("Acceso denegado")

print("---------------------------------------------------------")

#Ejercicio 6: Comprobar dos números
#Pedimos al usuario que introduzca un numero
numero1 = float(input("Introduce un número: "))

#Pedimos al usuario que introduzca otro numero
numero2 = float(input("Introduce otro numero: "))

#Comprobamos cual es mayor
if numero1 > numero2:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor")

print("----------------------------------------------------------")

#Ejercicios if-elif-else

#Ejercicio 7: Calificación
#Pedimos al usuario que introduzca una nota
nota = float(input("Introduce una nota del 0 al 10: "))

#Comprobamos si está suspenso, aprobado, notable o sobresaliente
if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")

print("---------------------------------------------------------")

#Ejercicio 8: Temperatura
#Pedimos al usuario que introduzca una temperatura
temperatura = float(input("Introduce una temperatura: "))

#Clasificamos la temperatura
if temperatura < 10:
    print("Hace frio")
elif temperatura <= 25:
    print("Temperatura agradable")
else:
    print("Hace calor")

print("--------------------------------------------------------")

#Ejercicio 9: Calculadora simple
#Pedimos al usuario introducir los números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

#Pedimos la operacion
operacion = input("Introduce una operación (+,-, *, /): ")

#Realizamos la operación correspondiente
if operacion == "+":
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
     print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    print("Resultado:", numero1 /numero2)
else:
    print("Operación no válida")

print("--------------------------------------------------")

#Ejercicio 10: Clasificación por edad
#Pedimos la edad al usuario
edad = int(input("Introduce tu edad: "))

#Comprobamos en que rango de edad está
if edad < 12:
    print("Niño")
elif edad <18:
    print("Adolescente")
elif edad <65:
    print("Adulto")
else:
    print("Jubilado")

print("---------------------------------------------------")

#Ejercicio 11: Dia de la semana
#Pedidmos un número del 1 al 7
dia = int(input("Introduce un número del 1 al 7: "))

#Comprobamos el valor usando match
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número no válido")

print("----------------------------------------------------")

#Ejercicio 12: Menú de restaurante
#Mostramos el menú
print("1. Pizza")
print("2. Hamburguesa")
print("3. Ensalada")

#Pedimos una opción
opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Has elegido pizza")
    case 2:
        print("Has elegido hamburguesa")
    case 3:
        print("Has elegido ensalada")
    case _:
        print("Opción no válida")

print("-----------------------------------------------------")

#Ejercicio 13: Calculadora con match
#Pedimos los dos números
numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))

#Pedimos la operación
operacion = input("Introduce una operación (+,-,*,/): ")

#Resultado de la operación que ha realizado el usuario
match operacion:
    case "+":
        print("Resultado:", numero1 + numero2)
    case "-":
        print("Resultado:", numero1 - numero2)
    case "*":
        print("Resultado:", numero1 * numero2)
    case "/":
        print("Resultado:", numero1 / numero2)
    case _:
        print("Operación no válida")

print("------------------------------------------------------")

#Ejercicio 14: Mes del año
#Pedimos un número del 1 al 12
mes = int(input("Introduce un número del 1 al 12: "))

#Mostramos el mes correspondiente
match mes:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case 13:
        print("Número de mes no válido")

print("--------------------------------------------------------")

#Ejercicio 15: Descuento en tienda
#Pedimos el importe de la compra
importe = float(input("Introduce el importe de tu compra: "))

#Comprobamos el importe que corresponde
if importe < 50:
    descuento = 0
elif importe < 100:
    descuento = 5
elif importe < 200:
    descuento = 10
else:
    descuento = 15

#Calculamos el precio final
precio_final = importe - (importe *descuento /100)

print("Descuento aplicado: ", descuento, "%")
print("Precio final: ", precio_final, "€")

print("------------------------------------------------------")

#Ejercicio 16: Piedra, papel o tijera

#Pedimos  la elección del usuario
opcion = input("Elige piedra, papel o tijera: ")

#Mostramos un mensaje según la opción elegida
match opcion:
    case "piedra":
        print("Has elegido piedra. La piedra rompe las tijeras")
    case "papel":
        print("Has elegido papel. El papel envuelve a la piedra")
    case "tijera":
        print("Has elegido tijera. La tijera corta el papel")
    case _:
        print("Opción no valida")

print("-------------------------------------------------------")

#Ejercicio 17: Año bisiesto
#Pedimos un año
anio = int(input("Inntoduce un año: "))

#Comprobamos si es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

print("----------------------------------------------------------")

#Ejercicio 18: Cajero automatico
#Pedimos el saldo disponible
saldo = float(input("Introduce tu saldo: "))

#Pedimos la cantidad a retirar
retirada = float(input("Cantidad a retirar: "))

#Comprobamos si hay fondo suficiente
if retirada > saldo:
    print("Saldo insuficiente")
else:
    saldo -= retirada

    print("Retirada realizada")
    print("Saldo restante:", saldo, "€")

print("-----------------------------------------------------------")

#Ejercicio 19: Conversor de notas
# Pedimos una letra al usuario
nota = input("Introduce una nota (A, B, C, D, F): ")

# Comprobamos la letra usando match
match nota:
    case "A":
        print("Excelente")

    case "B":
        print("Notable")

    case "C":
        print("Aprobado")

    case "D":
        print("Suficiente")

    case "F":
        print("Suspenso")

    case _:
        print("Nota no válida")

print("------------------------------------------------------------")

#Ejercicio 20: Clasificador de triángulos
# Pedimos los tres lados del triángulo
lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

# Comprobamos el tipo de triángulo
if lado1 == lado2 and lado2 == lado3:
    print("Equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")

else:
    print("Escaleno")
    







    


    





