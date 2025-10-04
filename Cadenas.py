'''
Ejercicios de repaso para  el manejo de cadenas
'''
#(1-EJERCICIO) Longitud de una cadena:
# Declara una variable con tu nombre completo y muestra cuántos caracteres tiene.

nombreCom =  'Fernando Jose Vasquez'
largo_cadena = len(nombreCom)
print( f' Mi nombre completo tiene en total: {largo_cadena} caracteres ')

#(2-EJERCICIO) Mayúsculas y minúsculas:
# Declara una cadena y muestra la misma en mayúsculas y minúsculas

Cadena =  'Python es Genial'
print( Cadena.lower() )
print( Cadena.upper() )

#(3-EJERCICIO) Primer y último carácter:
# Declara una cadena y muestra en pantalla el primer y el último carácter de esa cadena.

cdna = "Venecia"
print( cdna [0] )
print( cdna [-1] )

#(4-EJERCICIO) Subcadena:
# Declara una cadena y muestra solo los primeros 5 caracteres

cdna  = "Asturias Gijon"
sub_cadna = cdna[0:5]
print( f'mostrando la subcadena de la cadena original {sub_cadna} ' )

#(5-EJERCICIO)Concatenacion:
# Declara dos cadenas, tu nombre y tu apellido, y únelos en una sola cadena con un espacio en medio.

nombre = "Antonio"
apellido = "Vasquez"
conk =  nombre + ' ' + apellido
print(  f'Concatenacion basica:{conk} ' )

#UTILIZANDO EL METODO JOIN

concatenacion =  ''.join([nombre, ' ', apellido])
print( f'Concatenacion con metodo JOIN  "Mi Nombre completo es": {concatenacion}' )

#(6-EJERCICIO) Repetición de cadenas:
#Declara una cadena corta y repítela 5 veces en una sola salida.

frase =  'timoteo'
Veces = 5
resultado = frase * Veces
print( f'Resultado de la repeticion de la cadena : {resultado} ' )

#(7-EJERCICIO)Reemplazo de caracteres:
#Declara una cadena y reemplaza todas las letras "a" por "o".

kdna = "alvaran"
nueva_kdna = kdna.replace("a","o")
print( f'Esta es la cadena sin reemplazar : {kdna} ' )
print(f'Esta es la cadena con los valores de A reemplazados: {nueva_kdna} ' )

#(8-EJERCICIO) Buscar en cadena: Declara una cadena y verifica si contiene la palabra "python".

lenguaje = 'El lenguaje mas versatil y sencillo es python'
palabra = "python"

if palabra in lenguaje:
    print( f'Se encontro la palabra : {palabra} ' )
else:
    print( f'La palabra no se encuentra  {palabra} ' )

#(9-EJERCICIO) Eliminar espacios:
#Declara una cadena con espacios al inicio y al final, y muestra la misma cadena sin esos espacios.

spacios =  '  El espacio es infinnito y se encuentra en esta frase   '
limpieza = spacios.strip()
print( f' Esta es la cadena original: {spacios} ' )
print(f' Esta es la cadena con los espacios eliminados: {limpieza} ' )

#(9-EJERCICIO) Invertir una cadena:
#Declara una cadena y muéstrala invertida (ejemplo: "hola" → "aloh").

nrmal = 'Lugo'
invercion = nrmal[::-1]
print( f' Esta es la cadena original: {nrmal} ' )
print(f' Esta es la cadena invertida: {invercion} ' )






















