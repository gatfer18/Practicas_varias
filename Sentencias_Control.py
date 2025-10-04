'''
EJERCICIOS DE SENTENCIAS DE CONTROL

'''

#(1.-EJERCICIO) Mayor de dos números:
#Pide dos números al usuario y muestra cuál es mayor, o si son iguales.

numero1 = int(input("Introduce un numero:  "))
numero2 = int(input("Introduce un numero:  "))
if numero1 > numero2:
    print(f'El 1er numero es mayor: {numero1}')
elif numero1 < numero2:
    print(f'El 2nd numero es mayor: {numero2}')
elif numero1 == numero2:
    print(f'Los numeros introducidos son iguales  ')
else:
    print(f' Introduce cifras enteras  ')

#~(2.-EJERCICIO)Número positivo, negativo o cero:
#Pide un número y muestra si es positivo, negativo o cero.

num = float(input("Introduce un numero: "))
if num > 0:
    print(f'El numero es positivo  ')

elif num < 0:
    print(f'El numero es negativo  ')
else:
    print(f'El numero es zero  ')

#(3.-EJERCICIO) Clasificación de edades:
#Pide la edad de un usuario y muestra si es niño (0-12), adolescente (13-17), adulto (18-64) o adulto mayor (65+).

edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad <=12:
    print(f'Actualy you are a child')
elif edad >= 12 and edad <=17:
    print(f'Actualy you are a teenager')
elif edad >= 18 and edad <=64:
    print(f'actualy you are a adult ')
elif edad >= 65 and edad <=200:
    print( 'Congratulation you are aged' )

#(4.-EJERCICIO)
#Pide una nota de 0 a 100 y muestra si el alumno aprobó (>=60) o reprobó.
nota = float(input("Introduce tu nota: "))
if nota >= 0 and nota <= 60.00:
    print ('Sorry that your grade wasnt enough to pass ')
elif nota > 60.00:
    print ('“Congratulations! You have a good grade. You passed! ')
else:
    print ('introduce your mark ')












