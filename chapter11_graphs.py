from chapter6_circular_queue import CircularQueue
from chapter6_stack import Stack
from chapter5_sorted_arrrays import SortedArray


class Vertex:
    def __init__(self, label, destination_distance=None):
        self.label = label
        self.visited = False
        self.destination_distance = destination_distance
        self.adjacents = []

    
    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)


    def show_adjacents(self):
        for adjacent in self.adjacents:
            print(f'adjacent label: {adjacent.vertex.label} | adjacent cost: {adjacent.cost}')


class Adjacent:
    def __init__(self, vertex, cost = 0):
        self.vertex = vertex
        self.cost = cost
        self.a_star_distance = 0
        if self.vertex.destination_distance and self.cost:
            self.a_star_distance = self.vertex.destination_distance + self.cost



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


class CitiesOfRomaniaStraightLineDistanceGraphExample:
    arad = Vertex(label='Arad', destination_distance=366)
    zerind = Vertex(label='Zerind', destination_distance=374)
    oradea = Vertex(label='Oradea', destination_distance=380)
    sibiu = Vertex(label='Sibiu', destination_distance=253)
    timisoara = Vertex(label='Timisoara', destination_distance=329)
    lugoj = Vertex(label='Lugoj', destination_distance=244)
    mehadia = Vertex(label='Mehadia', destination_distance=241)
    dobreta = Vertex(label='Dobreta', destination_distance=242)
    craiova = Vertex(label='Craiova', destination_distance=160)
    rimnicu = Vertex(label='Rimnicu', destination_distance=193)
    fagaras = Vertex(label='Fagaras', destination_distance=178)
    pitesti = Vertex(label='Pitesti', destination_distance=98)
    bucharest = Vertex(label='Bucharest', destination_distance=0)
    giurgiu = Vertex(label='Giurgiu', destination_distance=77)

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


class WidthForceSearch:

    def __init__(self, start):
        self.start = start
        self.start.visited = True
        self.queue = CircularQueue(20)
        self.queue.line_up(start)


    def search(self):
        first = self.queue.first()
        print()
        print(f'First: {first.label}')
        temp = self.queue.dequeue()
        print(f'{temp.label} dequeued')
        for adjacent in first.adjacents:
            print(f'First was {temp.label}. Was {adjacent.vertex.label} visited? {adjacent.vertex.visited}')
            if not adjacent.vertex.visited:
                adjacent.vertex.visited = True
                self.queue.line_up(adjacent.vertex)
                print(f'Lined up: {adjacent.vertex.label}')
        if self.queue.number_of_elements > 0:
            self.search()


class GreedySearch:

    class SortedArray(SortedArray):

        def insert(self, value):
            if self.last_position == self.size - 1: #O(1)
                print("Array is full")
            else:
                position = 0
                for i in range(self.last_position + 1): #O(n)
                    position = i
                    if self.values[i].destination_distance > value.destination_distance:
                        break
                    if i == self.last_position:
                        position = i + 1    
                x = self.last_position
                while x >= position:    
                    self.values[x + 1] = self.values[x]
                    x -= 1
                self.values[position] = value
                self.last_position += 1


        def print_values(self):
            if self.last_position == -1:
                print("Array is empty")
            else:
                for i in range(self.last_position + 1):
                    print(i, " - ", self.values[i].label, " - ", self.values[i].destination_distance)
                print()

    def __init__(self, destination):
        self.destination = destination
        self.found = False


    def search(self, current):
        print()
        print(f'Current: {current.label}')
        current.visited = True
        if current == self.destination:
            self.found = True
        else:
            sorted_array = self.SortedArray(size=len(current.adjacents))
            for adjacent in current.adjacents:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    sorted_array.insert(adjacent.vertex)
            sorted_array.print_values()
            if sorted_array.values[0] is not None:
                self.search(sorted_array.values[0])


class AStarSearch:

    class SortedArray(SortedArray):

        def insert(self, adjacent):
            if self.last_position == self.size - 1: #O(1)
                print("Array is full")
            else:
                position = 0
                for i in range(self.last_position + 1): #O(n)
                    position = i
                    if self.values[i].a_star_distance > adjacent.a_star_distance:
                        break
                    if i == self.last_position:
                        position = i + 1    
                x = self.last_position
                while x >= position:    
                    self.values[x + 1] = self.values[x]
                    x -= 1
                self.values[position] = adjacent
                self.last_position += 1


        def print_values(self):
            if self.last_position == -1:
                print("Array is empty")
            else:
                for i in range(self.last_position + 1):
                    print(
                        i, 
                        " - ", 
                        self.values[i].vertex.label, 
                        " - ",
                        self.values[i].cost,
                        " - ", 
                        self.values[i].vertex.destination_distance,
                        " - ",
                        self.values[i].a_star_distance
                    )
                print()

    
    def __init__(self, destination):
        self.destination = destination
        self.found = False


    def search(self, current):
        print()
        print(f'Current: {current.label}')
        current.visited = True
        if current == self.destination:
            self.found = True
        else:
            sorted_array = self.SortedArray(len(current.adjacents))
            for adjacent in current.adjacents:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    sorted_array.insert(adjacent)
            sorted_array.print_values() 
            if sorted_array.values[0]:
                self.search(sorted_array.values[0].vertex)

        
romania_cities = CitiesOfRomaniaGraphExample()
romania_cities_straight_line_distance = CitiesOfRomaniaStraightLineDistanceGraphExample()

def in_depth_search_example():
    stack = Stack(size=5, type=object)
    stack.push_value(romania_cities.arad)
    stack.push_value(romania_cities.sibiu)
    stack.push_value(romania_cities.timisoara)
    print(stack.top().label)
    print(stack.pop_value_from_the_top().label)
    in_depth_search = InDepthSearch(start=romania_cities.arad)
    in_depth_search.search()


def width_force_search_sample_test(self):
    queue = CircularQueue(20)
    queue.line_up(romania_cities.arad)
    queue.line_up(romania_cities.bucharest)
    queue.line_up(romania_cities.fagaras)
    print(queue.first().label)
    print(queue.dequeue().label)
    print(queue.first().label)


def width_force_search_example():
    width_force_search_test = WidthForceSearch(start=romania_cities.arad)
    width_force_search_test.search()


def greedy_search_sample_test():
    array = GreedySearch.SortedArray(5)
    array.insert(romania_cities_straight_line_distance.arad)
    array.insert(romania_cities_straight_line_distance.craiova)
    array.insert(romania_cities_straight_line_distance.bucharest)
    array.insert(romania_cities_straight_line_distance.dobreta)
    array.print_values()
    array.insert(romania_cities_straight_line_distance.lugoj)
    array.print_values()


def greedy_search_example():
    greedy_search = GreedySearch(romania_cities_straight_line_distance.bucharest)
    greedy_search.search(romania_cities_straight_line_distance.arad)


def a_star_search_sample_test():
    array = AStarSearch.SortedArray(3)
    array.insert(romania_cities_straight_line_distance.arad.adjacents[0])
    array.insert(romania_cities_straight_line_distance.arad.adjacents[1])
    array.insert(romania_cities_straight_line_distance.arad.adjacents[2])
    array.print_values()


def a_star_search_example():
    a_star_search = AStarSearch(destination=romania_cities_straight_line_distance.bucharest)
    a_star_search.search(romania_cities_straight_line_distance.arad)

a_star_search_example()
