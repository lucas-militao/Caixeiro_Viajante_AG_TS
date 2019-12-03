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

algoritmo = AlgoritmoGenetico.AlgoritmoGenetico(tamanhoDaPopulacao,
                                                geracoes,
                                                taxaDeCrossover,
                                                taxaDeMutacao,
                                                listaDeCidades)


# algoritmo.executar()

#--TESTE--
pai1 = [1,2,3,4,5,6,7,8,9]
pai2 = [9,3,7,8,2,6,5,1,4]
#
# resultado = algoritmo.crossoverPMX(2, 7, pai1, pai2)
# algoritmo.crossoverAPX(pai1, pai2)
# algoritmo.mutacaoBaseadaEmPosicao(pai1)
# algoritmo.mutacaoInversao(pai1)
# print(resultado[0].caminho)
# print(resultado[1].caminho)

resultado = []
resultado.append(Classes.Solucao())
resultado.append(Classes.Solucao())
resultado[0].caminho = pai1
resultado[1].caminho = pai2
