from habitacion import Habitacion
class Hotel:
    __nombre : str
    __direccion : str
    __telefono : int
    __habitaciones : list
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__habitaciones = []
    def agregarHabitacion(self, numero, tipo, piso, precio, disponibilidad):
        if tipo == '':
            raise ValueError("El tipo de habitacion no puede estar vacio")
        self.__habitaciones.append(Habitacion(numero, piso, tipo, precio, disponibilidad))
    
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def mostrar(self):
        print(f"{self.__nombre}- {self.__direccion}- {self.__telefono}")
        for habitacion in self.__habitaciones:
            habitacion.mostrar()

    def reservar(self, numero):
        i = 0
        long = len(self.__habitaciones)
        band = False
        while i < long and not band:
            if self.__habitaciones[i].getNumero() == numero:
                band = True
            i += 1
        if band:
            self.__habitaciones[i].reservarr()
        else:
            print("Habitacion no encontrada")
            
    def liberar(self, numero):
        i = 0
        long = len(self.__habitaciones)
        band = False
        while i < long and not band:
            if self.__habitaciones[i].getNumero() == numero:
                band = True
            i += 1
        if band:
            self.__habitaciones[i].liberarr()
        else:
            print("Habitacion no encontrada")