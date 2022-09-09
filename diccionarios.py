producto = {
    "nombre" : "libro",
    "cantidad" : 3,
    "precio" : 18.2 
}

print(type(producto))

#Metodos de diccionario
print(dir(producto))

#Imprimir solo las claves
print(producto.keys())

#Imprimir los items
print(producto.items())

#Eliminar diccionario
del producto

#Eliminar los datos internos 
producto.clear()


productos = [
    {"name" : "Tv", "precio" : 3000},
    {"name" : "Laptop", "precio" : 3400}

]

print(type(productos))