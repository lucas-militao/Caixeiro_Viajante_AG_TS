import numpy
import AlgoritmoGenetico
import Util

#Lendo arquivo e retirando dados do mesmo
arquivo = open('ncit30.dat')
conteudo = arquivo.readlines()

numeroDeCidades = 0
cidades = []

for i in range(numpy.size(conteudo)):
    cidade = conteudo[i].split()
    cidade = [int(j) for j in cidade]
    if(i != 0):
        cidades.append(Util.Cidade(i, cidade[0], cidade[1]))
    numeroDeCidades = cidade[0]
#-----------------------------------------

variavel = AlgoritmoGenetico.AlgoritmoGenetico(1,1,1,1,1,1,1)