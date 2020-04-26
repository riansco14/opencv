import random


class Neuronio:
    def __init__(self, numEntradas):
        self.numEntradas = numEntradas
        self.pesos = []
        for i in range(numEntradas):
            self.pesos.append(random.random())
        self.pesos.insert(0, 1)
        self.rateAprendizado = 0.2

    def activation(self, sum):
        if sum >= 0:
            return 1
        else:
            return 0

    def calcSaida(self, entrada):
        sum = 0
        for i in range(self.numEntradas):
            sum = sum + entrada[i] * self.pesos[i]
        return sum

    def printNeuron(self, entrada, saidaEsperada, saida):
        print("Entrada: ", entrada, "|| Pesos: ", self.pesos,
              "|| Saída Esperada: ", saidaEsperada, " ", saida)


entradas = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2],
				[0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
saidas = [1, 0, 0, 1]
#
for entrada in entradas:
    entrada.insert(0, -1)

numElementos = len(entradas[0])
neuron = Neuronio(numElementos)

while True:
    erro = False
    for i in range(len(entradas)):
        sum = neuron.calcSaida(entradas[i])
        y = neuron.activation(sum)
        print(neuron.printNeuron(entradas[i], saidas[i], y))
        # Corrigir erro
        if y != saidas[i]:
            erro_aux = saidas[i] - y
            for j in range(len(entradas[i])):
                neuron.pesos[j] = neuron.pesos[j] + neuron.rateAprendizado * erro_aux * entradas[i][j]
            erro = True
    if not erro:
        break
