class categoria: 
    def __init__(self, id, nombre): 
        self.id = id
        self.nombre = nombre
   
# creating list       
categrias = [] 
  
# appending instances to list 
categrias.append( categoria(1,'Historia') )
categrias.append( categoria(2,'Algoritmos') )
categrias.append( categoria(3,'Sintaxis') )



class pregunta: 
    def __init__(self, id, descripcion,respuesta,idCat): 
        self.id = id
        self.descripcion = descripcion
        self.respuesta = respuesta
        self.idCat = idCat

preguntas = [] 
  
# appending instances to list 
preguntas.append(pregunta(1,'¿Desde cuándo podemos copiar y pegar?','a',1) )
preguntas.append(pregunta(2,'¿Recuerdas cuál fue el primer navegador de la historia?','c',1) )
preguntas.append(pregunta(3,'En qué año se desarrolló el lenguaje de programación C?','d',1) )



class alternativa: 
    def __init__(self, id, descripcion,idPre): 
        self.id = id
        self.descripcion = descripcion
        self.idPre = idPre

alternativas = [] 
  
# appending instances to list 
alternativas.append(alternativa(1,'1981',1) )
alternativas.append(alternativa(2,'World Wide Web',2) )
alternativas.append(alternativa(3,'1972',3) )
      