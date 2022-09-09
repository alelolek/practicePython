#Son utilizados para definir una coleccion que no tiene indice

letras = {'r','g','b'}

print(type(letras))
print(dir(letras))

#Validar existencia 
print('r' in letras)

#Agregar datos-aleatorio
letras.add('k')

#Remover elementos
letras.remove('g')

#Limpiar set
letras.clear()

#Eliminar set
del letras

print(letras)