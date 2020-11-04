import abc
from collections import defaultdict
import numpy as np

#######################################################################
#
# The base class representation of a Graph with all the interface
# methods
#
#######################################################################


class Graph(abc.ABC):

	def __init__(self, numVertices, directed=False):
		self.numVertices = numVertices
		self.directed = directed

	@abc.abstractmethod
	def add_edge(self, v1, v2, weight):
		pass

	@abc.abstractmethod
	def get_adjacent_vertices(self, v):
		pass

	@abc.abstractmethod
	def get_indegree(self, v):
		pass

	@abc.abstractmethod
	def get_edge_weight(self, v1, v2):
		pass

	@abc.abstractmethod
	def display(self):
		pass


#######################################################################
#
# A single node in a graph represented by an adjacency set. Every node
# has a vertex id
# Each node is associated with a set of adjacent vertices
#
#######################################################################

class Node:
	def __init__(self, vertexId):
		self.vertexId = vertexId
		self.adjacency_set = set()

	def add_edge(self, v):
		self.adjacency_set.add(v)

	def get_adjacent_vertices(self):
		return self.adjacency_set

	def __hash__(self):
		return hash(frozenset(self.vertexId))

	def __str__(self):
		return "id="+str(self.vertexId)
	
	def __eq__(self, other):
		if not isinstance(other, Node):
			return False

		return (set(self.vertexId) == set(other.vertexId))

	

class AdjacencySetGraph(Graph):
	
	def __init__(self, numVertices, directed=False):
		super(AdjacencySetGraph, self).__init__(numVertices, directed)

		self.vertex_list={}

	def add_edge(self, v1, v2, weight=1):
		if weight != 1:
			raise ValueError("An adjacency set cannot represent edge weights >1")

		if not v1.vertexId in self.vertex_list:
    			self.vertex_list[v1.vertexId]=v1

		self.vertex_list[v1.vertexId].add_edge(v2)
		if self.directed == False:
			if not v2.vertexId in self.vertex_list:
				self.vertex_list[v2.vertexId]=v2
				
			self.vertex_list[v2.vertexId].add_edge(v1)


	def get_adjacent_vertices(self, v):
		return self.vertex_list[v.vertexId].get_adjacent_vertices()

	def get_indegree(self, v):
		indegree=0
		for i in self.vertex_list.keys():
			if v in self.get_adjacent_vertices(self.vertex_list[i]):
				indegree=indegree + 1

		return indegree

	def get_edge_weight(self, v1, v2):
		return 1

	def display(self):
		for i in self.vertex_list.keys():
			for v in self.get_adjacent_vertices(self.vertex_list[i]):
				print(self.vertex_list[i], "-->", v)


#######################################################################
#
# Represents a graph as an adjacency matrix. A cell in the matrix has
# a value when there exists an edge between the vertex represented by
# the row and column numbers.
# Weighted graphs can hold values > 1 in the matrix cells
# A value of 0 in the cell indicates that there is no edge
#
#######################################################################
class AdjacencyMatrixGraph(Graph):

	def __init__(self, numVertices, directed=False):
		super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

		self.matrix=np.zeros((numVertices, numVertices))

	def add_edge(self, v1, v2, weight=1):
		if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
			raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

		if weight < 1:
			raise ValueError("An edge cannot have weight < 1")

		self.matrix[v1][v2]=weight
		if self.directed == False:
			self.matrix[v2][v1]=weight

	def get_adjacent_vertices(self, v):
		if v < 0 or v >= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)

		adjacent_vertices=[]
		for i in range(self.numVertices):
			if self.matrix[v][i] > 0:
				adjacent_vertices.append(i)

		return adjacent_vertices

	def get_indegree(self, v):
		if v < 0 or v >= self.numVertices:
			raise ValueError("Cannot access vertex %d" % v)

		indegree=0
		for i in range(self.numVertices):
			if self.matrix[i][v] > 0:
				indegree=indegree + 1

		return indegree

	def get_edge_weight(self, v1, v2):
		return self.matrix[v1][v2]

	def display(self):
		for i in range(self.numVertices):
			for v in self.get_adjacent_vertices(i):
				print(i, "-->", v)


# g = AdjacencySetGraph(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(2, 3)

# for i in range(4):
#     print("Adjacent to: ", i, g.get_adjacent_vertices(i))

# for i in range(4):
#      print("Indegree: ", i, g.get_indegree(i))

# for i in range(4):
#     for j in g.get_adjacent_vertices(i):
#        print ("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

# g.display()
