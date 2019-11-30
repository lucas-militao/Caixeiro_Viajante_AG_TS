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

    def crossoverPMX(self, posicao1, posicao2, pai1, pai2):

        filho1 = numpy.zeros(numpy.size(pai1))
        filho2 = numpy.zeros(numpy.size(pai2))

        filho1[:] = -1
        filho2[:] = -1

        for i in range(posicao1, posicao2):
            filho1[i] = pai1[i]
            filho2[i] = pai2[i]

        elementosNaoHerdados1 = []
        elementoHerdado1 = False

        elementosNaoHerdados2 = []
        elementoHerdado2 = False

        for i in range(posicao1, posicao2):
            for j in range(posicao1, posicao2):
                if(pai2[i] == filho1[j]):
                    elementoHerdado1 = True
                if(pai1[i] == filho2[j]):
                    elementoHerdado2 = True
            if(elementoHerdado1 == False):
                elementosNaoHerdados1.append(pai2[i])
            if(elementoHerdado2 == False):
                elementosNaoHerdados2.append(pai1[i])
            elementoHerdado1 = False
            elementoHerdado2 = False

        #--FILHO 1--
        for i in range(numpy.size(elementosNaoHerdados1)):
            pos = pai2.index(elementosNaoHerdados1[i])
            elemento = pai1[pos]
            pos = pai2.index(elemento)
            if(pos >= posicao1 and pos < posicao2):
                elemento = pai1[pos]
                pos = pai2.index(elemento)
                filho1[pos] = elementosNaoHerdados1[i]
            else:
                filho1[pos] = elementosNaoHerdados1[i]

        for i in range(numpy.size(filho1)):
            if(filho1[i] == -1):
                filho1[i] = pai2[i]

        #--FILHO 2--
        for i in range(numpy.size(elementosNaoHerdados2)):
            pos = pai1.index(elementosNaoHerdados2[i])
            elemento = pai2[pos]
            pos = pai1.index(elemento)
            if (pos >= posicao1 and pos < posicao2):
                elemento = pai2[pos]
                pos = pai1.index(elemento)
                filho2[pos] = elementosNaoHerdados2[i]
            else:
                filho2[pos] = elementosNaoHerdados2[i]

        for i in range(numpy.size(filho2)):
            if(filho2[i] == -1):
                filho2[i] = pai1[i]
        #--TESTE--
        # print(filho1)
        # print(filho2)
        # print(elementosNaoHerdados1)
        # print(elementosNaoHerdados2)

    def crossoverAPX(self, pai1, pai2):

        filho1 = numpy.zeros(numpy.size(pai1))
        filho2 = numpy.zeros(numpy.size(pai2))
        filho1 = []
        filho2 = []

        Herdado = False

        #--FILHO 1--
        for i in range(numpy.size(pai1)):
            for j in filho1:
                if(pai1[i] == j):
                    Herdado = True
                    break
            if(Herdado == False):
                filho1.append(pai1[i])
            Herdado = False

            for j in filho1:
                if(pai2[i] == j):
                    Herdado = True
                    break
            if(Herdado == False):
                filho1.append(pai2[i])
            Herdado = False

        #--FILHO 2--
        for i in range(numpy.size(pai2)):
            for j in filho2:
                if(pai2[i] == j):
                    Herdado = True
                    break
            if(Herdado == False):
                filho2.append(pai2[i])
            Herdado = False

            for j in filho2:
                if(pai1[i] == j):
                    Herdado = True
                    break
            if(Herdado == False):
                filho2.append(pai1[i])
            Herdado = False