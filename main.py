import heapq
import time
import sys

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}
        
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'D', 3)
graph.add_edge('A', 'C', 10)
graph.add_edge('D', 'C', 7)
# graph.add_edge('A', 'D', 3)


print(graph.vertices)

start_time = time.time()
print(graph.dijkstra('A'))
end_time = time.time()
run_time = end_time - start_time
print(f"Time to completion was {run_time:.7f} seconds.")
print(f"Size of return is {sys.getsizeof(graph.dijkstra('A'))} bytes")