import random
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

if __name__ == '__main__':
    programa = InformacionBandaMunicipalAcosta(programa_aleatorio)
    for i in range(5):
        programa.programa_De_Cursos_BMA()