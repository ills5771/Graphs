class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist')


def earliest_ancestor(ancestors, starting_id):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    return graph.vertices
    # q = Queue()
    # q.enqueue(starting_id)
    # visited = set()

    # while q.size() > 0:
    #     path = q.dequeue()
    #     v = path[-1]
    #     if v not in visited:
    #         if v == destination_vertex:
    #             return path
    #         visited.add(v)
    #         for n in self.vertices[v]:
    #             copy_path = path.copy()
    #             copy_path.append(n)
    #             q.enqueue(copy_path)
    # return None


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
