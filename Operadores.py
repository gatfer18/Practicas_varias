'''
 EJERCICIOS PARA TRABAJAR CON LOS DIFERENTES OPERADORES EN PYTHON
'''

#EJERCICIOS CON OPERADORES ARITMETICOS:

#1(.-EJERCICIO)  Suma y resta: Pide dos números al usuario y muestra su suma y su resta.

x = float(input( 'Introduce una cifra:  '))
y = float(input( 'Introduce una cifra: '))
resultado = x + y
rsultado = x - y
print(f'la suma de las dos cifras introducidas es: {resultado}, y la resta es: {rsultado} ')
print( f'la suma de las dos cifras es {x + y}, y la resta de las dos cifras es {x - y}')


#2(.-EJERCICIO)  Producto y división: Pide dos números y muestra su producto y su división.

a = float(input( 'Introduce una cifra:  '))
b = float(input( 'Introduce una cifra: '))
print(f'El producto de {a} y de {b} las dos cifras introducida es: {a * b}, y la division es: {a // b } ')

#3(.-EJERCICIO) División entera y módulo: Pide dos números y muestra el cociente entero y el residuo de la división.

a = float(input( 'Introduce una cifra:  '))
b = float(input( 'Introduce una cifra: '))
print(f'se muestra el cociente entero de las cifra {a} y la cifra {b}: Cociente entero {a // b} y el residio: {a % b}' )

#4(.-EJERCICIO) Potencia:Pide un número y muéstralo elevado al cuadrado y al cubo.

a = int(input( 'Introduce un numero:'))
print(f'el cuadrado de la cifra: {a} es { a ** 2}  y la cifra al cubo es: { a ** 3}')

#5(.-EJERCICIO) Mayor o menor: Pide dos números y muestra si el primero es mayor, menor o igual al segundo.
a = float(input( 'Introduce una cifra:  '))
b = float(input( 'Introduce una cifra: '))
if a > b:
    print(f'la cifra {a} es mayor')
elif a == b:
    print(f'las cifras son iguales ')
else:
    print(f'la 1 cifra es menor que la 2')

#6(.-EJERCICIO) Edad mínima: Pide la edad de un usuario y muestra si es mayor o menor de edad.

edad = int(input('introduce tu edad:  '))
if edad >18:
    print( 'Eres mayor de edad')
else:
    print( 'Lo siento no eres mayor de edad ')

#7(.-EJERCICIO)Comparar cadenas: Pide dos palabras y muestra si son iguales o diferentes.

cadena1 = str(input('Introduce una palabra: '))
cadena2 = str(input('Introduce otra Palabra: '))
if cadena1 == cadena2:
    print(f'Las palabras son iguales')
else:
    print(f'Las palabras son diferentes')

#8(.-EJERCICIO) Rango de edad: Pide la edad de un usuario y verifica si está entre 18 y 30 años.

edad = int(input( 'Escribe tu edad: '))
if edad >= 18 and edad <= 30:
    print( 'Estas en el rango de no clasificado')
else:
    print('Estas en el rango ganador ')

#9(.-EJERCICIO) Condición múltiple: Pide un número y muestra si es positivo y par al mismo tiempo

num = int(input( 'Introduce un numero: '))
if num > 0 and num % 2 ==0:
    print(' El numero proporcionado es par y es positivo ')
else:
    print( 'El numero no cumple las  caracteristicas')



#10(.-EJERCICIO)Negación lógica:Pide un número y muestra si no es mayor que 100.

num = int(input( 'Introduce un numero: '))
if num >100:
    print( 'el numero es mayor que 100')
else:
    print('El numero es menor que 100 ')

