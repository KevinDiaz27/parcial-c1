#Diego Samuel Reyes Moreno
#Kevin Alexander Diaz Parada
habitaciones = {
    'Simple': 50,
    'Doble': 80,
    'Suite': 120
}

servicios_extra = {
    'Piscina': 20,
    'Cancha de Golf': 50
}

def mostrar_opciones(opciones, tipo):
    print(f"\nOpciones de {tipo}:")
    for opcion, precio in opciones.items():
        print(f"{opcion}: ${precio}")

def solicitar_datos_cliente():
    """Solicita los datos del cliente."""
    nombre = input("Ingrese su nombre: ")
    noches = int(input("Ingrese el número de noches que permanecerá: "))
    return nombre, noches

def solicitar_servicios_extra():
    """Solicita los servicios extra que el cliente desea agregar."""
    mostrar_opciones(servicios_extra, 'servicios extra')
    servicios = input("Ingrese los servicios extra que desea (separados por coma): ").split(',')
    servicios = [servicio.strip() for servicio in servicios]
    return servicios

def calcular_total(habitacion, noches, servicios):
    """Calcula el costo total basado en la habitación, noches y servicios extra."""
    costo_habitacion = habitaciones[habitacion] * noches
    costo_servicios = sum(servicios_extra.get(servicio, 0) for servicio in servicios)
    return costo_habitacion + costo_servicios

def generar_factura(nombre, habitacion, noches, servicios, total):
    """Genera y muestra la factura final."""
    print("\n--- FACTURA ---")
    print(f"Nombre: {nombre}")
    print(f"Habitatión: {habitacion}")
    print(f"Número de noches: {noches}")
    print("Servicios extra:")
    for servicio in servicios:
        if servicio in servicios_extra:
            print(f"  - {servicio}: ${servicios_extra[servicio]}")
    print(f"Total a pagar: ${total}")

def main():
    """Función principal para ejecutar el programa."""
    print("Bienvenido al sistema de reservas del hotel de playa.")
    
    mostrar_opciones(habitaciones, 'habitaciones')
    habitacion = input("Seleccione la habitación deseada: ")
    
    if habitacion not in habitaciones:
        print("La habitación seleccionada no es válida.")
        return
    
    nombre, noches = solicitar_datos_cliente()
    servicios = solicitar_servicios_extra()
    
    total = calcular_total(habitacion, noches, servicios)
    generar_factura(nombre, habitacion, noches, servicios, total)

if __name__ == "__main__":
    main()
