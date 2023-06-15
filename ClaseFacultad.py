class Facultad:
    def __init__(self, codigo, nombre, direccion, ciudad, provincia, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.provincia = provincia
        self.telefono = telefono
        self.carreras = []

    def agregar_carrera(self, codigo, nombre, duracion, nivel):
        carrera = Carrera(codigo, nombre, duracion, nivel)
        self.carreras.append(carrera)

    def obtener_carreras(self):
        return self.carreras
