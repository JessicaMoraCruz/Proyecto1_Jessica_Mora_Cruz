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
        self.mensualidadFinal = (_mensualidad1 + _mensualidad2 + _mensualidad3) / 3
        self.historial = []

    def entregarDatos(self):
        print("No. Cedula: {} - {} {} - Mensualidad Final: {}".format(self.cedula, self.nombre, self.apellido, self.mensualidadFinal))

    def editarMensualidad(self, _mensualidad1, _mensualidad2, _mensualidad3):
        self.mensualidad1 = _mensualidad1
        self.mensualidad2 = _mensualidad2
        self.mensualidad3 = _mensualidad3
        self.mensualidadFinal = (_mensualidad1 + _mensualidad2 + _mensualidad3) / 3
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
    while True:
        print("____________________________________________________________________________")
        print("Bienvenido estimado usuario de la Banda Municipal de Acosta")
        print("A continuacion se le solicita que ingrese algunos datos de los estudiantes")
        print("Por favor selecciona alguna de las siguientes opciones")
        print("\n")
        print("____________________________________________________________________________")
        print("                               |*|  MENU  |*|                               ")
        print("____________________________________________________________________________")
        print("")
        print("Por favor elija una de las siguientes opciones:");
        print("1.- Registrar Integrante")
        print("2.- Mostrar Integrante")
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



if __name__ == "__main__":
    main()


