from claseHotel import Hotel
from claseHabitacion import Habitacion
import csv
class GestorHotel:
    __listaHoteles : list
    def __init__(self):
        self.__listaHoteles = []
    def agregarHotel(self, hotel):
        if isinstance(hotel, Hotel):
            self.__listaHoteles.append(hotel)
        else:
            raise TypeError("El objeto no es una instancia de Hotel")
    def cargar(self):
        archivo = open("C:\\Users\\usuario\\Desktop\\Luciano-LCC\\2ºaño\\POO\\U3\\borrador ej1\\Hoteles.csv", encoding="utf-8")
        reader = csv.reader(archivo, delimiter=';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                hotel = Hotel(fila[0], fila[1], fila[2]) 
                self.agregarHotel(hotel)
                i += 1
            elif len(fila) == 5:
                numero = int(fila[0])
                piso = int(fila[1])
                tipo = fila[2]
                precio = float(fila[3])
                disponible = fila[4] == 'True'
                self.__listaHoteles[i].agregarHabitacion(numero, piso, tipo, precio, disponible)
        archivo.close()
    def mostrarHoteles(self):
        for hotel in self.__listaHoteles:
            print(hotel)
            for habitacion in hotel.getHabitaciones():
                print(habitacion)
                
    def reservarHabitacion(self, num):
        nombre = input("ingrese el nombre del hotel: ")
        long = len(self.__listaHoteles)
        i = 0
        while i < long:
            if self.__listaHoteles[i].getNombre().lower() == nombre.lower():
                self.__listaHoteles[i].reservarHabitacion(num)
            i += 1
    def liberarHabitacion(self, num):
        nombre = input("ingrese el nombre del hotel: ")
        long = len(self.__listaHoteles)
        i = 0
        while i < long:
            if self.__listaHoteles[i].getNombre().lower() == nombre.lower():
                self.__listaHoteles[i].liberarHabitacion(num)
            i += 1
    def mostrarPorTipo(self, tipoH):
        i = 0
        long = len(self.__listaHoteles)
        nom = input("Ingrese el nombre del hotel: ")
        while i < long:
            if self.__listaHoteles[i].getNombre().lower() == nom.lower():
                self.__listaHoteles[i].mostrartipo(tipoH)
            i += 1
    def libresPorPiso(self):
        i = 0
        long = len(self.__listaHoteles)
        nom = input("Ingrese el nombre del hotel: ")
        while i < long:
            if self.__listaHoteles[i].getNombre().lower() == nom.lower():
                self.__listaHoteles[i].libres()
            i += 1
    def detallePorTipo(self):
        i = 0
        long = len(self.__listaHoteles)
        nom = input("Ingrese el nombre del hotel: ")
        while i < long:
            if self.__listaHoteles[i].getNombre().lower() == nom.lower():
                self.__listaHoteles[i].detalles()
            i += 1