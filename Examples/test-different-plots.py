import numpy as np
import networkx as nx
import sys
sys.path.append('..')
from PlotModule import *

#generating adjacency matrix of a 5x5 2d-horizontal-latiice
grid_dim = 5
G = nx.grid_graph(dim=(grid_dim, grid_dim), periodic=True)
adj_matrix = nx.adjacency_matrix(G)

#pre-computed probabilities
probs = np.array([[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00],
    [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.50000000e-01,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 2.50000000e-01,
    0.00000000e+00, 2.50000000e-01, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 2.50000000e-01, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
    0.00000000e+00],
    [0.00000000e+00, 0.00000000e+00, 6.25000000e-02, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 1.25000000e-01, 0.00000000e+00,
    1.25000000e-01, 0.00000000e+00, 6.25000000e-02, 0.00000000e+00,
    2.50000000e-01, 0.00000000e+00, 6.25000000e-02, 0.00000000e+00,
    1.25000000e-01, 0.00000000e+00, 1.25000000e-01, 0.00000000e+00,
    0.00000000e+00, 0.00000000e+00, 6.25000000e-02, 0.00000000e+00,
    0.00000000e+00],
    [0.00000000e+00, 1.56250000e-02, 1.56250000e-02, 1.56250000e-02,
    0.00000000e+00, 1.56250000e-02, 0.00000000e+00, 2.03125000e-01,
    0.00000000e+00, 1.56250000e-02, 1.56250000e-02, 2.03125000e-01,
    0.00000000e+00, 2.03125000e-01, 1.56250000e-02, 1.56250000e-02,
    0.00000000e+00, 2.03125000e-01, 0.00000000e+00, 1.56250000e-02,
    0.00000000e+00, 1.56250000e-02, 1.56250000e-02, 1.56250000e-02,
    0.00000000e+00],
    [7.81250000e-03, 7.81250000e-03, 1.56250000e-02, 7.81250000e-03,
    7.81250000e-03, 7.81250000e-03, 1.56250000e-02, 3.90625000e-03,
    1.56250000e-02, 7.81250000e-03, 1.56250000e-02, 3.90625000e-03,
    7.65625000e-01, 3.90625000e-03, 1.56250000e-02, 7.81250000e-03,
    1.56250000e-02, 3.90625000e-03, 1.56250000e-02, 7.81250000e-03,
    7.81250000e-03, 7.81250000e-03, 1.56250000e-02, 7.81250000e-03,
    7.81250000e-03],
    [7.81250000e-03, 1.17187500e-02, 4.88281250e-03, 1.17187500e-02,
    7.81250000e-03, 1.17187500e-02, 9.76562500e-03, 2.03125000e-01,
    9.76562500e-03, 1.17187500e-02, 4.88281250e-03, 2.03125000e-01,
    3.90625000e-03, 2.03125000e-01, 4.88281250e-03, 1.17187500e-02,
    9.76562500e-03, 2.03125000e-01, 9.76562500e-03, 1.17187500e-02,
    7.81250000e-03, 1.17187500e-02, 4.88281250e-03, 1.17187500e-02,
    7.81250000e-03],
    [1.95312500e-03, 1.87988281e-02, 3.73535156e-02, 1.87988281e-02,
    1.95312500e-03, 1.87988281e-02, 7.22656250e-02, 3.17382812e-03,
    7.22656250e-02, 1.87988281e-02, 3.73535156e-02, 3.17382812e-03,
    3.90625000e-01, 3.17382812e-03, 3.73535156e-02, 1.87988281e-02,
    7.22656250e-02, 3.17382812e-03, 7.22656250e-02, 1.87988281e-02,
    1.95312500e-03, 1.87988281e-02, 3.73535156e-02, 1.87988281e-02,
    1.95312500e-03],
    [9.88769531e-03, 1.37939453e-02, 1.92871094e-02, 1.37939453e-02,
    9.88769531e-03, 1.37939453e-02, 1.09863281e-02, 1.81701660e-01,
    1.09863281e-02, 1.37939453e-02, 1.92871094e-02, 1.81701660e-01,
    2.19726562e-03, 1.81701660e-01, 1.92871094e-02, 1.37939453e-02,
    1.09863281e-02, 1.81701660e-01, 1.09863281e-02, 1.37939453e-02,
    9.88769531e-03, 1.37939453e-02, 1.92871094e-02, 1.37939453e-02,
    9.88769531e-03],
    [1.95312500e-03, 2.02636719e-02, 2.14385986e-02, 2.02636719e-02,
    1.95312500e-03, 2.02636719e-02, 2.10266113e-02, 3.17382812e-03,
    2.10266113e-02, 2.02636719e-02, 2.14385986e-02, 3.17382812e-03,
    6.47521973e-01, 3.17382812e-03, 2.14385986e-02, 2.02636719e-02,
    2.10266113e-02, 3.17382812e-03, 2.10266113e-02, 2.02636719e-02,
    1.95312500e-03, 2.02636719e-02, 2.14385986e-02, 2.02636719e-02,
    1.95312500e-03],
    [5.98144531e-03, 5.28335571e-03, 3.21388245e-02, 5.28335571e-03,
    5.98144531e-03, 5.28335571e-03, 6.10351562e-03, 1.95148468e-01,
    6.10351562e-03, 5.28335571e-03, 3.21388245e-02, 1.95148468e-01,
    2.44140625e-04, 1.95148468e-01, 3.21388245e-02, 5.28335571e-03,
    6.10351562e-03, 1.95148468e-01, 6.10351562e-03, 5.28335571e-03,
    5.98144531e-03, 5.28335571e-03, 3.21388245e-02, 5.28335571e-03,
    5.98144531e-03]])


probs = probs[0:1]
##bar plot
#PlotProbabilityDistribution(probs)
#PlotProbabilityDistribution(probs, graph=G)
#PlotProbabilityDistribution(probs, labels={0: 'a', 5: 'b'})
#PlotProbabilityDistribution(probs, graph=G, labels=
#        {(0, 0): 'bottom left', (2, 2): 'middle', (0, 4): 'bottom right'})
#
##line plot
#PlotProbabilityDistribution(probs, plot_type='line')
#
##graph plot
#PlotProbabilityDistribution(probs, plot_type='graph', adj_matrix=adj_matrix)
#
##graph plot with colors and fixed node size
#PlotProbabilityDistribution(probs, plot_type='graph', adj_matrix=adj_matrix,
#        node_size=500, cmap='viridis')

#graph plot with colors and changing node size
PlotProbabilityDistribution(probs, plot_type='graph', adj_matrix=adj_matrix, cmap='default',
        graph=G, labels={(0, 0): 'bottom left', (2, 2): 'middle', (0, 4): 'bottom right'})

#testing if error is raised
try:
    PlotProbabilityDistribution(probs, plot_type='graph')
except KeyError as err:
    print("It was expected an " + str(err) + " entry in kwargs")

print()

#testing if error is raised
try:
    PlotProbabilityDistribution(probs, plot_type='hist')
except ValueError as err:
    print(err)
else:
    print('Unexpected exception raised')
