'''
**** Practicas del ciclo for *****
'''

print('\nEJERCICIO 1.Imprimir los números del 1 al 10.' )

for i in range(1,11):
    print(i, end='-')

print('\n\nEJERCICIO 2.Imprimir la tabla de multiplicar de cualquier numero .')

n = int(input("Que tabla de multiplicar quieres ver?: "))
for i in range(1,13):
    resultado = n * i
    print( n,"x",i,"=",resultado)


print('\n\nEJERCICIO 3.Imprimir todos los números pares entre 1 y 50..')

for numero in range(1,51):
    if numero % 2 == 0:
        print(numero, end='-')



print('\n\nEJERCICIO 4.Calcular el factorial de un número dado')

numero =  int(input("Ingrese un numero: "))
factorial = 1
for i in range(1,numero + 1):
    factorial = factorial * i

print( f'El factorial del numero: {numero} es: {factorial:.2f} ' )




print('\n\nEJERCICIO 5.Pedir 5 números al usuario y mostrar su promedio' )

suma = 0
for i in range(5):
    numero = float(input( 'Ingresa un numero: '))
    suma += numero

promedio = suma / 5

print( 'El promedio de los 5 numeros introducidos  es: ', promedio)


print('\n\nEJERCICIO 6 .Contar cuántas vocales tiene una palabra ingresada por el usuario.' )

palabra = input("Ingresa una palabre:  ").lower()
vocales =  'aeiou'
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra introducidad tiene: {contador}, Vocal(es).")


print('\n\nEJERCICIO 7 .Mostrar los caracteres de una cadena, uno por línea.' )

cadena = input("Escribe una Palabra o Frase: ").lower()

for caracter in cadena:
    print( caracter, end= ' - ')


print('\n\nEJERCICIO 8 .. Contar hasta la edad: Pregunta al usuario su edad y '
         ' muestra todos los años que ha cumplido, desde el 1 hasta su edad.' )


edad = int(input("Inserta tu edad: "))

for año in range (1, edad +  1):
    print(f"año, {año}: ¡Feliz cumpleaños numero {año}! ", end=' - ')

meses = edad * 12
dias = edad * 365

print("\n--- RESUMEN DE TU VIDA ---")
print(f"Tienes {edad} año(s).")
print(f"Has vivido aproximadamente {meses} meses.")
print(f"Y unos {dias} días en total.")




print('\n\nEJERCICIO 9.. Crea un programa que imprima un patrón de asteriscos en forma de triángulo ' )

numero_filas = int(input("Ingresa la altura del triangulo: "))

for fila in range(1, numero_filas + 1):
    espacios_blanco =  ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila -1)
    print(f'{espacios_blanco}{asteriscos} ')





print('\n\nEJERCICIO 10.. Crea un programa que imprima un patrón de asteriscos en forma de cuadrado ' )

n = int(input("Ingrese la altura del cuadrado: "))
borde = input("ingrese el caracter del borde de su cuadrado: ")
relleno = input('Ingrese el caracter para el interior de su cuadrado: ')

for i in range(1,n +1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:

            print(borde, end= " ")
        else:
           print( relleno, end=" ")
    print()















