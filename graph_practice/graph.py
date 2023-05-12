from __future__ import annotations
from typing import List
from random import sample, gauss, randint
import heapq
import sys

class Graph:
	"""
	Simple implementation of a Directed Graph
	Only allows positive edge weights for simplicity
	Adjecentcy list representation stored as a dict of dicts

	Ex:
	d = {
		 "A": {"B": 1, "C":2},
	     "B": {"C": 3},
	     "C": {}
	    }

	Node A has edges of weights 1 and 2 to B and C, respectively. B has one outgoing edge to C and C has none.

	"""

	def __init__(self, d: dict = None):
		self.adj_list = {}
		self.num_vertices = 0
		self.num_edges = 0
		self.vertices = []

		if d:
			self._create_from_dict(d)

	def __repr__(self):
		s = ""
		for v in self.adj_list.keys():
			s += (f"Vertex {v} Edges: ")
			for e in self.adj_list[v].keys():
				s += f"{e}({self.adj_list[v][e]}) "
			s += "\n"
		return s

	def _create_from_dict(self, d):
		self.adj_list = d
		self.num_vertices = len(self.adj_list.keys())
		for v in self.adj_list.keys():
			self.num_edges += len(self.adj_list[v].keys())
		self.vertices = list(d.keys())

	def get_num_vertices(self):
		return self.num_vertices

	def get_num_edges(self):
		return self.num_edges

	def get_vertices(self):
		return self.vertices

	def generate_random_graph(self, num_vertices=5, edge_density=0.5, min_weight=1, max_weight=10):
		"""
		Don't need to worry about this
		Randomly generates a graph given the number of vertices and an edge density

		:param num_vertices: Number of vertices in graph
		:param edge_density: controls how dense a graph is (0 = no edges, 1 = fully connected)
		:param min_weight: smallest weight to randomly generate
		:param max_weight: largets weight to randomly generate
		:return: Nothing; populates existing Graph object
		"""
		d = {}
		edge_mean = num_vertices*edge_density
		for v in range(num_vertices):
			e = {}
			_num_edges = min(int(max(gauss(1, 0.5), 0)*edge_mean), num_vertices)
			_edges = sample(range(num_vertices), _num_edges)
			for _e in _edges:
				e[_e] = randint(min_weight, max_weight+1)
			d[v] = e
		self._create_from_dict(d)


# TODO ##############################################################################################
	def get_edges(self, v: str) -> dict:
		"""
		Finds the edges from a given vertex
		:param v: node
		:return: dict of edges
		"""
		# TODO
		pass

	def has_edge(self, v1: str, v2: str) -> bool:
		"""
		Determines if there is an edge from v1 to v2 in the graph
		:param v1: source vertex
		:param v2: destination vertex
		:return: True if there is an edge from v1 to v2 else false
		"""
		# TODO
		pass

	def get_weight(self, v1: str, v2: str) -> int:
		"""
		Returns the weight of edge from v1 to v2 if it exists else -1
		:param v1: source vertex
		:param v2: destination vertex
		:return: integer weight
		"""
		# TODO
		pass

	def dfs(self, v: str = None) -> List[str]:
		"""
		Depth first search wrapper function. Implemented in _dfs() recursively.
		No need to update this function
		:param v: starting node; if none, take first available
		:return: list of vertices in the order they are visited
		"""
		visited = []
		if not v:
			v = list(self.adj_list.keys())[0]
		self._dfs(v, visited)
		return visited

	def _dfs(self, v: str, visited: List[str]):
		"""
		Recursive helper function for DFS
		:param v: current vertex
		:param visited: list of visited nodes
		:return:
		"""
		# TODO
		pass

	def bfs(self, v: str = None) -> List[str]:
		"""
		Breadth-first search (BFS).
		:param v: optional starting node
		:return: list of vertices in the order they are visited
		"""
		visited = []
		if not v:
			v = list(self.adj_list.keys())[0]

		# TODO
		pass

	def transpose_graph(self) -> Graph:
		"""
		Creates the transpose graph: reverses the direction of all edges
		returns a new graph with the new structure

		Hint: create a new dictionary from existing graph that will be used to create new one
		:return: Transposed graph
		"""
		# TODO
		pass

	def is_connected(self) -> bool:
		"""
		Determines if a graph is connected: there exists a path between all vertices

		Algorithm for Directed Graphs:
		1. create two visited lists initially empty
		2. List1 is created from DFS on an arbitrary node
		3. List2 is created by running DFS on the same starting node of the transposed graph
		4. If any vertex in the original graph does not show up in one of the lists, then graph is not connected

		Note: for undirected graphs just need one DFS. Why do we need transpose for directed graphs?

		https://www.geeksforgeeks.org/check-if-a-directed-graph-is-connected-or-not/
		:return: True if connected else false
		"""
		# TODO
		pass

	def djikstra(self, source) -> dict:
		"""
		Djikstra's algorithm to calculate distance between source node and all others
		Greedy algorithm that keeps track of distances to the source node that are updated if a shorter path is
		encountered
		Once a node is "visited", it will never be considered again since the greedy approach means it must be the
		smallest value to get there

		Idea:
		- mark all nodes as unvisited (or use an empty set to track visited nodes)
		- use a data structure to keep track of distances (dict can be used here)
		- initialize all distances to "infinity" (sys.maxsize) to start with; set source node to 0
		- loop and choose the node with the smallest distance (mark this as visited)
		(only consider unvisited nodes)
		- iterate through nodes that current one is connected to; update distances only if new path is shorter
		(only unvisited nodes are considered here since we can't improve upon visited ones)
		- repeat until all are visited or only remaining nodes are unconnected

		https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
		Notes:
		- this function can use a dict or list to store distances and find max
		- use sys.maxsize to represent infinity
		- there are a couple of stopping conditions: all nodes visited and only unconnected nodes remaining

		:param source: source node to find distances to all others
		:return: dict of distances from source node
		"""
		# TODO
		pass

	def djikstra_heap(self, source) -> dict:
		"""
		Djikstra's algorithm to calculate distance between source node and all others
		Use a priority queue (min heap) to improve computational complexity when finding
		the next vertex to visit
		Same approach as above except with a different data structure that can improve performance

		Notes:
		- use Python's heapq to find next vertex to visit
		- use sys.maxsize to represent infinity
		- Stopping conditions are slightly different when using a priority queue

		:param source: source node to find distances to all others
		:return: dict of distances from source node
		"""
		# TODO
		pass