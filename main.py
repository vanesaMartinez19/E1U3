from ClaseManejadorFacultades import ManejaFacultades
import csv

def menu():
    print("===== MENÚ =====")
    print("1. Mostrar carreras de una facultad por código")
    print("2. Mostrar facultad y localidad de una carrera por nombre")
    print("0. Salir")
    print("================")
    opcion = input("Ingrese una opción: ")
    return opcion


if __name__ == '__main__':
    maneja_facultades = ManejaFacultades()
    maneja_facultades.cargar_facultades('Facultades.csv')

    while True:
        opcion = menu()
        if opcion == '0':
            break
        elif opcion == '1':
            codigo_facultad = int(input("Ingrese el código de la facultad: "))
            maneja_facultades.mostrar_carreras_facultad(codigo_facultad)
        elif opcion == '2':
            nombre_carrera = input("Ingrese el nombre de la carrera: ")
            maneja_facultades.mostrar_facultad_carrera(nombre_carrera)
        else:
            print("Opción inválida. Intente nuevamente.")



