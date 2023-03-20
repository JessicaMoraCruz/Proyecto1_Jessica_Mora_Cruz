class Singleton:
    instance = None
    def __init__(self):
        pass
    clave = input("Clave: ")
    @classmethod
    def crearInstancia(cls):
        if not cls.__instancia:
            cls.__instancia = Singleton()
        return cls.__instancia
    def __str__(self):
        return self.clave
instancia1=Singleton.crearInstancia()
instancia2=Singleton.crearInstancia()
print("Instancia1: ", instancia1)
print("Instancia2: ", instancia2)
print()
print(instancia1 is instancia2)

