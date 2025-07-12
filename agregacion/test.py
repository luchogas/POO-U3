from gestorBiblioteca import gestorBiblioteca
from libro import Libro
from biblioteca import Biblioteca

def test():
    gestor = gestorBiblioteca()
    
    #otra manera de crear objetos si se pide ingresar por teclado
    # nombreBiblioteca = input("ingrese nombre de la biblioteca: ")
    # B3 = Biblioteca(nombreBiblioteca)
    # nombreLibro = input("ingrese nombre del libro: ")
    # L4 = Libro(nombreLibro)
    
    #B3.agregarLibro(L4)
    
    
    B1 = Biblioteca("Biblioteca Nacional", "Av. Libertador 2500", "011-12345678")
    B2 = Biblioteca("Biblioteca del Congreso", "Hipólito Yrigoyen 1750", "011-87654321")
    gestor.agregarBiblioteca(B1)
    gestor.agregarBiblioteca(B2)
    
    L1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 9780307474728, "Ficción")
    L2 = Libro("El Principito", "Antoine de Saint-Exupéry", 9780156012195, "Ficción")
    L3 = Libro("1984", "George Orwell", 9780451524935, "Ciencia Ficción")
    try:
        B1.agregarLibro(L1)
        B1.agregarLibro(L2)
        B2.agregarLibro(L3)
    except TypeError:
        print("error jeje")
    gestor.mostrar()
    gestor.eliminarLibro("Cien Años de Soledad")
    nom = input("ingrese el titulo de un libro:")
    gestor.buscar(nom)
    gestor.mostrar()
if __name__ == "__main__":
    test()