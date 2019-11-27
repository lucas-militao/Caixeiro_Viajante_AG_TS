import numpy
import random

import AlgoritmoGenetico
import Classes
import Funcoes

#Lendo arquivo e retirando dados do mesmo
arquivo = open('ncit30.dat')
conteudo = arquivo.readlines()

numeroDeCidades = 0
listaDeCidades = []

for i in range(numpy.size(conteudo)):
    cidade = conteudo[i].split()
    cidade = [int(j) for j in cidade]
    if(i != 0):
        listaDeCidades.append(Classes.Cidade(i, cidade[0], cidade[1]))
    else:
        numeroDeCidades = cidade[0]

#------------------------------------------

tamanhoDaPopulacao = 50
geracoes = 50
taxaDeCrossover = 0.75
taxaDeMutacao = 0.1

# def gerarPopulacao(populacao):
#
#     for i in range(populacao):
#         solucao = Classes.Solucao()
#         solucao.caminho = sequencia
#         random.shuffle(solucao.caminho)
#         solucao.aptidao = Funcoes.custo(cidades, solucao.caminho)
#
#         print(solucao.aptidao)
#
# gerarPopulacao(1)

algoritmo = AlgoritmoGenetico.AlgoritmoGenetico(tamanhoDaPopulacao,
                                                geracoes,
                                                taxaDeCrossover,
                                                taxaDeMutacao,
                                                listaDeCidades)

algoritmo.gerarPopulacao()
print(algoritmo.selecionarCaminho())

