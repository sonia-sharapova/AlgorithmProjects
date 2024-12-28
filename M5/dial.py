from __future__ import annotations

from typing import Hashable

import networkx as nx

from utils import generate_complete_weighted_graph



def dial_shortest_path_length(
    G: nx.Graph, source: Hashable, max_edge_weight: int | None = None
) -> dict[Hashable, float]:
    """Compute single-source shortest path distances via Dial's algorithm.

    Parameters
    ----------
    G : nx.Graph
        An undirected graph with bounded positive integer edge weights.
    source : Hashable
        The source vertex.
    max_edge_weight : Optional[int], optional
        Maximum edge weight in G, by default None.
        Will be calculated in Theta(E) time if not provided.

    Returns
    -------
    distance : dict[Hashable, float]
        Shortest path distances from source in G.

    Examples
    --------
    >>> G = generate_complete_weighted_graph(n=20, max_edge_weight=5)
    >>> expected = nx.single_source_dijkstra_path_length(G, source=0)
    >>> actual = dial_shortest_path_length(G, source=0, max_edge_weight=5)
    >>> actual == expected
    True
    """
    if max_edge_weight is None:
        # Compute max edge weight if not provided
        max_edge_weight = max(d["weight"] for u, v, d in G.edges(data=True))

    # TODO: Implement Dial's algorithm
        
    # Initialize distance dictionary with infinity values since we want to find shortest path
    distances = {node: float('inf') for node in G.nodes()}
    distances[source] = 0  # Base Case

    # Initialize buckets with empty lists
    buckets = [[] for _ in range(max_edge_weight * len(G) + 1)]
    bucket_idx = {node: None for node in G.nodes()} # To track bucket position
    
    # Place source node into the bucket and set initial bucket position to 0
    bucket_idx[source] = 0 
    buckets[0].append(source)

    # Cover all possible distances in bucket queue
    for curr_dist in range(max_edge_weight * len(G) + 1):
        # Process all nodes at given distance
        while buckets[curr_dist]:
            u = buckets[curr_dist].pop(0)  # Get and remove the first node in the current bucket
            for v, data in G[u].items():   # Iterate through graph
                weight = data['weight']
                if distances[u] + weight < distances[v]:   # Check for shorter path
                    distances[v] = distances[u] + weight   # Update distances
                    if bucket_idx[v] is not None:
                        buckets[bucket_idx[v]].remove(v)   # Remove from buckets and update
                    bucket_idx[v] = distances[v]
                    buckets[distances[v]].append(v)        

    return distances

# TODO: Analysis

'''
Let W be the maximum edge weight.

Runtime:

Initialization: O(V)
Main Loop: 
- Goes through all the edges once, O(E). 
- Iterates through the entire buckets array once, O(V*W)
- The bucket queue allows for constant time, O(1), when placing and removing buckets 
(based on distance).

Overall running time: O(V*W + E)


Space Complexity: O(V*W)

The space we need for the buckets array to hold the vertices and the maximum edge
weight is O(V*W). In the worst case, evert vertex's edge is of the maximum weight.
The dictionary containing the positions of the buckets needs O(V) space.

The total space complexity is then O(V + V * W) = O(V * W)

'''


if __name__ == "__main__":
    import doctest

    doctest.testmod()
