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

        Herdado = False

        for i in range(posicao1, posicao2):
            filho1[i] = pai1[i]
            filho2[i] = pai2[i]

        elementosNaoHerdados = []
        posicoes = []
        #--FILHO 1--
        for i in range(posicao1, posicao2):
            for j in range(posicao1, posicao2):
                if(filho1[j] == filho2[i]):
                    Herdado = True
                    break
            if(Herdado != True):
                elementosNaoHerdados.append(filho2[i])
                posicao = pai2.index(filho1[i])
                if(posicao > posicao1 and posicao < posicao2):
                    posicao = pai2.index(filho1[posicao])
                    posicoes.append(posicao)
                else:
                    posicoes.append(posicao)
            Herdado = False

        for i in range(numpy.size(elementosNaoHerdados)):
            filho1[posicoes[i]] = elementosNaoHerdados[i]

        for i in range(numpy.size(filho1)):
            if(filho1[i] == -1):
                filho1[i] = pai2[i]

        elementosNaoHerdados = []
        posicoes = []
        # --FILHO 2--
        for i in range(posicao1, posicao2):
            for j in range(posicao1, posicao2):
                if(filho1[i] == filho2[j]):
                    Herdado = True
                    break
            if(Herdado != True):
                elementosNaoHerdados.append(filho1[i])
                posicao = pai1.index(filho2[i])
                if(posicao > posicao1 and posicao < posicao2):
                    posicao = pai1.index(filho2[posicao])
                    posicoes.append(posicao)
                else:
                    posicoes.append(posicao)
            Herdado = False

        for i in range(numpy.size(elementosNaoHerdados)):
            filho2[posicoes[i]] = elementosNaoHerdados[i]

        for i in range(numpy.size(filho2)):
            if(filho2[i] == -1):
                filho2[i] = pai1[i]

        resultado = []
        resultado.append(Classes.Solucao)
        resultado.append(Classes.Solucao)
        resultado[0].caminho = filho1
        resultado[1].caminho = filho2
        return resultado


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

        resultado = []
        solucao = Classes.Solucao()
        solucao.caminho = filho1
        resultado.append(solucao)
        solucao = Classes.Solucao()
        solucao.caminho = filho2
        resultado.append(solucao)
        return resultado

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

        solucao = Classes.Solucao()
        solucao.caminho = elemento
        return solucao

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

        solucao = Classes.Solucao()
        solucao.caminho = elemento
        return solucao

    def selecao(self, solucoes):
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

    def sofrerMutacao(self):
        valor = random.randrange(0,100)

        if(valor > 10):
            return True
        else:
            return False

    def executar(self):

        self.gerarPopulacao()
        self.sorteio = []

        geracao = 0
        populacaoAtual = self.populacao
        filhos = []

        while(geracao < self.geracoes):

            while(numpy.size(filhos) < self.tamanhoDaPopulacao):
                self.sorteio = []
                self.selecao(populacaoAtual)

                resultado = self.crossoverPMX(5, 15,
                                  populacaoAtual[self.sorteio[0]].caminho,
                                  populacaoAtual[self.sorteio[1]].caminho)

                resultado[0].caminho = list(resultado[0].caminho)
                resultado[1].caminho = list(resultado[1].caminho)

                if(self.sofrerMutacao()):
                    resultado[0] = self.mutacaoInversao(resultado[0].caminho)
                    resultado[1] = self.mutacaoInversao(resultado[1].caminho)

                if(type(resultado[0].caminho[0]) == type(numpy.float64(10))):
                    resultado[0].caminho = numpy.array(resultado[0].caminho, dtype='int')
                    resultado[1].caminho = numpy.array(resultado[1].caminho, dtype='int')

                resultado[0].caminho = list(resultado[0].caminho)
                resultado[1].caminho = list(resultado[1].caminho)

                resultado[0].aptidao = Funcoes.custo(self.listaDeCidades, resultado[0].caminho)
                resultado[1].aptidao = Funcoes.custo(self.listaDeCidades, resultado[1].caminho)

                filhos.append(resultado[0])
                filhos.append(resultado[1])

            geracao = geracao + 1
            populacaoAtual = filhos
            filhos = []









