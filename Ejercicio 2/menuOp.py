from gestorBiblioteca import GestorBiblioteca
from claseBiblioteca import Biblioteca
def menu():
    print("\n--- MENÚ ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libro por título")
    print("4. Listar libros")
    print("x. Salir")

if __name__ == '__main__':
    gestor = GestorBiblioteca()
    gestor.cargar()
    op = ''
    while op != 'x':
        menu()
        op = input("Opción: ").lower()
        if op == '1':
            gestor.cargar()
        elif op == '2':
            tit = input("ingrese el titulo del libro a eliminar: ")
            gestor.eliminarLibro(tit)
        elif op == '3':
            t= input("ingrese el titulo del libro a buscar: ")
            gestor.buscarLibro(t)
        elif op == '4':
            gestor.mostrarBibliotecas()
        elif op == 'x':
            print("Saliendo...")
        else:
            print("Opción inválida")