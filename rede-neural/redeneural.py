import random
import numpy as np


class Neuronio:
    def __init__(self, numEntradas, indexCamada, indexNeuronio, bias=1):
        self.numEntradas = numEntradas
        self.pesos = []
        for i in range(numEntradas):
            self.pesos.append(random.random())
        self.pesos.insert(0, bias)
        self.rateAprendizado = 0.2
        self.indexCamada = indexCamada
        self.indexNeuronio = indexNeuronio
        self.saida=-9999


    def activation(self, x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

    def activationDerivate(self, sum):
        return 1-self.activation(sum)**2

    def calcSaida(self, entrada):
        sum = 0
        for i in range(self.numEntradas):
            sum = sum + entrada[i] * self.pesos[i]
        return sum

    def ativarNeuronio(self, entrada):
        self.saida=self.activation(self.calcSaida(entrada))
        self.printNeuronSaida(entrada)
        return self.saida

    def printNeuronSaida(self, entrada):
        print("Entrada: ", entrada, "|| Pesos: ", self.pesos,
              "|| Saída: ", " ", self.saida)

    def printNeuron(self):
        print("Camada: ", self.indexCamada, "Neuronio: ", self.indexNeuronio,"|| Pesos: ", self.pesos)

def neuroniosSaida(camada):
    entradas=[]
    for neuronio in camada:
        entradas.append(neuronio.saida)
    entradas.insert(0, -1)
    return entradas

def criarRedeNeural(numCamadas, numNeuronios, numElementosEntrada):
    camadas = list()
    # Criar Camada
    for i in range(numCamadas):
        neuronios = list()
        # Adicionar Neuronios
        for j in range(numNeuronios):
            if i == 0:
                neuronios.append(Neuronio(numElementosEntrada, i, j))
                break
            elif i == numCamadas - 1:
                neuronios.append(Neuronio(len(camadas[i - 1]), i, j))
                break
            else:
                neuronios.append(Neuronio(len(camadas[i - 1]), i, j))

        camadas.append(neuronios)
    return camadas


entradas = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2],
            [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
saidas = [1, 0, 0, 1]

for entrada in entradas:
    entrada.insert(0, -1)

numCamadas = 3
numNeuronios = 2
numElementosEntrada = len(entradas[0])

redeneural = criarRedeNeural(numCamadas, numNeuronios, numElementosEntrada)

for indexEntrada in range(1):
    for indexCamada in range(len(redeneural)):
        for neuronio in redeneural[indexCamada]:
            if indexCamada==0:
                neuronio.printNeuron()
                neuronio.ativarNeuronio(entradas[indexEntrada])
            else:
                neuronio.printNeuron()
                neuronio.ativarNeuronio(neuroniosSaida(redeneural[indexCamada-1]))

    for indexCamada in reversed(range(len(redeneural))):
        for neuronio in redeneural[indexCamada]:
            if indexCamada == len(redeneural)-1:
                print(indexCamada)
                for indexPeso in range(len(neuronio.pesos)):
                    somaAnterior=0
                    neuronio.pesos[indexPeso]+=-(neuronio.saida-saidas[indexEntrada])*(1)*entradas[indexEntrada][indexPeso]
            else:
                neuronio.pesos[indexPeso] +=(1)
        pass
