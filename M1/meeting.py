from typing import List, Set, Dict, Tuple    

def distance(house1: Tuple[int, int], house2: Tuple[int, int]) -> int:
    """
    Returns the distance between two houses.

    Parameters
    ----------
    house1, house2: Tuple[int, int]
        Houses to compare.

    Returns
    -------
    dist: int
        The distance between the houses.
    """
    dist = abs(house1[0] - house2[0]) + abs(house1[1] - house2[1])  # Distance equation
    return dist

def solve(N: int, houses: List[Tuple[int, int]]) -> int:
    """
    Given a list of student houses, returns the minimum total distance the students need to travel.

    Parameters
    ----------
    N : int
        The number of boxes.
    houses : List[Tuple[int, int]]
        A list of tuples each of which represents a student's house

    Returns
    -------
    int
        The minimum total distance all students need to travel.
    """

    min_distance = float('inf')

    for h in houses:
        total_distance = sum(distance(h, house) for house in houses)    # Compare to all other houses
        min_distance = min(min_distance, total_distance)                # Check if found dist is new minimum dist

    return min_distance
