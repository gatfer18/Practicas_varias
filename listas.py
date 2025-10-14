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

lista_A.append(55)
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


























