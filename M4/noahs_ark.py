from typing import List, Tuple, Dict
from collections import defaultdict, Counter


def get_neighbors(n: int, m: int, i: int, j: int) -> List[Tuple[int, int]]:
    """
    Given a point of the grid, return its neighbors.

    Parameters
    ----------
    n : int
        Number of rows in the grid
    m : int
        Number of columns in the grid
    i : int
        Line number of the point
    j : int
        Column number of the point

    Returns
    -------
        neighbors : List[Tuple[int, int]]
    """

    # neighbours
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    neighbors = []
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < m:
            neighbors.append((x, y))
    return neighbors


def largest_island(heights: List[List[int]]) -> List[List[bool]]:
    """
    It has been raining for 40 days and 40 nights and the whole world is underwater!
    Contemplating where to finally dock your ark, you want to find the largest island.
    You are lucky to have an exceptional topographical map that has the exact heights of all terrain.
    Unfortunately, you can't just find the largest landmass over sea level,
    as water can be trapped in valleys.

    Given an array of heights, return a bit-mask of the largest island.

    Parameters
    ----------
    heights : List[List[int]]
        A topological map of the surrounding land.
        Positive values represent heights above sea level
        and negative values, represent depth below sea level.
        A height of zero is considered underwater

    Returns
    -------
    mask : List[List[bool]]
        Boolean mask of the largest island
    """
    n, m = len(heights), len(heights[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    component = [[-1 for _ in range(m)] for _ in range(n)]
    components_size = {}
    largest_size = 0
    largest_component = -1

    def dfs(i: int, j: int, comp_id: int):
        if visited[i][j] or heights[i][j] <= 0:
            return 0
        visited[i][j] = True
        component[i][j] = comp_id
        size = 1
        for x, y in get_neighbors(n, m, i, j):
            if not visited[x][y] and heights[x][y] > 0:
                size += dfs(x, y, comp_id)
        return size

    # Initialize component ID and find components sizes
    comp_id = 0
    for i in range(n):
        for j in range(m):
            if heights[i][j] > 0 and not visited[i][j]:
                comp_size = dfs(i, j, comp_id)
                components_size[comp_id] = comp_size
                if comp_size > largest_size:
                    largest_size = comp_size
                    largest_component = comp_id
                comp_id += 1

    # Generate the mask for the largest component
    mask = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if component[i][j] == largest_component:
                mask[i][j] = True

    return mask


heights = [
    [0, 1, 1, 0],
    [1, 2, 2, 1],
    [1, 2, 3, 2],
    [0, 1, 2, 1]
]

largest_island(heights)

print(largest_island(heights))
