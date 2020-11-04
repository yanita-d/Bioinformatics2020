from queue import Queue

from graph import *


def build_distance_table(graph, source):
    # A dictionary mapping from the vertex number to a tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}

    for i in graph.vertex_list:
        distance_table[graph.vertex_list[i]] = (None, None)

    # The distance to the source from itself is 0
    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        # The distance of the current vertex from the source
        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # Only update the distance table if no current distance from
            # the source is set
            print(neighbor)
            if distance_table.get(neighbor)[0] is None:
                distance_table[neighbor] = (1 + current_distance, current_vertex)

                # Enqueue the neighbor only if it has other adjacent vertices
                # to explore
                if len(neighbor.get_adjacent_vertices()) > 0:
                    queue.put(neighbor)

    return distance_table


def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)

    path = [str(destination)]

    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [str(previous_vertex)] + path

        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print("There is no path from %s to %s" % (source, destination))
    else:
        path = [str(source)] + path
        print("Shortest path is: ", path)


# g = AdjacencySetGraph(8, directed=True)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 3)
# g.add_edge(1, 4)
# g.add_edge(3, 5)
# g.add_edge(5, 4)
# g.add_edge(3, 6)
# g.add_edge(6, 7)
# g.add_edge(0, 7)

# shortest_path(g, 0, 5)
# shortest_path(g, 0, 6)
# shortest_path(g, 7, 4)
