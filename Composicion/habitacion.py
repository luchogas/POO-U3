class Habitacion:
    __numero : int
    __piso : int
    __tipo : str
    __precio : float
    __disponibilidad : bool
    def __init__(self, numero, piso, tipo, precio, disponibilidad):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__disponibilidad = disponibilidad
    def getNumero(self):
        return self.__numero
    def getPiso(self):
        return self.__piso
    def getTipo(self):
        return self.__tipo
    def getPrecio(self):
        return self.__precio
    def getDisponibilidad(self):
        return self.__disponibilidad
    def mostrar(self):
        print(f"Numero: {self.__numero}, Piso: {self.__piso}, Tipo: {self.__tipo}, Precio: {self.__precio}, Disponibilidad: {self.__disponibilidad}")

    def reservarr(self):
        if self.__disponibilidad:
            self.__disponibilidad = False
            print(f"Habitacion {self.__numero} reservada.")
        else:
            print(f"Habitacion {self.__numero} no disponible para reserva.")

    def liberarr(self):
        if not self.__disponibilidad:
            self.__disponibilidad = True
            print(f"Habitacion {self.__numero} liberada.")
        else:
            print(f"Habitacion {self.__numero} ya estaba liberada.")
