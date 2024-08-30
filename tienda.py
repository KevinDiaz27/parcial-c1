class Mary:
    def __init__(self) -> None:
        self.libreta = []
        self.inventario = []

    def anotar(self, precio):
        self.libreta.append(precio)

    def calcular_y_dar_cambio(self, dinero, necesita_cambio):
        total = 0
        for p in self.libreta:
            total += p

        print(f"Total a pagar: {total}")
        dinero -= total

        if dinero > 0 and necesita_cambio:
            print(f"*Le da {dinero}*")
        elif dinero == 0 and necesita_cambio:
            print("Salio cabal")
        elif not necesita_cambio and dinero > 0:
            print("Gracias por la propina!")
        else:
            print("Insuficiente dinero")

    def atender_proveedores(self):
        cantidad = int(input("Cantidad de productos: "))
        for c in range(1, cantidad):

            nombre = input(f"Nombre del producto {c}: ")
            precio_sugerido = float(input("Precio sugerido: "))

            self.inventario.append({
                "nombre": nombre,
                "precio_sugerido": precio_sugerido
            })


def main():
    mary = Mary()

    print("1 - Atender cliente")
    print("2 - Atender proveedor")

    opcion = int(input("> "))

    if opcion == 1:
        while 1:

            precio = float(input("Precio: "))

            mary.anotar(precio)

            if input("Desea agregar otro producto (y/n): ").lower() == "y":
                continue

            break
        
        d = float(input("Dinero: "))
        c = True if input("Necesita cambio (y/n): ").lower() == "y" else False
        mary.calcular_y_dar_cambio(d, c)
    else:
        mary.atender_proveedores()

if __name__ == '__main__':
    main()