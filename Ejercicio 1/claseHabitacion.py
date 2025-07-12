class Habitacion:
    __numero: int
    __piso: int
    __tipo: str
    __precio: float
    __disponible: bool
    def __init__(self, numero, piso, tipo, precio, disponible):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__disponible = disponible
    def getNumero(self):
        return self.__numero
    def getPiso(self):
        return self.__piso
    def getTipo(self):
        return self.__tipo
    def getPrecio(self):
        return self.__precio
    def getDisponible(self):
        return self.__disponible
    def mostrar(self):
        estado = "Disponible" if self.__disponible else "Reservada"
        return f"Numero: {self.__numero}, Piso: {self.__piso}, Tipo: {self.__tipo}, Precio: {self.__precio}, Estado: {estado}"
    def reservar(self):
       if self.__disponible == True:
           self.__disponible = False
           print("La habitación ha sido reservada.")
       else:
              print("La habitación ya está reservada.")
    def liberar(self):
        if self.__disponible == False:
            self.__disponible = True
            print("La habitación ha sido liberada.")
        else:
            print("La habitación ya está libre.")
            
