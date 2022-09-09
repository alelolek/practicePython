miStr = "hello world"

print(miStr.upper()) #HELLO WORLD
print(miStr.lower()) #hello world
print(miStr.swapcase()) #HELLO WORLD 
print(miStr.capitalize()) #Hello world
print(miStr.replace("hello","bye")) # bye world
print(miStr.count('l'))  #3
print(miStr.startswith('hola')) #False
print(miStr.endswith('world')) #True
print(miStr.split()) #['hello', 'world']
print(miStr.find('h')) #0
print(len(miStr)) #11
print(miStr[4])  #o

#Imprimir un String concatenado 
print("My name is " + miStr)
print(f"My name is {miStr}")
print("My name is  {}".format(miStr))
