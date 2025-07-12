class Libro:
    __titulo : str
    __autor : str
    __isbn : str
    __genero : str
    def __init__(self, titulo, autor, isbn, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__genero = genero
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getIsbn(self):
        return self.__isbn
    def getGenero(self):
        return self.__genero
    
    def mostrarLibros(self):
        print(f"{self.__titulo} - {self.__autor} - {self.__isbn} - {self.__genero}")