import json
import numpy as np
global matriz

def menu():
    print("¿Qué opción desea realizar?")
    print("1.- Ingresar ficha de mascota")
    print("2.- Buscar mascota por codigo")
    print("3.- Eliminar mascota por codigo")
    print("4.- Listar mascotas")
    print("5.- Para salir y actualizar datos")
    op = int(input("Ingrese una opción válida (1/5): "))
    return op


def ingresar_mascota(matriz):
    while True:
        fila_vacia = None

        for i in range(matriz.shape[0]):
            if matriz[i][0] is None or matriz[i][0] == "":
                fila_vacia = i
                break

        if fila_vacia is None:
            print("No hay filas vacías para ingresar nuevas mascotas.")
            return matriz  # Retorna matriz sin cambios si no hay filas vacías
        
        print()
        nombre_completo = input("Ingrese el nombre completo de la mascota: ")
        codigo = input("Ingrese el codigo de la mascota: ")
        edad = input("Ingrese la edad de la mascota: ")
        peso = input("Ingrese el peso de la mascota: ")
        raza = input("Ingrese la raza de la mascota: ")
        especie = input("Ingrese la especie de la mascota: ")
        medicamento = input("Ingrese el medicamento recetado: ")
        diagnostico = input("Ingrese el diagnostico de la mascota: ")
        
        if nombre_completo == "" or codigo == "" or edad == "" or peso == "" or raza == "" or especie == "" or medicamento == "" or especie == "":
            print("Error: Todos los campos deben ser ingresados. No se permiten campos vacíos.")
            print("Por favor, vuelva a intentarlo.")
            continue  # Vuelve al inicio del bucle para pedir los datos nuevamente
        
        # Ingresar los datos del paciente en la fila vacía encontrada
        matriz[fila_vacia] = [nombre_completo, codigo, edad, peso, raza, especie, medicamento, diagnostico]
        print()
        print("Mascota ingresada con éxito en la fila", fila_vacia)

        respuesta = input("¿Desea ingresar otra mascota? (si/no): ")
        print()
        if respuesta.lower() != 'si':
            break

    return matriz  # Retorna la matriz global modificada


def buscar_mascota(codigo, matriz):
    encontrado=False
    for mascota in matriz:
        if mascota[1] == codigo:
            encontrado=True
            print()
            print("Datos del paciente:")
            print(f"Nombre mascota: {mascota[0]}")
            print(f"Codigo: {mascota[1]}")
            print(f"Edad: {mascota[2]}")
            print(f"Peso: {mascota[3]}")
            print(f"Raza: {mascota[4]}")
            print(f"Especie: {mascota[5]}")
            print(f"Medicamento: {mascota[6]}")
            print(f"Diagnostico: {mascota[7]}")
            print()

    if not encontrado:
        print(f"No se encontró ninguna mascota con el codigo {codigo}")
        print()

def eliminar_mascota(codigo, matriz):
    encontrado = False
    nombre_mascota = None

    for i in range(matriz.shape[0]):
        if matriz[i, 1] == codigo:
            encontrado = True
            nombre_mascota = matriz[i, 0]  # matriz[i, 0] es el campo del nombre en la matriz
            print(f"Eliminando mascota {nombre_mascota} con codigo {codigo}")
            matriz = np.delete(matriz, i, axis=0)
            print("Mascota eliminada correctamente.")
            print()
            break

    if not encontrado:
        print(f"No se encontro ninguna mascota con el codigo {codigo}")
        print()
    else:
        return matriz


def listar_mascotas(matriz):
    print()
    print("Listado de mascotas:")
    print()
    for mascota in matriz:
        if mascota[0] is not None and mascota[0] != "":
            print(f"{mascota[0]}, {mascota[1]}, {mascota[2]}, {mascota[3]}, {mascota[4]}, {mascota[5]}, {mascota[6]}, {mascota[7]}")
            print()
        else:
            break

   

