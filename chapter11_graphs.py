from chapter6_stack import Stack


class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adjacents = []

    
    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)


    def show_adjacents(self):
        for adjacent in self.adjacents:
            print(f'adjacent label: {adjacent.vertex.label} | adjacent cost: {adjacent.cost}')


class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost


class CitiesOfRomaniaGraphExample:
    arad = Vertex(label='Arad')
    zerind = Vertex(label='Zerind')
    oradea = Vertex(label='Oradea')
    sibiu = Vertex(label='Sibiu')
    timisoara = Vertex(label='Timisoara')
    lugoj = Vertex(label='Lugoj')
    mehadia = Vertex(label='Mehadia')
    dobreta = Vertex(label='Dobreta')
    craiova = Vertex(label='Craiova')
    rimnicu = Vertex(label='Rimnicu')
    fagaras = Vertex(label='Fagaras')
    pitesti = Vertex(label='Pitesti')
    bucharest = Vertex(label='Bucharest')
    giurgiu = Vertex(label='Giurgiu')

    arad.add_adjacent(adjacent=Adjacent(vertex=zerind, cost=75))
    arad.add_adjacent(adjacent=Adjacent(vertex=sibiu, cost=140))
    arad.add_adjacent(adjacent=Adjacent(vertex=timisoara, cost=118))

    zerind.add_adjacent(adjacent=Adjacent(vertex=arad, cost=75))
    zerind.add_adjacent(adjacent=Adjacent(vertex=oradea, cost=71))

    oradea.add_adjacent(adjacent=Adjacent(vertex=zerind, cost=71))
    oradea.add_adjacent(adjacent=Adjacent(vertex=sibiu, cost=151))

    sibiu.add_adjacent(adjacent=Adjacent(vertex=oradea, cost=151))
    sibiu.add_adjacent(adjacent=Adjacent(vertex=arad, cost=140))
    sibiu.add_adjacent(adjacent=Adjacent(vertex=fagaras, cost=99))
    sibiu.add_adjacent(adjacent=Adjacent(vertex=rimnicu, cost=80))

    timisoara.add_adjacent(adjacent=Adjacent(vertex=arad, cost=118))
    timisoara.add_adjacent(adjacent=Adjacent(vertex=lugoj, cost=111))

    lugoj.add_adjacent(adjacent=Adjacent(vertex=timisoara, cost=111))
    lugoj.add_adjacent(adjacent=Adjacent(vertex=mehadia, cost=70))

    mehadia.add_adjacent(adjacent=Adjacent(vertex=lugoj, cost=70))
    mehadia.add_adjacent(adjacent=Adjacent(vertex=dobreta, cost=75))

    dobreta.add_adjacent(adjacent=Adjacent(vertex=mehadia, cost=75))
    dobreta.add_adjacent(adjacent=Adjacent(vertex=craiova, cost=120))

    craiova.add_adjacent(adjacent=Adjacent(vertex=dobreta, cost=120))
    craiova.add_adjacent(adjacent=Adjacent(vertex=pitesti, cost=138))
    craiova.add_adjacent(adjacent=Adjacent(vertex=rimnicu, cost=146))

    rimnicu.add_adjacent(adjacent=Adjacent(vertex=craiova, cost=146))
    rimnicu.add_adjacent(adjacent=Adjacent(vertex=sibiu, cost=80))
    rimnicu.add_adjacent(adjacent=Adjacent(vertex=pitesti, cost=97))

    fagaras.add_adjacent(adjacent=Adjacent(vertex=sibiu, cost=99))
    fagaras.add_adjacent(adjacent=Adjacent(vertex=bucharest, cost=211))

    pitesti.add_adjacent(adjacent=Adjacent(vertex=rimnicu, cost=97))
    pitesti.add_adjacent(adjacent=Adjacent(vertex=craiova, cost=138))
    pitesti.add_adjacent(adjacent=Adjacent(vertex=bucharest, cost=101))

    bucharest.add_adjacent(adjacent=Adjacent(vertex=fagaras, cost=211))
    bucharest.add_adjacent(adjacent=Adjacent(vertex=pitesti, cost=101))
    bucharest.add_adjacent(adjacent=Adjacent(vertex=giurgiu, cost=90))


class InDepthSearch:
    def __init__(self, start):
        self.start = start
        self.start.visited = True
        self.stack = Stack(size=20, type=object)
        self.stack.push_value(start)

    
    def search(self):
        top = self.stack.top()
        print(f'Top: {top.label}')
        for adjacent in top.adjacents:
            print(f'Stack top: {top.label}. {adjacent.vertex.label} already visited? {adjacent.vertex.visited}')
            if not adjacent.vertex.visited:
                adjacent.vertex.visited = True
                self.stack.push_value(adjacent.vertex)
                print(f'Stacked {adjacent.vertex.label}')
                self.search()
        print(f'Unstacked {self.stack.pop_value_from_the_top().label}')
        print()



romania_cities = CitiesOfRomaniaGraphExample()
romania_cities.arad.show_adjacents()
romania_cities.bucharest.show_adjacents()
stack = Stack(size=5, type=object)
stack.push_value(romania_cities.arad)
stack.push_value(romania_cities.sibiu)
stack.push_value(romania_cities.timisoara)
print(stack.top().label)
print(stack.pop_value_from_the_top().label)
in_depth_search = InDepthSearch(start=romania_cities.arad)
in_depth_search.search()