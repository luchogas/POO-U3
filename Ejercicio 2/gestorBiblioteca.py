from claseBiblioteca import Biblioteca
from claseLibro import Libro
import csv
class GestorBiblioteca:
    __listaBibliotecas: list
    def __init__(self):
        self.__listaBibliotecas = []
    def agregarBiblioteca(self, unaBiblioteca: Biblioteca):
        self.__listaBibliotecas.append(unaBiblioteca)
        
    def cargar(self):
        archivo = open('C:\\Users\\usuario\\Desktop\\Luciano-LCC\\2ºaño\\POO\\U3\\Ejercicio 2U3\\Biblioteca.csv')
        reader = csv.reader(archivo, delimiter=';')
        i = -1
        for fila in reader:
            if len(fila) == 3:
                biblioteca = Biblioteca(fila[0], fila[1], fila[2])
                self.agregarBiblioteca(biblioteca)
                i += 1
            elif len(fila) == 4:
                titulo = fila[0]
                autor = fila[1]
                isbn = fila[2]
                genero = fila[3]
                self.__listaBibliotecas[i].agregarLibro(titulo, autor, isbn, genero)
        archivo.close()
    def mostrarBibliotecas(self):
        for biblioteca in self.__listaBibliotecas:
            print(biblioteca)
            for libro in biblioteca.getListaLibros():
                print(libro)
    def eliminarLibro(self , tit):
        i = 0
        long = len(self.__listaBibliotecas)
        n = input("ingrese el nombre de la biblioteca: ")
        while i < long:
            if self.__listaBibliotecas[i].getNombre() == n:
                self.__listaBibliotecas[i].eliminar(tit)
            i += 1
    def buscarLibro(self, t):
        i = 0
        long = len(self.__listaBibliotecas)
        biblio = input("ingrese el nombre de la biblioteca: ")
        while i < long:
            if self.__listaBibliotecas[i].getNombre() == biblio:
                self.__listaBibliotecas[i].buscar(biblio, t)
            i += 1
        
