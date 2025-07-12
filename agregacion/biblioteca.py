from libro import Libro
class Biblioteca:
    __nombre : str
    __direccion : str
    __telefono : str
    __listaLibros : list
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaLibros = []
        
        
        
    def agregarLibro(self, unLibro):
        if isinstance(unLibro, Libro):
            self.__listaLibros.append(unLibro)
        else:
            raise TypeError    
        
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getListaLibros(self):
        return self.__listaLibros
    
    def mostrar(self):
        print(f"{self.__nombre} - {self.__direccion} - {self.__telefono} ")
        
    def eliminar(self, tit):
        i = 0
        long = len(self.__listaLibros)
        band = False
        while i < long and not band:
            if self.__listaLibros[i].getTitulo() == tit:
                band = True
            else:
                i+=1
        if band:
            del self.__listaLibros[i]
            print(f"libro {tit} eliminado")
            return True
        else:
            print("error")
    def mostrarr(self, nom, titt):
        i = 0
        long = len(self.__listaLibros)
        band = False
        while i < long and not band:
            if self.__listaLibros[i].getTitulo() == nom:
                band = True
            else:
                i+=1
        if band:
            print(f"para el titulo: {nom} - {titt}- autor:{self.__listaLibros[i].getAutor()}- genero: {self.__listaLibros[i].getGenero()}")
        else:
            print("error")