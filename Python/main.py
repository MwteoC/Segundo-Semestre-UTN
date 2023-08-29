# Listas = Mateo, Maria Jose, Pablo, Joaquin, Emiliano

nombres = ['Mateo', 'Maria Jose', 'Pablo', 'Joaquin', 'Emiliano']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) # Solo muestra el indidce 0, 1 pero no el indice 2
# Ir del incio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0, 1 y 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor

nombres[2] = 'Sergio'
nombres[4] = 'Emi'
print(nombres)

# Iterar una lista
for nombre in nombres: # Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
print(nombres)

# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',) # Una tupla necesita aunque sea un elemento la coma
# De lo contrario seria un tipo str cadena

# Recorremos los elementos de la tupla 
for cocinar in cocina: # Print usta usando \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end= para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)

print('\n', cocina)

# del cocina esto es para eliminar la tupla