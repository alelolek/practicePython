"""demo_list = [1,"hello",2.4,True,[1,2,3]]
listadenumeros = list((1,2,3,4,5))
print(type(listadenumeros))



#Imprime una lista desde el 1 hasta el 9
r = list(range(1, 10))
print(r)

#Ver todos los metodos que tiene list
print(dir(colores))

colores = ['azul','amarillo','rojo']

#cantidad de elementos en la lista
print(len(colores))

#una posicion especifica
print(colores[1])

#ver si un elemento esta en una lista 
print("azul" in colores)

#cambiar un elemneto 
colores [1] = "violeta"

#Agrega un elemento a la lista
colores.append('violeta')

#solo se pueden añadir mas de un elemento cuando 
# la lista la conviertes en una tupla
colores.append(('verde', 'celeste')) # se veria como tal

#Integra elementos
colores.extend(('verde' , 'celeste')) 
colores.extend(['negro','blanco'])

#colocar un elemento en un determinado lugar 
colores.insert(1,'rosado')

#insertar un elemnto al final 
colores.insert(len(colores),'morado')

#quita el ultimo elemento
colores.pop()

#remueve un valor especifivo 
colores.remove('amarillo')

#elimina rodo de la lsita 
colores.clear()

#ordenar una lista por orden alfaetco
colores.sort()

#invierte la lista 
colores.reverse()

#saberla posicion de un elemnto
print(colores.index('azul'))

#saber la cantidad de un mismo elemento
print(colores.count('rojo'))

print(colores)"""

"""
import random


lista = []
lista.append(12)
lista.append(1)
lista.append(13)
print(lista)

lista1 =[1,"pepe"]
lista1[0]= "juan"
print(lista1)


print(lista)
print(sum(lista))

print("cualquiera",random.choice(lista))
print(lista)
print(max(lista))
print(min(lista))

print("\nÍndice de 'juan':", lista1.index("juan"))
print(" cant elemento",len(lista))"""

"""lista = [10,20,30,40,50,60,70,80,90,100]

for numero in range (0,4):
    print(lista[numero])

for element in lista:
    print(element)"""


"""paises = ['Peru','Chile','Argentina','Ecuador']
capitales = ['Lima','Satiago de Chile','Buenos Aires','Quito']

for i in range (0,4):
    print("La capital de",paises[i],"es",capitales[i])"""

lista = [10,20,30,40,50,60,70,80,90,100]

for element in lista:
    if element > 30:
        print(element,"es mayor a 30!")
    else :
        print(element,"Es menor que 30!")
    