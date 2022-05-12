# hpwalk
Source code of Hiperwalk project
http://qubit.lncc.br/qwalk/

Currently, it is necessary to have
[neblina-core](https://github.com/paulomotta/neblina-core) and
[pyneblina](https://github.com/paulomotta/pyneblina) installed.
Paulo Motta described on his blog the
[installation steps for both neblina-core and pyneblina](https://paulomotta.pro.br/wp/2021/05/01/pyneblina-and-neblina-core/).

# Style Guide for Python Code
The code must be written accordingly [PEP 8](https://peps.python.org/pep-0008/).
Some code may need to be updated to match PEP 8's requirements.

# TODO List
- [ ] Update installation instructions
- [X] Refactor Coined\_QW\_Adjacency\_Matrix-v2.ipynb
- [ ] Create separated file for plotting
	- [ ] General plotting based on networkx
- [ ] Specific functions for widely used walks?
- [ ] Support for different coins
	- [ ] Hadamard Coin general dimensions
	- [ ] Generating shift operator: checking whether argument type is sparse or not
	- [ ] Optimization: use lil\_matrix instead of csr\_matrix while generating S operator
- [ ] Construct shift operators based on sympy expressions?
- [ ] Implement and refactor tests
	- [ ] Complete Graph
	- [ ] Line walk
	- [ ] Mesh walk
	- [ ] Tests for plotting graphs?
- [ ] Clean examples
- [ ] Add commentaries to CoinedModel
- [ ] Create documentation
	- [ ] pdf (with LaTeX)
	- [ ] webpage
- [ ] PyneblinaInterface.py
	- [ ] Rename functions
	- [ ] Remove definition from examples
	- [ ] Move PyneblinaInterface.py functions to Pyneblina project?
