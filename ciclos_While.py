'''
EJERCICIOS PARA PRACTICAR EL CICLO WHILE
'''

print('**** ESTO ES UNA LISTA DE EJERCICIOS PARA PRACTICA EL CICLO WHILE ***** ')

print('\n*** EJERCICIO 1.- Imprimir los números del 1 al 10.')

contador = 1
while contador <= 10:
    print( contador, end= ' - ')
    contador +=1


print('\n\n*** EJERCICIO 2.- Hacer un conteo regresivo desde un número 12 hasta 0.')

cont = 12
while cont >= 0:
    print( cont, end= ' - ')
    cont -=1

print('\n\n*** EJERCICIO 3.- Pedir números al usuario hasta que ingrese el 0, y luego mostrar la suma total ')

sum_total = 0
num = int(input(' Ingrese Un numero: ')) 
while num != 0:
    sum_total += num
    num =int(input("Ingresa un número (0 para salir): "))
print(f'La suma total de los numeros que has ingresado es: {sum_total}')






