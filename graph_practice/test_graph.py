import sys

from graph import Graph


# pytest
def test_create_graph():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {},
		"D": {}
		}
	g = Graph(d)

	assert g.adj_list == d
	assert g.get_num_edges() == 3
	assert g.get_num_vertices() == 4

def test_get_edges():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {},
		"D": {}
	}
	g = Graph(d)

	assert g.get_edges("A") == d["A"]
	assert g.get_edges("C") == d["C"]

def test_has_edge():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {},
		"D": {}
	}
	g = Graph(d)

	assert g.has_edge("A", "B")
	assert not g.has_edge("A", "D")

def test_get_weight():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {},
		"D": {}
	}
	g = Graph(d)

	assert g.get_weight("A", "B") == 1
	assert g.get_weight("B", "A") == -1

def test_dfs():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"D": 3},
		"C": {"D": 4},
		"D": {}
	}
	g = Graph(d)

	assert g.dfs() == ["A", "B", "D", "C"]

def test_bfs():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"D": 3},
		"C": {"D": 4},
		"D": {}
	}
	g = Graph(d)

	assert g.bfs() == ["A", "B", "C", "D"]

def test_is_connected():
	# test connected graph
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"D": 3},
		"C": {"D": 4},
		"D": {}
	}
	g = Graph(d)

	assert g.is_connected()

	# test unconnected graph
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"C": 3},
		"C": {"B": 4},
		"D": {}
	}
	g = Graph(d)

	assert not g.is_connected()

def test_djikstra():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"D": 3},
		"C": {"D": 4},
		"D": {}
	}
	g = Graph(d)
	resA = {
		"A": 0,
		"B": 1,
		"C": 2,
		"D": 4
	}

	assert g.djikstra("A") == resA

	resD = {
		"A": sys.maxsize,
		"B": sys.maxsize,
		"C": sys.maxsize,
		"D": 0
	}

	assert g.djikstra("D") == resD

def test_djikstra_heap():
	d = {
		"A": {"B": 1, "C": 2},
		"B": {"D": 3},
		"C": {"D": 4},
		"D": {}
	}
	g = Graph(d)
	resA = {
		"A": 0,
		"B": 1,
		"C": 2,
		"D": 4
	}

	assert g.djikstra_heap("A") == resA

	resD = {
		"A": sys.maxsize,
		"B": sys.maxsize,
		"C": sys.maxsize,
		"D": 0
	}

	assert g.djikstra_heap("D") == resD
