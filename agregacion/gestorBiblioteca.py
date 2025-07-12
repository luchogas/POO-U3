from biblioteca import Biblioteca
class gestorBiblioteca:
    __listaBibliotecas : list
    def __init__(self):
        self.__listaBibliotecas = []
    def getListaBibliotecas(self):
        return self.__listaBibliotecas
    def agregarBiblioteca(self, unaBiblioteca):
        self.__listaBibliotecas.append(unaBiblioteca)
    
    def mostrar(self):
        for biblio in self.__listaBibliotecas:
            print(biblio.mostrar())
            for lib in biblio.getListaLibros():
                print(lib.mostrarLibros())
    def eliminarLibro(self, tit):
        nom = input("ingrese el nombre de la biblioteca: ")
        i = 0
        long = len(self.__listaBibliotecas)
        band = False
        while i < long and not band:
            if self.__listaBibliotecas[i].getNombre() == nom:
                band = True
            else:
                i+=1
        if band:
            self.__listaBibliotecas[i].eliminar(tit)
        else:
            print("error")
    def buscar(self, nom):
        i = 0
        long = len(self.__listaBibliotecas)
        band = False
        titt = input("nombre de biblio: ")
        while i < long and not band:
            if self.__listaBibliotecas[i].getNombre() == titt:
                band = True
            else:
                i+=1
        if band:
            self.__listaBibliotecas[i].mostrarr(nom, titt)
        else:
            print("error")
            