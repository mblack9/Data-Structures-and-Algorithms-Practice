from time import time

from graph import Graph


def timer_func(func):
	"""
	Decorator for timing functions
	Decorators are "Syntactic Sugar" that can be added to function definitions to add additional functionality
	automatically
	:param func: function that is passed using the decorator syntax
	:return:
	"""
	def wrap_func(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
		return result

	return wrap_func

@timer_func
def time_djikstra(g: Graph, source: str) -> dict:
	return g.djikstra(source)

@timer_func
def time_djikstra_heap(g: Graph, source: str) -> dict:
	return g.djikstra_heap(source)

# compare run times for the two Djikstra's algorithms with different types of graphs
def main():
	g = Graph()
	g.generate_random_graph(num_vertices=1000, edge_density=0.1)

	res1 = time_djikstra(g, g.get_vertices()[0])
	res2 = time_djikstra_heap(g, g.get_vertices()[0])

	assert res1 == res2


if __name__ == "__main__":
	main()