import random
import os
class InformacionBandaMunicipalAcosta:

    def __init__(self, BMA_cursos=None):
        """ Cursos Banda Municipal de Acosta """
        self.BMA_cursos = BMA_cursos
    def programa_De_Cursos_BMA(self):
        """Crea y muestra cursos usando el metodo: abstract factory"""
        programa = self.BMA_cursos()
        print("Necesita guia sobre cursos:  {} de la BMA?".format(programa))
        print("Su duracion es de  {} ".format(programa.tiempo()))
        print("Su precio sería {}".format(programa.precio()))
        print('\n')

class Basicos:
    """ Clase de solfeo ritmico"""
    def tiempo(self):
        return "Un mes"
    def precio(self):
        return "15000"
    def __str__(self):
        return "Basico"

class Medios:
    """ Clase de solfeo melodico"""
    def tiempo(self):
        return "Un mes"
    def precio(self):
        return "25000"
    def __str__(self):
        return "Medio"

class Premium:
    """ Clase solfeo ritmico melodico y ejecucion de instrumento"""
    def tiempo(self):
        return "Tres meses"
    def precio(self):
        return "50000"
    def __str__(self):
        return "Premium"

def programa_aleatorio():
    """ Se brindara informacion aleatoria para los usuarios"""
    return random.choice([Basicos, Medios, Premium])()

listaIntegrantes=[]


class Integrantes:
    def __init__(self, _cedula, _nombre, _apellido, _edad, _mensualidad1, _mensualidad2, _mensualidad3):
        self.cedula = _cedula
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.mensualidad1 = _mensualidad1
        self.mensualidad2 = _mensualidad2
        self.mensualidad3 = _mensualidad3
        self.mensualidadFinal = (_mensualidad1 + _mensualidad2 + _mensualidad3)
        # A continuacion se calcula el monto que le va a corresponder a cada profesor
        # por las mensualidades pagadas por este estudiante
        self.montoProfesor = (_mensualidad1 + _mensualidad2 + _mensualidad3) / 5
        self.historial = []

    def entregarDatos(self):
        print("No. Cedula: {} - {} {} - Mensualidad Final: {} - Monto a Profesor: {}".format(self.cedula, self.nombre, self.apellido, self.mensualidadFinal, self.montoProfesor))

    def editarMensualidad(self, _mensualidad1, _mensualidad2, _mensualidad3):
        self.mensualidad1 = _mensualidad1
        self.mensualidad2 = _mensualidad2
        self.mensualidad3 = _mensualidad3
        self.mensualidadFinal = (_mensualidad1 + _mensualidad2 + _mensualidad3)
        self.montoProfesor = (_mensualidad1 + _mensualidad2 + _mensualidad3) / 5
        print("Registro Exitoso!")

    def incluirEvento(self, _mensualidad1, _mensualidad2, _mensualidad3):
        return ("modificacion: Mensualidad_1: {} Mensualidad_2: {} Mensualidad_3: {}".format(_mensualidad1, _mensualidad2, _mensualidad3))

    def entregaHistorial(self):
        print("No. Cedula: {} - {} {}".format(self.cedula, self.nombre, self.apellido))


def registrarIntegrante():
    print("Registro de Integrantes\n")
    cedula = int(input("Ingrese el numero de cedula: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese su edad: "))
    mensualidad1 = float(input("Ingrese mensualidad 1: "))
    mensualidad2 = float(input("Ingrese mensualidad 2: "))
    mensualidad3 = float(input("Ingrese mensualidad 3: "))
    objIntegrante = Integrantes(cedula, nombre, apellido, edad, mensualidad1, mensualidad2, mensualidad3)
    listaIntegrantes.append(objIntegrante)

def listadoIntegrantes():
    print("Listado de Integrantes\n")
    for objIntegrante in listaIntegrantes:
        objIntegrante.entregarDatos()


def buscarIntegrante():
    print("Buscar Integrante\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objIntegrante in listaIntegrantes:
        if cedula == objIntegrante.cedula:
            objIntegrante.entregarDatos()


def modificarMensualidad():
    print("Modificar Mensualidad\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objIntegrante in listaIntegrantes:
        if cedula == objIntegrante.cedula:
            mensualidad1 = float(input("Ingrese mensualidad 1: "))
            mensualidad2 = float(input("Ingrese mensualidad 2: "))
            mensualidad3 = float(input("Ingrese mensualidad 3: "))
            objIntegrante.editarMensualidad(mensualidad1, mensualidad2, mensualidad3)
            objIntegrante.entregarDatos()
            recepcionMensaje = objIntegrante.incluirEvento(mensualidad1, mensualidad2, mensualidad3)
            objIntegrante.historial.append(recepcionMensaje)


def consultarHistorial():
    print("Consulta de Historial\n")
    cedula = int(input("Ingrese el numero de cedula a buscar: "))
    for objIntegrante in listaIntegrantes:
        if cedula == objIntegrante.cedula:
            for recepcionMensaje in objIntegrante.historial:
                print("Evento: {}".format(recepcionMensaje))

def salir():
    print("Has elegido finalizar, muchas gracias. ")
    exit()

def main():

    os.system('cls' if os.name == 'nt' else'clear')
    # Bienvenida a los profesores de la Banda Municipal de Acosta
    print("____________________________________________________________________________")
    print("Bienvenido estimado profesor de la Banda Municipal de Acosta")
    print("____________________________________________________________________________")
    print("")
    # Lista de profesores autorizados para editar la lista
    profesores_encargados = ["Jose", "Julio", "Axel", "Jessica", "Ernesto"]
    nombre = input("Estimado profesor por favor ingrese su nombre: ")
    if nombre in profesores_encargados:
        print("Usted está autorizado a editar, ya que se encuentra en la siguiente lista: ")
    else:
        print("Usted no está autorizado a editar, ya que no se encuentra en la siguiente lista: ")

    # Lista de profesores en una matriz que es recorrida mediante un for y se imprimen los datos.
    lista_de_profesores = [['N°', 'ID', '       Nombre', ' Cant.Est.', 'Años expe'],
                           [1, 112340981, 'Jose \t\t', 3, 15],
                           [2, 114560981, 'Julio \t\t  ', 2, 5],
                           [3, 113450876, 'Axel \t\t   ', 6, 6],
                           [4, 111230567, 'Jessica \t', 5, 10],
                           [5, 113450967, 'Ernesto\t\t', 4, 8]]
    b = ''
    for i in range(6):
        for j in range(5):
            b += str(lista_de_profesores[i][j]) + '\t'
        print(b)
        b = ''
    os.system('cls' if os.name == 'nt' else'clear')
    # A continuación se brinda el total de estudiantes que le corresponde a cada profesor.
    # La lista primero está desordena según la cantidad, luego se ordena de menor a mayor cantidad.

    print("A continuacion se indica la cantidad de estudiantes que deben ingresar")
    profes = [
        ('Jose', 3, 'Saxofon'),
        ('Julio', 2, 'Trompeta'),
        ('Axel', 6, 'Clarinete'),
        ('Jessica', 5, 'Trombon'),
        ('Ernesto', 4, 'Tuba')
    ]
    print(sorted(profes, key=lambda profe: profe[1]))
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("A continuacion se le solicita que ingrese algunos datos de los estudiantes")
        print("Por favor selecciona alguna de las siguientes opciones")
        print("\n")
        print("____________________________________________________________________________")
        print("                              ----  MENU  ----                              ")
        print("____________________________________________________________________________")
        print("")
        print("Por favor elija una de las siguientes opciones:");
        print("1.- Ingresar datos de integrantes")
        print("2.- Mostrar datos de integrante")
        print("3.- Buscar Integrante")
        print("4.- Modificar mensualidad")
        print("5.- Consultar Historial")
        print("6.- Salir\n")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            registrarIntegrante()
        elif opcion == 2:
            listadoIntegrantes()
        elif opcion == 3:
            buscarIntegrante()
        elif opcion == 4:
            modificarMensualidad()
        elif opcion == 5:
            consultarHistorial()
        elif opcion == 6:
            salir()
        i = input("\nDesea volver al menu principal (s/n). Si elige NO se le mostrara informacion de cursos BMA")
        if i == 'n' or i == 'N':
            break


if __name__ == "__main__":
    main()
    programa = InformacionBandaMunicipalAcosta(programa_aleatorio)
    for i in range(5):
        programa.programa_De_Cursos_BMA()


