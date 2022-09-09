import random
import time


puntaje =random.randint(0,10)
nombre =input("Ingresa tu nombre :")


def Historia(nombre,puntaje):
    countCorrectas = 0
    countIncorrectas = 0
    puntaje +=2
    print("\nMuy bien",nombre,"veo que tomaste la mejor desicion jaja")
    print("Ahora tienes",puntaje,"puntitos,es hora de demostrar lo que sabes!","\n")

    print("Pregunta 1:")
    print("¿Desde cuándo podemos copiar y pegar?","\n")

    print("a)1981")
    print("b)1986")
    print("c)1982")
    print("d)1984")

    respuesta1 =input("\nElije una respuesta:")

    while respuesta1 not in ("a", "b", "c", "d"):
     respuesta1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ","\n")

    if(respuesta1 == "a"):
        countCorrectas +=1
        puntaje +=30
        print("\nCorrecto",nombre,"!,Fue desde 1981","\n")
    else:
        countIncorrectas +=1
        #Relativo
        # puntaje -= 10
        print("\nIncorrecto",nombre,"!,La respuesta correcta es 1981, el ingeniero Larry Tesler desarrolló esta función que nos ahorra tantas horas de trabajo.","\n")


    time.sleep(10)
    ################################################################################

    print("Pregunta 2:")
    print("¿Recuerdas cuál fue el primer navegador de la historia?","\n")

    print("a)Netscape Navigator")
    print("b)Safari")
    print("c)World Wide Web")
    print("d)Internet Explorer")

    respuesta2 =input("\nElije una respuesta:")

    while respuesta2 not in ("a", "b", "c", "d"):
     respuesta2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ","\n")

    if(respuesta2 == "c"):
        countCorrectas +=1
        puntaje +=15
        print("\nCorrecto",nombre,"!,La WWW fue el primer navegador","\n")
    else:
        countIncorrectas +=1
        #Relativo
        # puntaje -= 10
        print("\nIncorrecto",nombre,"!,La World Wide Web fue el primer navegador","\n")


    ################################################################################


    print("Pregunta 3:")
    print("¿En qué año se desarrolló el lenguaje de programación C?","\n")
    print("a)1968")
    print("b)1970")
    print("c)1974")
    print("d)c")

    respuesta3 = input("Ingresa una respuesta:")

    while respuesta3 not in ("a", "b", "c", "d"):
     respuesta3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ","\n")

    if(respuesta1 == "d"):
        countCorrectas +=1
        puntaje +=30
        print("\nCorrecto",nombre,"!,Se desarrollo en 1972 por Dennis M. Ritchie","\n")
    else:
        countIncorrectas +=1
        #Relativo
        # puntaje -= 12
        print("\nIncorrecto",nombre,"!,La respuesta correcta es 1972. C fue creado en 1972 por Dennis M. Ritchie en los Laboratorios Bell","\n")


    ################################################################################

    
    if(countCorrectas>countIncorrectas):
        resultado = print("\nIncreible",nombre,"has ganado  esta trivia con",puntaje,"puntasos")
    else:
        resultado = print("\nLo siento",nombre,"has perdido la trivia :(") 

    


def Algoritmos(nombre,puntaje):
    countCorrectas = 0
    countIncorrectas = 0
    puntaje +=2
    print("\nMuy bien",nombre,"veo que tomaste la mejor desicion jaja")
    print("Ahora tienes",puntaje,"puntitos,es hora de demostrar lo que sabes!","\n")








##########################################   

print("\nHola", nombre,",te doy la bienvenida a esta trivia!")
print("No olvides que inicias con",puntaje,"puntos, los cuales aumentaran o", 
"disminuiran depende de la categoria que escojas :), Suerte!","\n")

print("Elije una categoria :","\n")

print("1) Historia")
print("2) Algoritmos")
print("3) Sintaxis","\n")

respuestaCat =input("Elije una categoria :")

while respuestaCat not in ("1", "2", "3"):
  respuestaCat = input("Debes responder 1,2 o 3. Ingresa nuevamente tu respuesta: ")

if(respuestaCat == "1"):
    print(Historia(nombre,puntaje))
elif(respuestaCat == "2"):
    print("Hola")