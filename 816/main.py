"""Solution for Problem #816."""

import math
import time

from typing import List, Tuple
from min_dist import closestpair


SAVED_VALS = {}


def _generator_helper(n: int) -> int:
    """Helper function to generate the random number recursively.

    Args:
        n: The value of n in s_n.

    Returns:
        The random number generated (s_n)
    """
    if n in SAVED_VALS:
        return SAVED_VALS[n]
    s_zero = 290797
    if n == 0:
        return s_zero

    value = _generator_helper(n-1)**2 % 50515093
    SAVED_VALS[n] = value
    return value


def construct_points(k: int) -> List[Tuple[int, int]]:
    """Main driver function for point generation.

    Args:
        k: The number of points to generate.

    Returns:
        A list containing the points generated.
    """
    points = []
    for i in range(k):
        value = _generator_helper(2*i)
        next_value = value**2 % 50515093
        SAVED_VALS[2*i + 1] = next_value
        point = (value, next_value)
        points.append(point)
    return points


def calculate_distance(
    a: Tuple[float, float],
    b: Tuple[float, float]
) -> float:
    """Calculates the distance between two points."""
    dist = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return dist


def main():
    # Input 2000000 for the specific solution to the problem.
    num = int(input("Enter number: "))

    point_gen_start_time = time.time()
    points_array = construct_points(num)
    point_gen_end_time = time.time()

    total_point_gen_time = point_gen_end_time - point_gen_start_time
    print(f'Time taken to generate points: {total_point_gen_time}s')

    dist_calculator_start_time = time.time()
    a, b = closestpair(points_array)
    min_dist = calculate_distance(a, b)
    dist_calculator_end_time = time.time()
    total_dist_calc_time = (
        dist_calculator_end_time - dist_calculator_start_time
    )
    print(
        f'The closest pair is: {a}, {b} '
        f'with a distance of {min_dist}'
    )
    print(
        f'Time taken to calculate shortest distance: {total_dist_calc_time}s'
    )


if __name__ == "__main__":
    main()
