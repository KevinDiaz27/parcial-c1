class Asistencia:
    """
    Objeto asistencia
    """
    def __init__(self, fecha, estado, razon=None) -> None:
        self.fecha = fecha
        self.estado = estado
        self.razon = razon

class Estudiante:
    """
    Estudiante. El estudiante
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = []

    def registrar_asistencia(self, fecha, estado, razon_permiso=None):
        self.asistencias.append(Asistencia(fecha, estado, razon_permiso))

    def mostrar_asistencias(self):
        print(f"Asistencias de {self.nombre}:")
        for asistencia in self.asistencias:
            if asistencia.razon == 'Permiso':
                print(f"Fecha: {asistencia.fecha}, Estado: {asistencia.estado}, Razón: {asistencia.razon_permiso}")
            else:
                print(f"Fecha: {asistencia.fecha}, Estado: {asistencia.estado}")

class Docente:
    """
    Docente se encarga de anotar las asistencias
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = {}

    def agregar_estudiante(self, estudiante):
        self.estudiantes[estudiante.nombre] = estudiante

    def registrar_asistencia_estudiante(self, nombre_estudiante, fecha, estado, razon_permiso=None):
        if nombre_estudiante in self.estudiantes:
            self.estudiantes[nombre_estudiante].registrar_asistencia(fecha, estado, razon_permiso)
        else:
            print(f"Estudiante no encontrado: {nombre_estudiante}")

    def mostrar_asistencias_estudiantes(self):
        for estudiante in self.estudiantes.values():
            estudiante.mostrar_asistencias()

class Director:
    """ Director. Se encarga de revisar las asistencias"""
    def __init__(self, nombre):
        self.nombre = nombre

    def revisar_asistencias(self, docente):
        print(f"Revisando asistencias de los estudiantes registrados por {docente.nombre}:")
        docente.mostrar_asistencias_estudiantes()

# Tenemos un director y un docente
docente = Docente("Profesor Gómez")
director = Director("Director Martínez")
fecha = "2024-08-30"

# Le pedimos los datos de asistencias del estudiante
while True:
    nombre = input("Nombre del estudiante: ")
    estado = "Asistio" if input("Asistio a clases (y/n): ").lower() == "y" else "No asistio"
    tiene_permiso = input("Tiene permiso (y/n): ")
    razon = None

    if tiene_permiso.lower() == "y":
        estado = "Permiso"
    
    docente.agregar_estudiante(Estudiante(nombre))
    
    docente.registrar_asistencia_estudiante(nombre, fecha, estado, razon)

    if input("Otra asistencia? (y/n): ").lower() == "y":
        continue

    break


# Mostrar asistencias
docente.mostrar_asistencias_estudiantes()

# Director revisa asistencias
director.revisar_asistencias(docente)