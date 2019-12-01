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
        #--SEQUENCIA ARMAZENA ORDENADAMENTE O NÚMERO INTEIRO QUE REPRESENTA CADA CIDADE--
        self.populacao = []
        sequencia = []

        for i in range(1, numpy.size(self.listaDeCidades) + 1):
            sequencia.append(i)

        #--ALEATORIAMENTE FORMA OS CAMINHOS E CALCULA A APTIDÃO DE CADA POSSÍVEL SOLUÇÃO--
        for i in range(self.tamanhoDaPopulacao):
            solucao = Classes.Solucao()
            solucao.caminho = sequencia.copy()
            random.shuffle(solucao.caminho)
            solucao.aptidao = Funcoes.custo(self.listaDeCidades, solucao.caminho)
            self.populacao.append(solucao)

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

        #--COPIA PARA AS DUAS POSICOES SELECIONADAS PARTE DO PAI 1 PARA O FILHO 1 E DO PAI 2 PARA O FILHO 2--
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

        solucao = Classes.Solucao()
        solucao.caminho = filho1
        self.filhos.append(solucao)
        solucao = Classes.Solucao()
        solucao.caminho = filho2
        self.filhos.append(solucao)


    def crossoverAPX(self, pai1, pai2):

        filho1 = []
        filho2 = []
        tamanho = numpy.size(pai1)
        Herdado = False

        for i in range(tamanho):
            if(numpy.size(filho1) < tamanho):

                for j in filho1:
                    if(j == pai1[i]):
                        Herdado = True
                        break
                if(Herdado == True):
                    Herdado = False
                    for j in filho1:
                        if(j == pai2[i]):
                            Herdado = True
                            break
                    if(Herdado == False):
                        filho1.append(pai2[i])
                else:
                    filho1.append(pai1[i])
            else:
                break

        for i in range(tamanho):
            if(numpy.size(filho2) < tamanho):

                for j in filho2:
                    if(j == pai2[i]):
                        Herdado = True
                        break
                if(Herdado == True):
                    Herdado = False
                    for j in filho2:
                        if(j == pai1[i]):
                            Herdado = True
                            break
                    if(Herdado == False):
                        filho2.append(pai1[i])
                else:
                    filho2.append(pai2[i])
            else:
                break

        solucao = Classes.Solucao()
        solucao.caminho = filho1
        self.filhos.append(solucao)
        solucao = Classes.Solucao()
        solucao.caminho = filho2
        self.filhos.append(solucao)

    def mutacaoBaseadaEmPosicao(self, elemento):

        pos1 = random.randint(0, numpy.size(elemento) - 1)
        pos2 = random.randint(0, numpy.size(elemento) - 1)

        j = 0

        if(pos1 < pos2):
            j = elemento[pos1]
            for i in range(pos1, pos2):
                elemento[i] = elemento[i+1]
            elemento[pos2] = j
        else:
            j = elemento[pos2]
            for i in range(pos2, pos1):
                elemento[i] = elemento[i+1]
            elemento[pos1] = j
        print(elemento)

    def mutacaoInversao(self, elemento):

        pos1 = random.randint(0, numpy.size(elemento) - 1)
        pos2 = random.randint(0, numpy.size(elemento) - 1)

        parteCortada = []

        if(pos1 < pos2):
            for i in range(pos1, pos2):
                parteCortada.append(elemento[i])
            parteCortada.reverse()
            elemento[pos1:pos2] = parteCortada
        else:
            for i in range(pos2, pos1):
                parteCortada.append(elemento[i])
            parteCortada.reverse()
            elemento[pos2:pos1] = parteCortada

        print(elemento)

    def roleta(self, solucoes):
        #--ORDENA AS SOLUÇÕES A PARTIR DA APTIDÃO--
        solucoes.sort(key=lambda i: i.aptidao, reverse=True)
        #--FUNÇÃO DE APTIDÃO--
        maior = solucoes[0].aptidao
        menor = solucoes[numpy.size(solucoes) - 1].aptidao
        N = numpy.size(solucoes)
        fi = []

        for i in range(N):
            fi.append(menor+((maior-menor)*((N-i)/(N-1))))

        soma = 0
        for i in solucoes:
            soma = soma + i.aptidao

        probabilidade = []
        for i in fi:
            probabilidade.append(i/soma)

        elemento = random.randrange(int(fi[numpy.size(fi) - 1]), int(fi[0]))
        pai = min(fi, key=lambda x:abs(x-elemento))
        pos = fi.index(pai)
        self.sorteio.append(pos)
        elemento = random.randrange(int(fi[numpy.size(fi) - 1]), int(fi[0]))
        pai = min(fi, key=lambda x: abs(x - elemento))
        pos = fi.index(pai)
        self.sorteio.append(pos)

    def executar(self):

        self.gerarPopulacao()
        self.filhos = []
        self.sorteio = []

        geracao = 0
        populacaoAtual = self.populacao

        self.gerarPopulacao()

        while(geracao < self.geracoes):

            while(numpy.size(self.filhos) < self.tamanhoDaPopulacao):
                self.sorteio = []
                self.roleta(populacaoAtual)

                self.crossoverPMX(5, 15,
                                  populacaoAtual[self.sorteio[0]].caminho,
                                  populacaoAtual[self.sorteio[1]].caminho)

                # if(numpy.size(self.filhos) < self.tamanhoDaPopulacao):










