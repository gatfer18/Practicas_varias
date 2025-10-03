'''

Practicas de Entrada de datos

'''

#(1.-EJERCICIO) Pide al usuario su nombre e imprime un saludo personalizado.

nombre = input(str('Introduce tu Nombre: '))
apellido = input(str( 'Introduce tu Apellido: '))

print(f' Tu nombre es: {nombre} y tu apellido  {apellido} ')

#(2.-EJERCICIO) Edad futura: Pide la edad del usuario y muestra cuántos años tendrá dentro de 10 años.

edad = int(input( 'Introduce tu edad: ' ))
print( f'Tu edad es : {edad}, y en 10 años tendras {edad + 10}')

#(3.-EJERCICIO) Suma de dos números: Pide dos números al usuario, súmalos y muestra el resultado.

x = int(input('Introduce un numero entero: '))
y = int(input('Introduce un numero entero: '  ))
resultado = x + y
print(f'la suma de los numeros proporcionados es: {resultado}')

#(4.-EJERCICIO)Promedio de tres notas: Pide tres notas al usuario y calcula su promedio.

nota_A = float(input( 'Introduce la primera nota de las tres asignatura: '))
nota_B = float(input( 'Introduce la segunda nota de las tres asignatura: '))
nota_C = float(input( 'Introduce la tercera nota de las tres asignatura: '))
promedio = (nota_A + nota_B + nota_C) / 3
print(f'Las notas que has introdudo son: {nota_A}; {nota_B}; {nota_C} y el promedio acumulado es: {promedio:.2f}')

#(5.-EJERCICIO) Área de un triángulo: Pide la base y la altura de un triángulo y calcula el área.

area1 = float(input( 'Introduce la base del triangulo: '))
area2 = float(input( 'Introduce la altura del triangulo: '))
print(f' el area del triangulo es: {area1 * area2}')

#(6.-EJERCICIO) Conversión de metros a centímetros: Pide una cantidad en metros y conviértela a centímetros.

metros = int(input(f'Introduce una cantidad en metros:  '))
convercion =  metros * 100
print ( f'la cantidad de {metros} son {convercion} centimetros ')

#(7.-EJERCICIO) Concatenación de nombre completo: Pide al usuario su nombre y su apellido y muéstralos como nombre completo.

nombre = str(input( 'Introduce tu nombre: '))
apellidos = str(input( 'Introduce tu apellido: '))
print (f'Tu nombre completo es : {nombre + ' ' + apellidos} ')

#(8.-EJERCICIO) Residuo de una división:

x = int(input('Ingresa una monto: '))
y = int(input('Ingresa otro monto: '))

print(f'El residuo de los montos proporcionados {x} y {y} es: {x % y} ')
