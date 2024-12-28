from typing import List, Hashable

import networkx as nx
import numpy as np

#import utils


def segment_image(k: int, image: np.ndarray) -> np.ndarray:
    """
    Segment a grayscale image into n segments with MST-based segmentation.
    Create an undirected graph representation of the image and
    run the described modified Kruskal's algorithm to form segments

    Parameters
    ----------
    k : int
        Parameter determining whether segments are contiguous
    image : np.ndarray
        Two dimensions NumPy array representing a grayscale image

    Returns
    -------
    segments : np.ndarray
        Two dimensional NumPy array of the same dimensions as `image`.
        Each entry contains the label of the segment the corresponding
        pixel belongs.
    """
    assert len(image.shape) == 2


    # TODO

    # Initialize a graph G:
    G = nx.Graph()
    rows, cols = image.shape

    # Initialize the vertices in the graph
    for i in range(rows):
        for j in range(cols):
            G.add_node((i, j), value=image[i, j])

    # Compute VALID edges, check for corner and edge cases
    for i in range(rows):
        for j in range(cols):
            neighbors = [(i-1, j-1), # Top left
                         (i-1, j),   # Top
                         (i-1, j+1), # Top right
                         (i, j-1),   # Left
                         (i, j+1),   # Right
                         (i+1, j-1), # Bottom left
                         (i+1, j),   # Bottom
                         (i+1, j+1)] # Bottom Right
            
            # For weight computations:
            for x, y in neighbors:
                if 0 <= x and x < rows and 0 <= y and y < cols: # Check boundary conditions
                    weight = abs(image[i, j] - image[x, y])  # Compute weights 
                    G.add_edge((i, j), (x, y), weight=weight)  # Add weighted edge

    sorted_edges = sorted(G.edges(data=True), key=lambda edge: edge[2]['weight']) # Sort edges by weight
    
    vertices = [(x, y) for x in range(rows) for y in range(cols)]     # Initilize vertices
    values = [image[x, y] for x in range(rows) for y in range(cols)]  # Initilize greyscale values

    uf = UnionFind(vertices, values) # Call unionfind

    for u, v, weights in sorted_edges:
        if uf.find(u) != uf.find(v):  # Check if u and v belong to different segments
            weight = weights['weight'] 
            threshold = min(uf.max_diff(u) + k / uf.size(u), uf.max_diff(v) + k / uf.size(v))  # Compute threshold weight
            if weight <= threshold:
                uf.union(u, v) # Call union to combine u and v into one segment

        #Else: Do nothing


    # For mapping uf segments to the 2D array
                
    seg_img = np.zeros_like(image)
    seg_label = {}
    mapping = {}

    # Initialize vertices from our graph G:
    for u in G.nodes:
        seg_label[u] =  uf.find(u)

    # Map vertices to their value
    for data, v in enumerate(seg_label.values()):
        mapping[v] = data

    # Segmented Image: Each entry is an integer label for a segment
    for (x, y), label in seg_label.items():
        seg_img[x, y] = mapping[label]

    return seg_img
    


class UnionFind:
    """
    Union-Find data structure

    Attributes
    ----------
    parent : Dict[Hashable, Hashable]
        Dictionary pointing to a vertex to its representative
    min_values : Dict[Hashable, any]
        Minimum value in each segment
    max_values : Dict[Hashable, any]
        Maximum value in each segment

    Methods
    -------
    find(x: Hashable) -> Hashable
        Given a vertex `x`, return the representative of the segment it belongs
    union(x: Hashable, y: Hashable) -> None
        Combines the two segments connected by the edge (x,y) into one segment
    max_diff(x: Hashable) -> int
        Given a vertex, returns the largest difference in values between
        any vertices in the segment `x` belongs to
    """
    def __init__(self, vertices: List[Hashable], values: List):
        """
        Parameters
        ----------
        vertices : List[Hashable]
            List of vertices
        values : List
            Grayscale values for each vertex
        """
        # the parent of x, used by find() to retrieve x's segment
        self.parent = {x: x for x in vertices}
        # the smallest value in x's segment
        self.min_values = {x: values[idx] for idx, x in enumerate(vertices)}
        # the largest value in x's segment
        self.max_values = {x: values[idx] for idx, x in enumerate(vertices)}


        # initialize the rank for each vertex
        self.rank = {x: 1 for x in vertices}
        

    def find(self, x: Hashable) -> Hashable:
        """
        Given a vertex `x`, return the representative of the segment it belongs

        Parameters
        ----------
        x : Hashable
            A vertex of the graph

        Returns
        -------
        representative : Hashable
            The representative of the segment that `x` belongs to
        """
        # TODO: Make sure you use path compression
        ...
    
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]



    def union(self, x: Hashable, y: Hashable) -> None:
        """
        Combines the two segments connected by the edge (x,y) into one segment

        Parameters
        ----------
        x : Hashable
            A vertex
        y : Hashable
            Another vertex
        """
        # TODO: Combine the two segments into one if they are different
        #       Make sure to update al relevant auxiliary variables
        ...
        x_p = self.find(x)
        y_p = self.find(y)

        if x_p != y_p:
            if self.rank[x_p] < self.rank[y_p]:   # To see which tree to merge to
                self.parent[x_p] = y_p  # reassign parent
                self.rank[y_p] += self.rank[x_p]  # update rank
                self.min_values[y_p] = min(self.min_values[x_p], self.min_values[y_p]) # Update min values
                self.max_values[y_p] = max(self.max_values[x_p], self.max_values[y_p]) # Update max values
            else:
                self.parent[y_p] = x_p
                self.rank[x_p] += self.rank[y_p]
                self.min_values[x_p] = min(self.min_values[x_p], self.min_values[y_p]) # Update min values
                self.max_values[x_p] = max(self.max_values[x_p], self.max_values[y_p]) # Update max values

                if self.rank[x_p] == self.rank[y_p]:  
                    self.rank[x_p] += 1



    def max_diff(self, x: Hashable) -> int:
        """
        Given a vertex, returns the largest difference in values between
        any vertices in the segment `x` belongs to

        Parameters
        ----------
        x : Hashable
            A vertex

        Returns
        -------
        diff : int
            Largest difference in values between any vertices in the segment `x` belongs to
        """
        return self.max_values[self.find(x)] - self.min_values[self.find(x)]


    # Helper function find the the size (rank) of the vertex's segment
    def size(self, x: Hashable) -> int:
        root = self.find(x)
        return self.rank[root]
    
    


if __name__ == "__main__":
    # You can manually test your code here
    wave = utils.load_segment_save_image(9, "wave.png", "wave_segmented.png")
    #smile = utils.load_segment_save_image(3, "smiling.png", "smiling_segmented.png")
    
    segment_image(0, wave)
    pass
