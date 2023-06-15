from ClaseFacultad import Facultad
class ManejaFacultades:
    def __init__(self):
        self.facultades = []

    def cargar_facultades(self, archivo):
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            i = 0
            while i < len(lineas):
                datos_facultad = lineas[i].strip().split(',')
                codigo_facultad = int(datos_facultad[0])
                nombre_facultad = datos_facultad[1]
                direccion_facultad = datos_facultad[2]
                ciudad_facultad = datos_facultad[3]
                provincia_facultad = datos_facultad[4]
                telefono_facultad = datos_facultad[5]

                facultad = Facultad(codigo_facultad, nombre_facultad, direccion_facultad,
                                    ciudad_facultad, provincia_facultad, telefono_facultad)

                i += 1
                while i < len(lineas) and lineas[i].startswith(str(codigo_facultad)):
                    datos_carrera = lineas[i].strip().split(',')
                    codigo_carrera = int(datos_carrera[1])
                    nombre_carrera = datos_carrera[2]
                    duracion_carrera = datos_carrera[4]
                    nivel_carrera = datos_carrera[5]
                    facultad.agregar_carrera(codigo_carrera, nombre_carrera, duracion_carrera, nivel_carrera)
                    i += 1

                self.facultades.append(facultad)

    def mostrar_carreras_facultad(self, codigo_facultad):
        for facultad in self.facultades:
            if facultad.codigo == codigo_facultad:
                print(f"Nombre de la Facultad: {facultad.nombre}")
                print("Carreras:")
                for carrera in facultad.obtener_carreras():
                    print(f"- Nombre: {carrera.nombre}")
                    print(f"  Duración: {carrera.duracion}")
                    print(f"  Nivel: {carrera.nivel}")
                return
        print("No se encontró la facultad con el código ingresado.")

    def mostrar_facultad_carrera(self, nombre_carrera):
        for facultad in self.facultades:
            for carrera in facultad.obtener_carreras():
                if carrera.nombre == nombre_carrera:
                    print(f"Código de la Facultad: {facultad.codigo}")
                    print(f"Nombre de la Facultad: {facultad.nombre}")
                    print(f"Localidad: {facultad.ciudad}")
                    return
        print("No se encontró la carrera ingresada.")
