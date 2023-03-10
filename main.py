import json
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# Leitura do json
filename = "./estados.json"
with open(filename) as f:
    estados = json.load(f)["estados"]


# Criação dos vetores auxiliares
siglas = []
fronteiras = {}
for estado in estados:
    sigla = estado['sigla']
    siglas.append(sigla)
    fronteiras[sigla] = estado['fronteiras']
#print(siglas)
#print(fronteiras)

size_estados = len(siglas)

# Criação da Matriz

def criaGrafo(nos, vertices):
    sizeNos = len(nos)
    grafo = [[0 for j in range(sizeNos)] for i in range(sizeNos)]
    for i in range(sizeNos):
        for j in range(sizeNos):
            if nos[i] in vertices[nos[j]]:
                grafo[i][j] = 1
    return grafo

grafo = criaGrafo(siglas, fronteiras)

# Print da matriz no console

def printGrafoConsole(grafo):
    est = "   "
    for i in siglas:
        est += i + " "

    print(est)
    for i, linha in enumerate(grafo):
        print(siglas[i], linha)
printGrafoConsole(grafo)

# Cria Plot do grafo como matriz

def printGrafo(grafo, lableX):
    fig, ax = plt.subplots()
    im = ax.imshow(grafo)

    ax.set_xticks(np.arange(len(grafo[0])), labels=lableX, rotation="vertical")
    ax.set_yticks(np.arange(len(grafo[0])), labels=lableX)

    for i in range(len(grafo[0])):
        for j in range(len(grafo[0])):
            text = ax.text(i, j, grafo[i][j],
                           ha="center", va="center", color="w")

    ax.set_title("Grafo")
    fig.tight_layout()
    plt.show()

printGrafo(grafo, siglas)



# Cria Plot das frequencias dos estados
nun_fronteiras = []
grau_Max = []
grau_Min = []

max_f = -1
min_f = 28

for i in range(size_estados):
    # Contagem da quantidade de fronteiras de cada estado a partir da matriz
    t = 0
    for j in range(size_estados):
        t += grafo[i][j]
    nun_fronteiras.append(t)

    # Define o estados com maior e o com menor quantidade de fronteiras
    if t > max_f:
        grau_Max = []
        grau_Max.append(str(siglas[i]))
        max_f = t
    elif t == max_f:
        grau_Max.append(str(siglas[i]))

    if t < min_f:
        grau_Min = []
        grau_Min.append(str(siglas[i]))
        min_f = t
    elif t == min_f:
        grau_Min.append(str(siglas[i]))


# Grafico Qnt estados X Qnt fronteiras
frequencia = Counter(nun_fronteiras)
plt.bar(frequencia.keys(), frequencia.values(), edgecolor=(0, 0, 0))
plt.title("Frequencia")
plt.xlabel("Qnt fronteiras")
plt.ylabel("Qnt estados")
plt.show()


# Print Max e Min
print("Graus Máximo = ", grau_Max, " fronteiras = ", max_f)
for f in grau_Max:
    print(f, ": ", fronteiras[f])
print("Graus Mínimo = ", grau_Min, " fronteiras = ", min_f)
for f in grau_Min:
    print(f, ": ", fronteiras[f])

# Grafico Qnt de fronteiras x Estado
plt.bar([x for x in range(size_estados)],
        nun_fronteiras,
        0.8,
        edgecolor=(0, 0, 0))

plt.title("Quantidade de fronteiras de cada estado")
plt.ylabel("Qnt fronteiras")
plt.xticks(range(len(siglas)), siglas, rotation="vertical")
plt.show()