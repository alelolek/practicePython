class Categoria: 
    def __init__(self, id, nombre): 
        self.id = id
        self.nombre = nombre
   
# creating list       
categorias = [] 
  
# appending instances to list 
categorias.append( Categoria(1,'Historia') )
categorias.append( Categoria(2,'Algoritmos') )
categorias.append( Categoria(3,'Sintaxis') )

class Pregunta: 
    def __init__(self, id, descripcion,respuesta,idCat): 
        self.id = id
        self.descripcion = descripcion
        self.respuesta = respuesta
        self.idCat = idCat

preguntas = [] 
  
# appending instances to list 
preguntas.append(Pregunta(1,'1) ¿Desde cuándo podemos copiar y pegar?','a',1) )
preguntas.append(Pregunta(2,'2) ¿Recuerdas cuál fue el primer navegador de la historia?','c',1) )
preguntas.append(Pregunta(3,'3) En qué año se desarrolló el lenguaje de programación C?','d',1) )

preguntas.append(Pregunta(4,'1) ¿Pregunta 1 cat 2?','a',2) )
preguntas.append(Pregunta(5,'2) ¿Pregunta 2 cat 2?','c',2) )
preguntas.append(Pregunta(6,'3) Pregunta 3 cat 2?','d',2) )

preguntas.append(Pregunta(7,'1) ¿Pregunta 1 cat 3?','a',3) )
preguntas.append(Pregunta(8,'2) ¿Pregunta 1 cat 2?','c',3) )
preguntas.append(Pregunta(9,'3) Pregunta 1 cat 2?','d',3) )

class Alternativa: 
    def __init__(self, id, descripcion,idPre): 
        self.id = id
        self.descripcion = descripcion
        self.idPre = idPre

alternativas = [] 
  
# appending instances to list 
alternativas.append(Alternativa(1,'a) 1981',1) )
alternativas.append(Alternativa(2,'b) 1986',1) )
alternativas.append(Alternativa(3,'c) 1982',1) )
alternativas.append(Alternativa(4,'d) 1984',1) )


alternativas.append(Alternativa(5,'a) Netscape Navigator',2) )
alternativas.append(Alternativa(6,'b) Safari',2) )
alternativas.append(Alternativa(7,'c) World Wide Web',2) )
alternativas.append(Alternativa(8,'d) Internet Explorer',2) )


alternativas.append(Alternativa(9,'a) 1968',3) )
alternativas.append(Alternativa(10,'b) 1970',3) )
alternativas.append(Alternativa(11,'c) 1974',3) )
alternativas.append(Alternativa(12,'d) 1972',3) )

def obtenerCategorias():
    return categorias

def obtenerPreguntasPorCategoria(categoriaId):
    return list(filter(lambda x: (x.idCat == categoriaId), preguntas))

def obtenerAlternativasPorPreguntas(preguntaId):
    return list(filter(lambda x: (x.idPre == preguntaId), alternativas))

import random

def obtenerAlternativaDeBot():
    alternativasDeBot = ['a','b','c','d']
    respuestaRandom = random.randint(0,3)
    return alternativasDeBot[respuestaRandom]

import time

def main():
    puntaje = 0
    puntajeBot = 0
    listaCategorias = obtenerCategorias()
    for categoria in listaCategorias:
        print(categoria.id,categoria.nombre)
    respuestaCategoria = int(input('Ingresa una categoria :'))
    listaPreguntas = obtenerPreguntasPorCategoria(respuestaCategoria)
    for pregunta in listaPreguntas:
        print(pregunta.descripcion)
        listaAlternativas = obtenerAlternativasPorPreguntas(pregunta.id)
        for alternativa in listaAlternativas:
            print(alternativa.descripcion)
        respuestaAlternativa = input('Ingresa una alternativa :')
        if respuestaAlternativa == pregunta.respuesta:
            print('Respuesta correcta')
            puntaje += 1
        else:
            puntaje -= 1
            print('Respuesta incorrecta')
        respuestaDeBot = obtenerAlternativaDeBot()
        if respuestaDeBot == pregunta.respuesta:
            puntajeBot += 1
        else:
            puntajeBot -= 1
        time.sleep(1)
    print(puntaje,puntajeBot)

if __name__ == "__main__":
    main()