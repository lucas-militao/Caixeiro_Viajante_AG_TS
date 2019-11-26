class Cidade:
    def __init__(self, numero, coordenadaX, coordenadaY):
        self.numero = numero
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

class Solucao:
    def __init__(self):
        self.caminho = []
        self.aptidao = -1