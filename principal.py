from funciones import menu, ingresar_mascota, buscar_mascota, eliminar_mascota, listar_mascotas
import json, os
import numpy as np

matriz = np.empty((50, 8), dtype=object)

if os.path.exists('mascotas.json'):
    with open('mascotas.json', 'r') as file:
        json_mascotas = json.load(file)

    for i, mascota in enumerate(json_mascotas):
        matriz[i, 0] = mascota['nombre']
        matriz[i, 1] = mascota['codigo']
        matriz[i, 2] = mascota['edad']
        matriz[i, 3] = mascota['peso']
        matriz[i, 4] = mascota['raza']
        matriz[i, 5] = mascota['especie']
        matriz[i, 6] = mascota['medicamento']
        matriz[i, 7] = mascota['diagnostico']

while True:
    op = menu()

    match op:
        case 1:
            matriz=ingresar_mascota(matriz) 
            #captura y actualiza la matriz global
        case 2:
            print()
            codigo_input=input("Ingrese el codigo de la mascota que desea buscar ")
            buscar_mascota(codigo_input, matriz)
        case 3:
            print()
            codigo_input=input("Ingresa el codigo de la mascota que deseas eliminar ")
            matriz=eliminar_mascota(codigo_input, matriz)
        case 4:
            listar_mascotas(matriz)   
        case 5:
            print("Has elegido salir. Adiós!")
            break
        case _:
            print("Opción no valida")

diccionario_mascotas = []

for mascota in matriz:
    if None in mascota:
        continue
    
    mascotas_dict = {
    "nombre_completo": mascota[0],
    "codigo": mascota[1],
    "edad": mascota[2],
    "peso": mascota[3],
    "raza": mascota[4],
    "especie": mascota[5],
    "medicamento": mascota[6],
    "diagnostico": mascota[7]
    }
    diccionario_mascotas.append(mascotas_dict)                                

with open('mascotas.json', 'w') as file:
    json.dump(diccionario_mascotas, file, indent=4)

print("Datos de mascotas guardados en mascotas.json exitosamente.")