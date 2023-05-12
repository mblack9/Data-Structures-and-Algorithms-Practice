# Graph Practice
The Python code contained here can be used to practice with Directed Graphs. A simple dict-based class is created that uses adjaceny lists as the underlying graph representation. Basic functionality is provided with
additional blank functions that have instructions on how to complete them. Rudimentary unit tests are provided using the Pytest framework which should be expanded upon to test for edge cases and ensure robustness.

*Tested on Python 3.7.4; anything >3.7 should work fine.*

**Files**
```
├── graph.py
├── test_graph.py
├── main.py
├── time_djikstra.py
├── README.md
└── .gitignore
```

* The `Graph` class in graph.py is imported by other modules for use or testing. This file should be updated.<br>
* The `main.py` file is provided primarily for debugging during implementation. It can be run with `python main.py`<br>
* The unit tests are found in `test_graph.py` which can be used to help test the implementation in graph.py. This can be run simply using `pytest` in the command line. It automatically finds any test files and functions (they have to be prepended with test_)<br>
* `time_djikstra.py` can be used to test performance differences between the two Djikstra implementations once complete
