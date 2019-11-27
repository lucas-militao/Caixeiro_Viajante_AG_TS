import numpy
from scipy.spatial import distance
import random

import Classes
import Funcoes


class AlgoritmoGenetico:

    def __init__(self, tamanhoDaPopulacao, geracoes, taxaDeCrossover, taxaDeMutacao, listaDeCidades):
        self.listaDeCidades = listaDeCidades
        self.tamanhoDaPopulacao = tamanhoDaPopulacao
        self.geracoes = geracoes
        self.taxaDeCrossover = taxaDeCrossover
        self.taxaDeMutacao = taxaDeMutacao

        self.populacao = []

    def gerarPopulacao(self):

        sequencia = []

        for i in range(1, numpy.size(self.listaDeCidades) + 1):
            sequencia.append(i)

        for i in range(self.tamanhoDaPopulacao):
            solucao = Classes.Solucao()
            solucao.caminho = sequencia
            random.shuffle(sequencia)
            solucao.aptidao = Funcoes.custo(self.listaDeCidades, solucao.caminho)
            self.populacao.append(solucao)

    def selecionarCaminho(self):

        v1 = random.randrange(numpy.size(self.populacao)//2)
        v2 = random.randrange(numpy.size(self.populacao)//2)

        if(self.populacao[v1].aptidao > self.populacao[v2].aptidao):
            return v2
        else:
            return v1



