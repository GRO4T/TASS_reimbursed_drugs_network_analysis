import networkx as nx
import pandas as pd


def create_bipartite_graph(set_0, set_1, weights=None) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(set_0, bipartite=0)
    graph.add_nodes_from(set_1, bipartite=1)
    if weights is not None:
        edges = list(zip(set_0, set_1, weights))
        graph.add_weighted_edges_from(edges)
    else:
        edges = list(zip(set_0, set_1))
        graph.add_edges_from(edges)

    return graph


def create_bipartite_layout(set_0, set_1) -> dict:
    layout = {}
    layout.update((n, (1, i)) for i, n in enumerate(set_0))
    layout.update((n, (2, i)) for i, n in enumerate(set_1))

    return layout


def sum_node_weights(graph, nodes, columns) -> pd.DataFrame:
    weight_sum = [
        (n, sum(graph.edges[n, neighbor]["weight"] for neighbor in graph.neighbors(n)))
        for n in nodes
    ]
    return pd.DataFrame(weight_sum, columns=columns)
