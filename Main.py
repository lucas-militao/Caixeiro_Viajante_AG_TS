import numpy
import random
import matplotlib.pyplot as plt

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


resultado = algoritmo.executar()

menor = resultado[0]

for i in range(numpy.size(resultado)):
    if(menor.aptidao > resultado[i].aptidao):
        menor = resultado[i]

x = []
y = []
for i in range(numpy.size(menor.caminho)):
    x.append(listaDeCidades[menor.caminho[i] - 1].coordenadaX)
    y.append(listaDeCidades[menor.caminho[i] - 1].coordenadaY)


plt.plot(x,y,'ro')
plt.plot(x,y)
plt.show()




#--TESTE--
# pai1 = [1,2,3,4,5,6,7,8,9]
# pai2 = [9,3,7,8,2,6,5,1,4]
#
# resultado = algoritmo.crossoverPMX(2, 7, pai1, pai2)
# algoritmo.crossoverAPX(pai1, pai2)
# algoritmo.mutacaoBaseadaEmPosicao(pai1)
# algoritmo.mutacaoInversao(pai1)
# print(resultado[0].caminho)
# print(resultado[1].caminho)


