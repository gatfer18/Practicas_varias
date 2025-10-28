'''
SERIE DE EJERCICIOS PARA PRACTICAR LAS TUPLAS EN PYTHON
print( '\n\nEjercicio.- ')
'''

print( '\n\nEjercicio.-1 Crea una tupla con los días de la semana y muestra el tercer día.  ')

dias_semana = ( 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimache')
print(f'Le troisième jour de la semaine est: {dias_semana[2]}' )

print( '\n\nEjercicio.-2 Convierte una lista en tupla y muestra ambos tipos para comparar. ')

lista_A = [ 'Janvier',' Février', ' Mars','Avril ','Mai',' juin',' juin' ]
tupla1 = tuple(lista_A)
lista_A.append(' Juillet')
print( f'La lista A: {lista_A}')
print( f'La tupla A: {tupla1}')

print( '\n\nEjercicio.-3 Usa el método count() para contar cuántas veces aparece un valor en una tupla.')

print(f'Usando el metodo count:{tupla1}')
print(tupla1.count(' juin'))