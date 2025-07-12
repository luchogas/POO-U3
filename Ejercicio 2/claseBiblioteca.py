from claseLibro import Libro
class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaLibros: list
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaLibros = []
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getListaLibros(self):
        return self.__listaLibros
    def agregarLibro(self, titulo, autor, isbn, genero):
        self.__listaLibros.append(Libro(titulo, autor, isbn, genero))
    def __str__(self):
        return f'Nombre: {self.__nombre}, Direccion: {self.__direccion}, Telefono: {self.__telefono}'
    def eliminar(self, titulo):
        i = 0
        long = len(self.__listaLibros)
        while i < long:
            if self.__listaLibros[i].getTitulo() == titulo:
                del self.__listaLibros[i]
                print(f"Libro '{titulo}' eliminado.")
                return
            i += 1
    def buscar(self, biblio, titulo):
        i = 0
        long = len(self.__listaLibros)
        while i < long:
            if self.__listaLibros[i].getTitulo() == titulo:
                print(f"{biblio}: autor: {self.__listaLibros[i].getAutor()}, Genero: {self.__listaLibros[i].getGenero()}")
                
            i += 1
    
    