from scipy import spatial as sp
import numpy

def calcularPesos(vertices, caminho):
    arestas = []

    for i in range(numpy.size(caminho) - 1):
        v1 = vertices[caminho[i] - 1]
        v2 = vertices[caminho[i + 1] - 1]

        arestas.append(euclideanNorm(v1.coordenadaX, v2.coordenadaX, v1.coordenadaY, v2.coordenadaY))

    return arestas

def euclideanNorm(x1, x2, y1, y2):
    pontoA = []
    pontoB = []

    pontoA.append(x1)
    pontoA.append(y1)
    pontoB.append(x2)
    pontoB.append(y2)

    return sp.distance.euclidean(pontoA, pontoB)

def custo(vertices, caminho):
    pesos = calcularPesos(vertices, caminho)

    return sum(pesos)

def crossOverPMX(caminho1, caminho2):

    posicao1 = 5
    posicao2 = 15
