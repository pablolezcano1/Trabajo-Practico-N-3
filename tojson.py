# %%
# Read and Write data to JSON
import json

def guardar_lista_diccionarios_como_json(lista_diccionarios, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(lista_diccionarios, archivo)

def cargar_lista_diccionarios_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lista_diccionarios = json.load(archivo)
    return lista_diccionarios

datos = [
    {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'},
    {'nombre': 'María', 'edad': 30, 'ciudad': 'Barcelona'},
    {'nombre': 'Pedro', 'edad': 35, 'ciudad': 'Sevilla'}
]

nombre_archivo = 'datos.json'

guardar_lista_diccionarios_como_json(datos, nombre_archivo)

datos_cargados = cargar_lista_diccionarios_desde_json(nombre_archivo)

for diccionario in datos_cargados:
    print(diccionario)

# %%
