import numpy as np
from scipy.spatial import distance
import Util
import random

class AlgoritmoGenetico:

    def __init__(self, numeroDeCidades, quantidadeDaPopulacao, numeroDeGeracoes, cidades, taxaDeCrossover, taxaDeMutacao):
        self.numeroDeCidades = numeroDeCidades
        self.cidades = cidades
        self.quantidadeDaPopulacao = quantidadeDaPopulacao
        self.numeroDeGeracoes = numeroDeGeracoes
        self.taxaDeCrossover = taxaDeCrossover
        self.taxaDeMutacao = taxaDeMutacao


    def calcularDistanciaEuclideana(self, coordenada1, coordenada2):
        return distance.euclidean(coordenada1, coordenada2)

    # def calcularCusto(self, caminho):


    def geraPopulacao(self):
        global populacao

        for i in range(self.quantidadeDaPopulacao):
            solucao = Util.Solucao()
            solucao.caminho = self.cidades
            random.shuffle(solucao.caminho)
            print(solucao.caminho)





