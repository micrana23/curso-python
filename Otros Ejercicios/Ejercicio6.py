#Ejercico sobre el funcionamiento de una orquesta

class Instrumento:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def tocar(self):
        print(f"Tocando el instrumento {self.nombre}")

    def afinar(self):
        print(f"Afinando el instrumento {self.nombre}")


class Flauta(Instrumento):

    def __init__(self, nombre, tipo, modelo):
        super().__init__(nombre, tipo)
        self.modelo = modelo

    def tocar(self):
        super().tocar()
        print("Soplando")


class Guitarra(Instrumento):

    def __init__(self, nombre, tipo, numero_cuerdas):
        super().__init__(nombre, tipo)
        self.numero_cuerdas = numero_cuerdas


class GuitarraElectrica(Guitarra):

    def __init__(self, nombre, tipo, numero_cuerdas, potencia):
        super().__init__(nombre, tipo, numero_cuerdas)
        self.potencia = potencia

    def tocar(self):
        print("Tocando la guitarra eléctrica")


class Tambor(Instrumento):

    def __init__(self, nombre, tipo, tamano):
        super().__init__(nombre, tipo)
        self.tamano = tamano

    def aporrear(self):
        print(f"Aporreando tambor {self.nombre}")


class Orquesta:

    def __init__(self):
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def tocar_orquesta(self):

        for instrumento in self.instrumentos:

            if isinstance(instrumento, Tambor):
                instrumento.aporrear()
            else:
                instrumento.tocar()


# Crear instrumentos
flauta = Flauta("Flauta Travesera", "Viento", "Yamaha")
guitarra = Guitarra("Guitarra Clásica", "Cuerda", 6)
guitarra_electrica = GuitarraElectrica(
    "Stratocaster",
    "Cuerda",
    6,
    100
)
tambor = Tambor("Tambor Grande", "Percusión", "Grande")

# Crear orquesta
orquesta = Orquesta()

# Añadir instrumentos
orquesta.agregar_instrumento(flauta)
orquesta.agregar_instrumento(guitarra)
orquesta.agregar_instrumento(guitarra_electrica)
orquesta.agregar_instrumento(tambor)

# Tocar
orquesta.tocar_orquesta()