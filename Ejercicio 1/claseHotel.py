from claseHabitacion import Habitacion
class Hotel:
    __nombre :str
    __direccion :str
    __telefono :str
    __habitaciones : list
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__habitaciones = []
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f'Hotel {self.__nombre}, direccion: {self.__direccion}, telefono: {self.__telefono}'
    def agregarHabitacion(self, numero, piso, tipo, precio, disponible):
        self.__habitaciones.append(Habitacion(numero, piso, tipo, precio, disponible))
    def reservarHabitacion(self, num):
        i = 0
        long = len(self.__habitaciones)
        while i < long:
            if num == self.__habitaciones[i].getNumero():
                self.__habitaciones[i].reservar()
            i += 1
    def liberarHabitacion(self, num):
        i = 0
        long = len(self.__habitaciones)
        while i < long:
            if num == self.__habitaciones[i].getNumero():
                self.__habitaciones[i].liberar()
            i += 1
    def mostrartipo(self, tipoH):
        i = 0
        long = len(self.__habitaciones)
        while i < long:
            if self.__habitaciones[i].getTipo().lower() == tipoH.lower():
                print(f"tipo: {tipoH}, numero: {self.__habitaciones[i].getNumero()}, piso: {self.__habitaciones[i].getPiso()}")
            i += 1
    def libres(self):
        for piso in range(1, 4): 
            cant = 0
            i = 0
            while i < len(self.__habitaciones):
                if self.__habitaciones[i].getPiso() == piso and self.__habitaciones[i].getDisponible():
                    cant += 1
                i += 1
            if cant > 0:
                print(f"Piso {piso}: {cant} habitaciones libres")
    def detalles(self):
        for tipo in ['sencilla', 'doble', 'suite']:
            i = 0
            while i < len(self.__habitaciones):
                if self.__habitaciones[i].getTipo().lower() == tipo.lower():
                    print(f"Tipo: {tipo}   Numero: {self.__habitaciones[i].getNumero()}  piso: {self.__habitaciones[i].getPiso()},Precio: {self.__habitaciones[i].getPrecio()}  Disponibilidad: {self.__habitaciones[i].getDisponible()}")
                i += 1
