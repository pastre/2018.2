from PIL import Image

import heapq

im = Image.open('C:\\Temp\\b.png', 'r')
wdt, hgt = im.size

pxl = im.load()


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]    

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1) 

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

visited = {}

def search (graph, start, goal, algorithm):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            return frontier.elements
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                if algorithm == 'a*':
                    priority = new_cost + heuristic(goal, next)
                elif algorithm == 'dij':    
                    priority = new_cost
                elif algorithm == 'glutty':    
                    priority = heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
                if not current in visited.keys(): visited[current] = 0
                visited[current] += 1
                x, y = current
                pxl[x, y] = (255, 50, 50, int(visited[current]/1000/(sum([i for i in visited.values()]))))

a = GridWithWeights(wdt, hgt)

for x in range(0, wdt):
    for y in range(0, hgt):
        if pxl[x, y] ==  (0, 0, 0, 255):
            a.walls.append((x, y, ))
start, end = (), ()

for x in range(0, wdt):
    if pxl[x, 0] == (255, 255, 255, 255):
        start = (x, 0)
        break

for x in range(0, wdt):
    if pxl[x, wdt - 1] == (255, 255, 255, 255):
        end = (x, wdt - 1)
        break
if end == ():
    for x in range(0, wdt):
        if pxl[wdt - 1, x] == (255, 255, 255, 255):
            print('Found end')
            end = (wdt - 1, x)
            break

if end == ():
    for x in range(0, wdt):
        if pxl[0, x] == (255, 255, 255, 255):
            print('Found end')
            end = (wdt - 1, 0)
            break
if end == ():
    for x in range(wdt, 0, -1):
         if pxl[x - 1, 0] == (255, 255, 255, 255):
            print('Found end')
            end = (0, x)
            break
print(f'Start is {start} end is {end}')
r = search(a, start, end, 'glutty')


for element in r:
    _, tmp= element
    x, y  = tmp
    pxl[x, y] = (0, 255, 0, 100)
print(r)

im.show()
