from collections import defaultdict
from collections import deque

class Graph(object):
    def __init__(self, graph_dict=defaultdict(list)):
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge, add_reversed=True):
        vertex1, vertex2 = edge
        self.graph_dict[vertex1].append(vertex2)
        if add_reversed:
            self.graph_dict[vertex2].append(vertex1)

    def remove_vertex(self, vertex_to_remove):
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                self.graph_dict[vertex].remove(vertex_to_remove)

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)

    def isolated_vertices(self):
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def __str__(self):
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())

    def neighbours(self,vertex):
        return self.graph_dict[vertex]



def breadth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):

    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return []
    visited = {starting_vertex}
    queue = deque([[starting_vertex]])
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        vertex_list = queue.popleft()
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
        for neighbour in graph.neighbours(vertex_to_expand):
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                queue.append(vertex_list + [neighbour])
        if verbose:
            print()

def generate_Graph_and_search(graph, Xn, Yn, Zn, C1, C2, C3):
    start_node=(Xn,Yn,Zn)
    graph.add_vertex(start_node)
    if Xn==1:
        return start_node

    poseteni={start_node}
    navigator=deque([start_node])

    while navigator:
        nav = navigator.popleft()
        Xn, Yn, Zn = nav

        if Yn < C2:
            if (C2 - Yn) >= Xn:
                node = (0, Yn + Xn, Zn)
            elif (C2 - Yn) < Xn:
                node = (Xn - (C2 - Yn), Yn + (C2 - Yn), Zn)
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn < C3:
            if (C3 - Zn) >= Xn:
                node = (0, Yn, Zn + Xn)
            elif (C3 - Zn) < Xn:
                node = (Xn - (C3 - Zn), Yn, Zn + (C3 - Zn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Xn != 0:
            node = (0, Yn, Zn)
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Xn != C1:
            node = (C1, Yn, Zn)
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

        if Xn < C1:
            if (C1 - Xn) >= Yn:
                node = (Yn + Xn, 0, Zn)
                if node==(1,0,0):
                    break
            elif (C1 - Xn) < Yn:
                node = (Xn + (C1 - Xn), Yn - (C1 - Xn), Zn)
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn < C3:
            if (C3 - Zn) >= Yn:
                node = (Xn, 0, Zn + Yn)
            elif (C3 - Zn) < Yn:
                node = (Xn, Yn - (C3 - Zn), Zn + (C3 - Zn))
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn != 0:
            node = (Xn, 0, Zn)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn != C2:
            node = (Xn, C2, Zn)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

        if Xn < C1:
            if (C1 - Xn) >= Zn:
                node = (Xn + Zn, Yn, 0)
                if node==(1,0,0):
                    break
            elif (C1 - Xn) < Zn:
                node = (Xn + (C1 - Xn), Yn, Zn - (C1 - Xn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn < C2:
            if (C2 - Yn) >= Zn:
                node = (Xn, Yn + Zn, 0)
                if node==(1,0,0):
                    break
            elif (C2 - Yn) < Zn:
                node = (Xn, Yn + (C2 - Yn), Zn - (C2 - Yn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn != 0:
            node = (Xn, Yn, 0)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn != C3:
            node = (Xn, Yn, C3)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

    if node not in poseteni:
        poseteni.add(node)
        graph.add_vertex(node)
        graph.add_edge((node, nav))
        navigator.append(node)
    fastest_path=breadth_first_search_find_path(graph,start_node,(1,0,0),True)
    return fastest_path

graph=Graph()
c1=5
c2=8
c3=10
x=0
y=0
z=0
listazapat=generate_Graph_and_search(graph,x,y,z,c1,c2,c3)


