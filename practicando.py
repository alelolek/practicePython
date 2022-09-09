"""
#Ejercicio1
palabra = input("Ingresa la palabra :")
veces = int(input("Ingresa la cantidad de repeticiones :"))


#contador
x=0


while x < veces:
 print(palabra)
 x = x+1"""

"""##Ejercicio2 
x = 0

while x <= 10: 
 if(x==3):
  print("Boom")
 else: 
    print(x)
 x = x + 1
"""

"""#Ejercicio 3
numero = int(input("Ingresa el numero de pisos del triagulo :"))
simbolo = '+'
print(simbolo)
for i in range(numero - 1):
   simbolo = simbolo + '+'
   print(simbolo)"""



"""Promedio
numero1 = int(input("Ingresa el primer numero :"))
numero2 = int(input("Ingresa el segundo numero :"))

op = float((numero1 +numero2)/2)
print("El promedio es:",op)"""

"""Potencia
numero1 = int(input("Ingresa un numero :"))
numero2 = int(input("Ingresa la potencia :"))

op = int(numero1**numero2)
print(numero1,"elevado a ",numero2,"es igual a :",op)"""


"""numero1 = int(input("Ingresa un numero :"))

op = float(numero1**(0.5))
print("LA raiz cuadrada de",numero1,"es :",op)"""


"""numero1 = int(input("Ingresa un numero :"))
numero2 = int(input("Ingresa la potencia :"))

op = int(((numero1**2)+(numero2**2))**(0.5))
print("Resultado :",op)"""

"""
#Colores en constantes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


#Asi se imprime
print("\033[34m Este texto es azul \033[39m")
print(GREEN+"Este texto será verde"+RESET)"""


"""
for i in range (5,101,5):
   print(i)
"""
"""veces = int(input("Ingresa la veces :"))
palabra = "Hola"
for veces in range (0,veces,1):
   print(palabra) """


"""for i in range (10,-1,-1):
   print(i)"""

"""veces = int(input("Ingresa la veces :"))
simbolo = "+"

#1 forma
for i in range (0,veces,1):
   print(simbolo)
   simbolo = simbolo + "+"

#2 forma ???
for i in range (0,veces + 1):
   for j in range (0,i):
      print("+",end=" ")
   print(" ")  """ 
 

 #Ejercicios del reto de la sesion 4

"""edad = int(input("Ingresa una edad :"))

for i in range(1,edad + 1,1):
   print(i,end=" ")"""

"""num = int(input("Ingresa un numero :"))
for i in range(1,num+1,2):
   print(i)"""


"""#Factorial de un numero 
num = int(input("Ingresa un numero :"))
for i in range (1,num,1):
   num = num*i
print(num)"""


"""palabra = "hola mundo"
for i in palabra:
   print(i)"""

"""lista = ['Hola','hi','hello','bye']
for i in lista:
   print(i)"""


#Retos sesion 5

##1
"""lista = []
for i in range(0,5):
 palabra = input("Ingresa una palabra :")
 lista.append(palabra)

for i in lista:
   print(i)"""

##2
"""palabra = input("Ingresa una palabra :")
vocales = ['a','e','i','o','u']


for i in range(0,5):
  if(palabra[0] == vocales[i]):
    print("Empieza con vocal")
    palabra = input("Ingresa una palabra :")
else:
    print("Empieza con una consonante")"""


##3
##con paquetw
"""from collections import Counter

letra = input("Ingrese una letra :")
frase = input("Ingrese una letra :")

count = Counter(frase)
print(count[letra])"""

###############
#Reto sesion 6

#1
"""numero = int(input("Ingresa un numero del 1 al 12:"))

while numero not in (1,2,3,4,5,6,7,8,9,10,11,12):
   numero = int(input("Ingresa un numero del 1 al 12:"))
for i in range(1,13):
   print(numero*i)"""

a = int(input("Ingrese el primer numero: "))
"""for i in range(1,13,1):
      print(a*i)"""

#2
"""veces = int(input("Ingresa un numero :"))
for i in range(1,veces+1):
   print((i*2)-1)"""
   
#3
"""numero = int(input("Escribe un numero par : "))

while (numero%2==0):
   numero = int(input())
   """
while(True):
    a = int(input("Ingrese numero: "))
    if a%2!=0:
      break

#4