'''

EJERCICIOS PARA PRACTICAR LAS LISTAS EN PYTHON
print('\n\nEJERCICIO.- ' )
'''


print('\nEJERCICIO.-1 Crea una lista con 5 números y muestra el primer y último elemento..' )

lista_A = [12, 14,17,19,22]

print(f'Lista {lista_A} ')
primer_elemento = lista_A[0]
print(f'El Primer elemento es: {primer_elemento}')

ultimo_elemento =lista_A [-1]
print(f'El ultimo elementode la lista es: {ultimo_elemento} ')

print('\n\nEJERCICIO.- 2 Agrega un nuevo número a la lista anterior y muéstrala actualizada.')

lista_A.append(1)
lista_A.append(524)
lista_A.append(156)
print(f'lista actualizada{lista_A}')

print('\n\nEJERCICIO.- 3 Elimina el segundo elemento de la lista y muestra el resultado. ' )

lista_A.pop(2)
print(f'Lista despues de eliminar 2do Elemento: {lista_A}')


print('\n\nEJERCICIO.-4 Calcula la suma y el promedio de los elementos de una lista de números.')

suma_total = sum(lista_A)
cantidad_elementos =len(lista_A)
if cantidad_elementos > 0:
    prom = suma_total /cantidad_elementos
else:
    prom = 0

print(f'La lista es: {lista_A} ')
print(f'La suma total de los elementos es: {suma_total}')
print(f'El Promedio es: {prom}')

print('\n\nEJERCICIO.-5 Recorre una lista con un for y muestra cada elemento junto con su índice.')

#para iterar la lista mostrando su indice hay que utilizar la funcion enumerate

frutas =[' Fresa', ' Mango', 'Pera',  'Manzana',  'Melon']

print(f'lista sin iterar:{frutas}')
for indice, fruta in enumerate(frutas):

    print(f'El Indice {indice},es: {fruta}')



print('\n\nEJERCICIO.-6 Verifica si un número ingresado por el usuario está dentro de la lista' )


while True:
    usu = int(input( 'Ingresa un numero: '))

    if usu in lista_A:
        print( f'EL numero ingresado esta en la lista: {lista_A}' )
        print( 'Saliendo del sistema.....')
        break

    else:
        print('Vuelve a intentarlo: Ingresa un numero: ' )

print('\n\nEJERCICIO.- 7 Ordena una lista de números de menor a mayor ' )


lista_original = lista_A[:]
print(f'Lista sin ordenar: {lista_original} ')
lista_ordenado = sorted(lista_A)
print(f'Lista  ordenada : {lista_ordenado} ')


print('\n\nEJERCICIO.- 8  Crea una lista vacía y permite al usuario ingresar 5 nombres. Luego muéstralos todos. ' )

nombres = []
for i in range(5):
    nombre = str(input( f'Ingresa un nombre: {i + 1 }:  '))
    nombres.append(nombre)

print('\nLos nombres que has ingresado son: ')
for n in nombres:
    print(n)

print('\n\nEJERCICIO.- 9 Usa una lista por comprensión para generar los cuadrados del 1 al 10 ')


cuadrados = [i ** 2 for i in range(1,11)]
print(cuadrados)

print('\n\nEJERCICIO.- 10 Combina dos listas de nombres y muestra la lista final. ')

lista1 = [ 'Maria', ' Pedro', ' Raul']
lista2 = [ 'Maritza', ' Peter', ' Jopse']

lista_final = lista1 + lista2
print(f'Lista Uno: {lista1} ')
print(f'Lista Dos: {lista2} ')
print(f'Lista Final: {lista_final} ')




