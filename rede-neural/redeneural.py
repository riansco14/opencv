import random
from math import exp

import numpy as np


class Neuronio:
    def __init__(self, numEntradas, indexCamada, indexNeuronio, bias=1):
        self.numEntradas = numEntradas
        self.pesos = []
        for i in range(numEntradas):
            self.pesos.append(random.random())
        # self.pesos.insert(0, bias)
        self.rateAprendizado = 0.2
        self.indexCamada = indexCamada
        self.indexNeuronio = indexNeuronio
        self.saida=-9999
        self.erro=None

    #sigmoid
    def activation(self, sum):
        return 1.0 / (1.0 + exp(-sum))

    def activationDerivate(self, sum):
        return sum * (1.0 - sum)

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
        print("Camada: ", self.indexCamada, "Neuronio: ", self.indexNeuronio,"|| Pesos: ", self.pesos, "|| Erro: ",self.erro)

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
                print("criando", numElementosEntrada)
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
    #feedfoward
    for indexCamada in range(len(redeneural)):
        for neuronio in redeneural[indexCamada]:
            if indexCamada==0:
                # neuronio.printNeuron()
                neuronio.ativarNeuronio(entradas[indexEntrada])
            else:
                # neuronio.printNeuron()
                neuronio.ativarNeuronio(neuroniosSaida(redeneural[indexCamada-1]))

    #backpropagation
    for indexCamada in reversed(range(len(redeneural))):
        camada=redeneural[indexCamada]

        #se for ultima camada
        if indexCamada == len(redeneural)-1:
            for indexNeuronio in range(len(camada)):
                neuronio = camada[indexNeuronio]
                yE=saidas[indexEntrada]
                y=neuronio.saida
                neuronio.erro=(yE-y) * neuronio.activationDerivate(y)
        #camada intermediaria
        else:
            for indexNeuronio in range(len(camada)):
                # print("rodou a anterior", indexCamada)
                neuronio = camada[indexNeuronio]
                erro=0.0
                for neuronioProximo in redeneural[indexCamada+1]:
                    erro+=(neuronioProximo.pesos[indexNeuronio]*neuronioProximo.erro)
                y = neuronio.saida
                neuronio.erro=erro*neuronio.activationDerivate(y)

        for neuronio in camada:
            neuronio.printNeuron()

    #atualizar pesos e corrigir error
    for indexCamada in range(len(redeneural)):
        camada=redeneural[indexCamada]
        entrada = entradas[indexEntrada]
        if indexCamada != 0:
            entrada=neuroniosSaida(redeneural[indexCamada-1])
        for neuronio in camada:
            for indexPeso in range(len(neuronio.pesos)):
                neuronio.pesos[indexPeso]+=neuronio.rateAprendizado*neuronio.erro*entrada[indexPeso]
            neuronio.printNeuronSaida(entrada)