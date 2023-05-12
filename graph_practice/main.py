from graph import Graph


# python main.py
def main():
	# any code to help with debugging

	# creating a graph from a dictionary
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {},
		"D": {}
		}
	g = Graph(d)
	# __repr__ is overwritten in Graph class to format printing
	print(g)

	# creating empty graph then generating random vertices and edges
	g_random = Graph()
	g_random.generate_random_graph(num_vertices=5, edge_density=0.5)
	print(g_random)


if __name__ == "__main__":
	main()