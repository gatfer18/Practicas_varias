print( '*** Programa de descuento ****')

NO_PROC_DESCUENTO =12
cantidad_productos = int(input( 'Cuantos articulos has adquirido hoy?: '))
tiene_membresia = input( 'Eres Miembro o Socio: ')

es_elegible_descuento = (cantidad_productos >= NO_PROC_DESCUENTO and tiene_membresia.strip().lower() ==  'si')
print (f'Tienes acceso al descuento vip? ´{es_elegible_descuento} ')