from random import randint
from xml.dom.minidom import ProcessingInstruction

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

print('\n\n*** EJERCICIO 4.- Pedir una contraseña hasta que el usuario la escriba correctamente. ')

password1 =   (input( 'Ingresa la contraseña(a-z) no num: '))
password2 =  'Login'
while password1 != password2:
    respuesta = (input( 'Contraseña incorrecta desea continuar:  '))
    if respuesta == 'si':
        password1 = (input( 'Ingresa de nuevo la contraseña(a-z) no num: ' ))
    else:
        print( 'Saliendo del sistema.....')
        break

if password1 == password2:
    print( '***** Bienvenido al Sistema **** ')

print('\n\n*** EJERCICIO 5.- Adivinar un número secreto (predefinido en el código). ')

num_secr = randint(1, 70)

intentos = 0
intentos_max = 3
adivinado = False

print( "¡¡Bienvenido al juego adivinar numero!!")
print( "*** Adivina el numero secreto entre 1 y  70 ***")

while adivinado != num_secr and intentos < intentos_max:
    adivinado = int(input( 'Adivina el numero secreto entre 1  y  70: '))
    if adivinado < num_secr:
        print( 'WARM.!! El numero es mayor')
    elif adivinado > num_secr:
        print( 'COLD.!! El numero es menor ')
    intentos += 1

if adivinado == num_secr:
    print( 'CONGRATULATIONS.!! Lo has logrado')
else:
    print(f'Lo sentimos has agotado el numero de intentos maximos: {intentos_max} ')
    print(f'El numero secreto era : {num_secr}')



print('\n\n*** EJERCICIO 6.- Calcular la suma de los números pares menores a 100 ')

suma_pares = int(input(  'Ingresa un numero menor a  100: '))
numero = 0
while numero < 100: #verifico si el numero es par
    if numero % 2  == 0:
        suma_pares += numero # sumo el numero par a la variable suma_pares
    numero += 1
#Imprimo el resultado
print(f'La suma de los numeros pares menores a 100 es: {suma_pares}')

print('\n\n*** EJERCICIO 7.- Mostrar los dígitos de un número uno por uno ')

n = int(input(' Ingresa un numero de mas de cuatro digitos : '))
tempe = n
contador = 0
while tempe  > 0:
    tempe = tempe // 10
    contador += 1
#CREAMOS UN DIVISOR PARA EXTRAER DIGITO POR DIGITO
divisor = 10 ** (contador - 1)
tempe = n
while divisor > 0:
    digito = tempe // divisor
    print(digito, end=' - ')
    tempe = tempe % divisor
    divisor = divisor // 10

#FORMA SENCILLA Y FACIL DE COMPRENDER

nm = int(input( '\nIngresa Un numero mayor de 3 digitos: '))
numero_str = str(nm)
i = 0
while i < len(numero_str):
    print(numero_str[i], end=' - ')
    i += 1

print('\n\n*** EJERCICIO 8.- Leer números hasta que el usuario ingrese un número negativo.')

numeros = [] # NOS CREAMOS UNA LISTA PARA ALMACENAR LOS NUMEROS

num = int(input( 'Ingresa un numero (ingresa un numero negativo para detener: )'))

while num >= 0:
    numeros.append(num)#con esto añadimos el numero a la lista
    num = int(input( 'Inserte otro numero: '))
print(f'Numeros Ingresados: {numeros}')


print('\n\n*** EJERCICIO 9.- Generar los primeros N números de la serie de Fibonacci.')

n = int(input( '¿cuantos numeros de la serie fibonacci quiere ver?: '))

a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=' - ')
    #calculamos el siguiente numero
    siguiente  = a + b
    #Se avanza en la serie
    a = b
    b = siguiente
    contador += 1


print('\n\n*** EJERCICIO 10.- Simular un cajero automático: '
      'pedir una cantidad inicial de saldo y permitir retirar dinero hasta que no haya suficiente..')

#Preestablecemos un saldo fijo
print(f'\nBienvenido a tu cajero automatico ')

saldo = 1100 #saldo inicial fijo

while saldo > 0:
    print(f'\nTu saldo actual es {saldo:.2f}')
    retiro = float(input( 'Ingresa la cantidad que deseas retirar: (0 para salir del sistema): '))

    if retiro == 0:
        print( 'Operacion cancelada, Gracias por usar nuestro cajero')
        break
    elif retiro > saldo:
        print(' Saldo insuficiente, Ingresa otro monto')
    else:
        saldo -= retiro
        print(f'f has retirado ${retiro:.2f}. saldo restante actual: ${saldo:.2f} ')
if saldo <= 0:
    print('\nSaldo agotado.fin de la operacion ')







































