import random
import time
import heapq
import math
vertices = []
entradaDeDados = []
sequenciaDePassos = []
population = []
crosses = []
sPopulation = 10
tries = 0
hasImprooved = True

class Vertex:
    def __init__(self, n, x, y):
      self.n = n
      self.x = x
      self.y = y
class Resolve:
    path = []
    aptd = -1	# Aptidao

    def __lt__(self, other):
        return self.coast() < other.coast()

    def coast(self):	# Funcao custo
        global vertices
        if (self.aptd == -1):
            s = 0
            for i in range(conjSize - 1):
                v1 = vertices[self.path[i] - 1]
                v2 = vertices[self.path[i + 1] - 1]
                s += math.sqrt(((v1.x - v2.x) ** 2) +
                                  ((v1.y - v2.y) ** 2))
            v1 = vertices[self.path[0] - 1]
            v2 = vertices[self.path[conjSize - 1] -1]
            s += math.sqrt(((v1.x - v2.x) ** 2) +
                              ((v1.y - v2.y) ** 2))
            self.aptd = s
        return self.aptd

conjSize = int(input())
for i in range(conjSize):
    entrada = input()
    entradaDeDados.append(entrada)
for i in range(conjSize):
    vList = entradaDeDados[i].split()
    print(vList)
    vertice = Vertex(int(vList[0]), float(vList[1]), float(vList[2]))
    vertices.append(vertice)
for i in range(1, conjSize + 1):
    sequenciaDePassos.append(i)

def populate():
    global population
    
    for i in range(sPopulation):
        res = Resolve()
        res.path = sequenciaDePassos[:]
        random.shuffle(res.path)
        heapq.heappush(population, res)
        
    return population
    
def defineRoute(_population):
    vRandom1 = random.randrange(sPopulation//2)
    vRandom2 = random.randrange(sPopulation//2)

    if _population[vRandom1].coast() < _population[vRandom2].coast():
        return _population[vRandom1].path
    else:
        return _population[vRandom2].path

def cross(resA, resB):
    global sPopulation
    global conjSize
    
    crosses = []
    n = 0
    nGenerations = int(sPopulation * 0.8)
    ncut = int(conjSize * 0.95)
    while n < nGenerations:

        new_path = resA[:ncut]
        nAdded = 0
        for i in resB:
            if nAdded == (conjSize - ncut):
                break
            if i not in new_path:
                new_path.append(i)
                nAdded += 1

        new_path = mutacaoCaminho(new_path) #Mutação
        cross = Resolve()
        cross.path = new_path
        cross = buscaLocal(cross) #Busca Local - First Improvement
        crosses.append(cross)
        n += 1

    return crosses
    
def mutacaoCaminho(path):
    p1 = random.randrange(conjSize - 1)
    p2 = random.randrange(p1, conjSize - 1)
    path[p1], path[p2] = path[p2], path[p1]
    return path
    
def genNegihbour(path, i):
    path = path[:]
    (path[i], path[i +1]) = (path[i +1], path[i])
    return path

def buscaLocal(cross):
    i = 0
    neighbour = Resolve()
    for i in range(conjSize//2):
        neighbour.path = genNegihbour(cross.path, i)
        if neighbour.coast() < cross.coast():
            cross = neighbour
            break

    return cross

def updatePop(_population, crosses):
    global hasImprooved
    global tries

    for c in crosses:
        M = heapq.nlargest(1, _population)[0]
        m = _population[0]

        _cross = c.coast()
        if (_cross < M.coast()):
            _population.remove(M)
            heapq.heappush(_population, c)
            heapq.heapify(_population)
            
            if (_cross < m.coast()):
                tries = 0
            else:
                tries += 1
        else:
            tries += 1

        if (tries == 700):
            hasImprooved = False

    return _population
        
def getSmallestPop(population):
    return population[0].coast()

population = populate()
while (hasImprooved):
    #Avaliação e Seleção
    resA = defineRoute(population)
    resB = defineRoute(population)

    #Cruzamento
    crosses = cross(resA, resB)

    #Atualização - Elitismo
    population = updatePop(population, crosses)

print(getSmallestPop(population))
