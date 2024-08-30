from datetime import datetime

class Empleado:
    def __init__(self, nombre, anio_ingreso):
        self.nombre = nombre
        self.anio_ingreso = anio_ingreso

    def calcular_antiguedad(self):
        anio_actual = datetime.now().year
        return anio_actual - self.anio_ingreso

    def calcular_pago(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def calcular_bono_antiguedad(self):
        if self.calcular_antiguedad() > 5:
            return 100  # Valor del bono por antigüedad
        return 0

class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anio_ingreso, salario_base, comisiones):
        super().__init__(nombre, anio_ingreso)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        pago = self.salario_base + self.comisiones + self.calcular_bono_antiguedad()
        return pago

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anio_ingreso, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, anio_ingreso)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self):
        pago = self.horas_trabajadas * self.pago_por_hora + self.calcular_bono_antiguedad()
        return pago

# Ejemplo de uso
empleado_fijo = EmpleadoPlazaFija("Ana García", 2015, 1200, 200)
empleado_horas = EmpleadoPorHoras("Carlos Pérez", 2018, 80, 15)

print(f"Pago total para {empleado_fijo.nombre}: ${empleado_fijo.calcular_pago()}")
print(f"Pago total para {empleado_horas.nombre}: ${empleado_horas.calcular_pago()}")

while True:

    nombre = input("Nombre del empleado: ")
    anio_ingr = input("Año de ingreso: ")
    sal = float(input("Salario base: "))
    com = float(input("Comisiones: "))

    empleado = None

    fijo = input("Es empleado fijo (y/n): ")
    if fijo == "y":
        empleado = EmpleadoPlazaFija(nombre, anio_ingr, sal, com)
    else:
        empleado = EmpleadoPorHoras(nombre, anio_ingr, sal, com)
    
    if input("Desea agregar otro empleado (y/n): ").lower() == "y":
        continue

    break