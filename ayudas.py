
#POO - relaciones entre clases  U3 -   Ejemplos

# Asociación 1
# ==============================

#en la asociacion se programa del lado de menor cardinalidad
#import Libro
class Autor:
    __nombre : str
    __libro : object 
    def __init__(self, nombre, libro = None):#valor None para no crear referencia circular
        self.__nombre = nombre
        self.__libro = libro
        
    def __str__(self):
        return f"Autor: {self.__nombre}"
    def setLibro(self, libro):
        self.__libro = libro
    
    
class Libro:
    #import Autor -  se importa dentro de la clase en un modulo y fuera en otro para no generar problemas
    __titulo : str
    __autor : object
    def __init__(self, titulo, autor =  None):
        self.__titulo = titulo
        self.__autor = autor  
        self.__autor.setLibro(self) #le agrega el autor al libro
    
    def setAutor(self, autor):
        self.__autor = autor
    
    def mostrar(self):
        print(f"Libro: {self.__titulo}, escrito por {self.__autor}")




# ==============================
# Clase Asociación 
# ==============================
class RegistroCivil:
    __actas: list
    def __init__(self):
        self.__actas=[]
    
    def inscribirPersona(self):
        acta = ActaNacimiento(self  #atributos de la clase asociacion
)
        self.__actas.append(acta)
        
#en la clase de mayor cardinalidad no se hace nada
class Persona:
    __dni: int
    def __init__(self, dni):
        self.__dni=dni
    def mostrar(self):
        print(f"dni: {self.__dni}")
        
#esta es la clase asociacion       
class ActaNacimiento:
    __fechaInscripcion: str
    __numeroroLibro: int
    __numeroActa: int
    __persona: object# referencia a la clase persona
    __registrocivil: object #referenia a la clase registro civil 
    def __init__(self, nroActa, nroLibro, fecha, persona, registroCivil):
        self.__numeroActa = nroActa
        self.__numeroLibro = nroLibro
        self.__fecha = fecha
        self.__persona = persona
        self.__registrocivil = registroCivil



# ==============================
# Clase que modela una Asociación:
# ==============================

#aca las dos clases van a crear una lista de la clase que van a modelar por ser los dos de menor cardinalidad
class Medico:
    __prescripciones : list
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__prescripciones = []

    def agregarPrescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)


class Paciente:
    __prescripciones : list
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__prescripciones = []

    def agregarPrescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)
#esta es la clase que modela la asociacion
class Prescripcion:
    def __init__(self, medico, paciente, diagnostico):
        self.__medico = medico
        self.__paciente = paciente##                        añade las dos clases
        self.__diagnostico = diagnostico##
        self.__medico.agregarPrescripcion(self)#####
        self.__paciente.agregarPrescripcion(self)####

    def mostrar(self):
        print(f"Prescripción: {self.__diagnostico}, Médico: {self.__medico}, Paciente: {self.__paciente}")

# ==============================
# Agregación: relacion debil
# ==============================
class Bebida:  #parte
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def __str__(self):                                     #en las partes no se hace nada se programa normal
        return self.__nombre                                

class Plato: # parte
    def __init__(self, descripcion, precio):
        self.__descripcion = descripcion
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def __str__(self):
        return self.__descripcion

class Pedido: #todo incluye las partes pero la relacion es debil
    __bebidas : list
    __platos : list
    def __init__(self):
        self.__bebidas = []
        self.__platos = []

    def agregarBebida(self, bebida):
        self.__bebidas.append(bebida)

    def agregarPlato(self, plato):
        self.__platos.append(plato)

if __name__ == '__main__':
    #los objetos se crean aparte por que es una relacion debil
    plato1 = Plato()
    bebida1 = Bebida()
    pedido1 = Pedido(bebida1, plato1)
    del pedido1

# ==============================
# Composición: relacion fuerte
# ==============================
class CuentaCampus:
    def __init__(self, usuario, clave):
        self.__usuario = usuario
        self.__clave = clave

    def __str__(self):
        return f"Cuenta: {self.__usuario}, Clave: {self.__clave}"   #se programa en el todo

class Profesor:
    __cuentaCampus : object
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        usuario = (nombre + apellido).lower()
        self.__cuenta = CuentaCampus(usuario, dni)  # Composición, el objeto se crea dentro de la clase 
#                                                   # por ser relacion fuerte
    def __del__(self):
        del self.__cuentaCampus #puedo borrar la cuenta

# ==============================
# Herencia Simple
# ==============================

import math
class Circulo:                    #clase abstracta no se programa 
    def __init__(self, radio):
        self.__radio = radio

    def superficie(self):
        return math.pi * self.__radio**2

    def getRadio(self):
        return self.__radio

    def __str__(self):
        return f"Circulo de radio {self.__radio}"

class Cilindro(Circulo):                #clase concreta (clase de la que hereda) 
    def __init__(self, radio, altura):
        super().__init__(radio)# super invoca al constructor de la clase base o abstracta
        self.__altura = altura

    def volumen(self):
        return self.superficie() * self.__altura

    def __str__(self):
        return f"Cilindro de radio {self.getRadio()} y altura {self.__altura}"

# ==============================
# Tests simples
# ==============================
if __name__ == '__main__':
    # Asociación
    autor = Autor("Borges")
    libro = Libro("Ficciones", autor)
    libro.mostrar()

    # Clase Asociación
    medico = Medico("Dr. Pérez")
    paciente = Paciente("Juan López")
    prescripcion = Prescripcion(medico, paciente, "Gripe")
    prescripcion.mostrar()


    # Clase que modela la asociación
    m = Medico("Dra. Gómez")
    p = Paciente("Ana Torres")
    presc = Prescripcion(m, p, "Faringitis")
    presc.mostrar()

    # Agregación
    b1 = Bebida("Coca Cola", 800)
    pl1 = Plato("Milanesa con papas", 2500)
    pedido = Pedido()
    pedido.agregarBebida(b1)
    pedido.agregarPlato(pl1)
    pedido.mostrar()

    # Composición
    profe = Profesor("Karina", "Moreno", "20333111")
    print(profe)

    # Herencia
    c = Cilindro(5, 10)
    print(c)
    print("Volumen del cilindro:", c.volumen())
    
    
    
    
    
# ==============================
# Polimorfismo. capacidad de dos objetos de clases diferentes  de responder al mismo mensaje de forma diferente
# ==============================
import math
import numpy as np

class Cuerpo:
    def __init__(self, altura):
        self.__altura = altura

    def superficieBase(self):
        # Método que será redefinido por las subclases ya que es abstracto
        pass

    def volumen(self):
        return self.superficieBase() * self.__altura

    def getAltura(self):
        return self.__altura

# Subclase Cilindro
class Cilindro(Cuerpo):
    def __init__(self, altura, radio):
        super().__init__(altura)
        self.__radio = radio

    def superficieBase(self):
        return math.pi * self.__radio ** 2 ##cada uno responde de forma diferente al mismo mensaje

    def __str__(self):
        return f"Cilindro - Altura: {self.getAltura()}, Radio: {self.__radio}"

# Subclase PrismaRectangular 
class PrismaRectangular(Cuerpo):
    def __init__(self, altura, lado1, lado2):
        super().__init__(altura)
        self.__lado1 = lado1
        self.__lado2 = lado2

    def superficieBase(self):
        return self.__lado1 * self.__lado2 ## cada uno responde de forma diferente al mismo mensaje

    def __str__(self):
        return f"Prisma Rectangular - Altura: {self.getAltura()}, Lado1: {self.__lado1}, Lado2: {self.__lado2}"

# Arreglo de cuerpos (polimorfismo)
class Arreglo:
    def __init__(self, dimension=10):
        self.__cuerpos = np.empty(dimension, dtype=object)
        self.__actual = 0
        self.__dimension = dimension

    def agregarCuerpo(self, cuerpo):
        if self.__actual < self.__dimension:
            self.__cuerpos[self.__actual] = cuerpo
            self.__actual += 1

    def calcularVolumenes(self):
        for i in range(self.__actual):
            c = self.__cuerpos[i]
            print(str(c)+', volumen = {0:7.2f} '.format(c.volumen()))
            
            
# ==============================
# Ejemplo completo de Excepciones
# ==============================

# ------------------------------
# assert: control lógico simple
# ------------------------------
def verificar_precio(precio):
    # Verifica que el precio sea mayor a cero
    assert precio > 0, "El precio debe ser mayor a cero."
    print(f"Precio correcto: ${precio}")

# ------------------------------
# raise: forzar una excepción manualmente
# ------------------------------
def dividir(a, b):
    # Si b es cero, lanza un error manualmente
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b

# ------------------------------
# Excepción personalizada
# ------------------------------
class ErrorEdad(Exception):
    def __init__(self, mensaje="Edad inválida"):
        super().__init__(mensaje)

def verificar_edad(edad):
    # Lanza una excepción propia si la edad es menor a 18
    if edad < 18:
        raise ErrorEdad("Debés ser mayor de edad para registrarte.")
    print("Edad aceptada.")

# ------------------------------
# try / except para manejar errores de ingreso
# ------------------------------
def cargar_dato():
    try:
        numero = int(input("Ingresá un número entero: "))
        print("Número ingresado correctamente:", numero)
    except ValueError:
        print("Error: eso no es un número entero.")

# ------------------------------
# Test general
# ------------------------------
if __name__ == "__main__":
    print("Test de assert:")
    try:
        verificar_precio(150)
        verificar_precio(-10)  # Esto lanza el assert
    except AssertionError as e:
        print(e)

    print("\nTest de raise con división:")
    try:
        resultado = dividir(20, 0)
        print("Resultado:", resultado)
    except ZeroDivisionError as e:
        print(e)

    print("\nTest de excepción personalizada:")
    try:
        verificar_edad(16)
    except ErrorEdad as e:
        print(e)

    print("\nTest de try/except clásico:")
    cargar_dato()
    
    
# ==============================
# listas definidas por el programador
# ==============================
class Profesor:
    def __init__(self, dni, apellido, nombre):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre

    def getDNI(self):
        return self.__dni

    def __str__(self):
        return f"Profesor:\nApellido y nombre: {self.__apellido}, {self.__nombre}\nClave: {self.__dni}"

# ==============================
# Clase Nodo
# ==============================
class Nodo:
    __profesor : Profesor
    __siguiente : object
    def __init__(self, profesor):
        self.__profesor = profesor
        self.__siguiente = None

    def setSiguiente(self, nodosig):
        self.__siguiente = nodosig # Siguiente nodo en la lista

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__profesor

# ==============================
# Clase Lista (iterable definida por el programador)
# ==============================
class Lista:
    __comienzo : Nodo
    def __init__(self):
        self.__comienzo = None

    def agregarProfesor(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
    def listar(self):
        aux = self.__comienzo
        while aux is not None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    def eliminarPorDNI(self, dni):
        aux = self.__comienzo
        encontrado = False

        if aux is not None and aux.getDato().getDNI() == dni:
            print(" Encontrado y eliminado:\n", aux.getDato())
            self.__comienzo = aux.getSiguiente()
            del aux
            self.__tope -= 1
            return

        ant = aux
        aux = aux.getSiguiente()
        while aux is not None and not encontrado:
            if aux.getDato().getDNI() == dni:
                encontrado = True
            else:
                ant = aux
                aux = aux.getSiguiente()

        if encontrado:
            print(" Encontrado y eliminado:\n", aux.getDato())
            ant.setSiguiente(aux.getSiguiente())
            del aux
            self.__tope -= 1
        else:
            print(f" El DNI {dni} no está en la lista.")

# ==============================
# Test de Lista definida por el programador
# ==============================
if __name__ == '__main__':
    lista = Lista()
    lista.agregarProfesor(Profesor(20201234, 'Moreno', 'Karina'))
    lista.agregarProfesor(Profesor(11234432, 'Díaz', 'Mónica'))
    lista.agregarProfesor(Profesor(31002008, 'Pusineri', 'Lucas'))

    print("📋 Listado completo:")
    for profe in lista:
        print(" Datos del", profe)

    lista.eliminarPorDNI(11234432)

    print("\n📋 Listado luego de borrar:")
    for profe in lista:
        print(" Datos del", profe)
        

#Ejemplos JSON
# ======================
# Clase Medio
# ======================
import json
class Medio:
    def __init__(self, nombre, tipo, frecuencia, alcance):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__frecuencia = frecuencia
        self.__alcance = alcance

    def getNombre(self):
        return self.__nombre

    def mostrar(self):
        print(f"{self.__nombre} ({self.__tipo}) - {self.__frecuencia}, {self.__alcance}")

# ======================
# Gestor de Medios
# ======================
class GestorMedios:
    def __init__(self):
        self.__medios = []

    def cargarDesdeJSON(self, archivo):
        with open(archivo, 'r') as f:
            data = json.load(f)
            for item in data:
                medio = Medio(
                    item['nombre'],
                    item['tipo'],
                    item['frecuencia'],
                    item['alcance']
                )
                self.__medios.append(medio)

    def mostrarTodos(self):
        for m in self.__medios:
            m.mostrar()

    def buscarPorTipo(self, tipo):
        i = 0
        while i < len(self.__medios):
            if self.__medios[i]._Medio__tipo == tipo:
                self.__medios[i].mostrar()
            i += 1

# ======================
# Main que solo delega
# ======================
if __name__ == "__main__":
    gm = GestorMedios()
    gm.cargarDesdeJSON("medios.json")
    print("📋 Todos los medios:")
    gm.mostrarTodos()

    print("\n📡 Medios de tipo TV:")
    gm.buscarPorTipo("TV")
    
    
    
# ======================
# Interfaz (Clase Abstracta)
# ======================
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def getColor(self):
        return self._color

# ======================
# Subclases concretas
# ======================
class Rectangulo(Figura):
    def __init__(self, base, altura, color):
        super().__init__(color)
        self.__base = base
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura

    def tipo(self):
        return "Rectángulo"

    def __str__(self):
        return f"[{self.tipo()}] Área: {self.area()} - Color: {self._color}"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.__radio = radio

    def area(self):
        import math
        return math.pi * self.__radio**2

    def tipo(self):
        return "Círculo"

    def __str__(self):
        return f"[{self.tipo()}] Área: {self.area():.2f} - Color: {self._color}"

# ======================
# Testing con isinstance(), type(), polimorfismo y abstracción
# ======================
if __name__ == '__main__':
    figuras = [
        Rectangulo(10, 5, "rojo"),
        Circulo(7, "azul"),
        Rectangulo(2, 3, "verde"),
        Circulo(1, "amarillo")
    ]

    print("📋 Dibujando figuras con polimorfismo:")
    for fig in figuras:
        print(fig)

    print("\n🔍 Probando isinstance() y type():")
    for fig in figuras:
        if isinstance(fig, Circulo):
            print(f"→ {fig.tipo()} de tipo Circulo (con isinstance)")
        if type(fig) == Rectangulo:
            print(f"→ {fig.tipo()} de tipo exacto Rectangulo (con type)")
