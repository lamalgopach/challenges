"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2

    >>> furthest_best_time(7, [0, 6])
    3

    >>> furthest_best_time(3, [0, 1, 2])
    0

    >>> furthest_best_time(3, [2])
    2

    >>> furthest_best_time(3, [0])
    2

    >>> furthest_best_time(6, [2, 4])
    2


"""

def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""


    max_dist = 0
    for hole in range(num_holes):
        
        dist = min([abs(hole - cafe) for cafe in cafes])

        max_dist = max(dist, max_dist)

    return max_dist

def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe. Optimized runtime."""


    from bisect import bisect_left

    worst = 0

    for hole in range(num_holes):

        # Find the place we'd insert this hole into the
        # sorted cafes list.

        idx = bisect_left(cafes, hole)

        if idx == len(cafes):
            # print("uno")
            # This hole is after all the cafes, so the distance
            # is from this hole to the cafe before it
            dist = hole - cafes[idx - 1]

        elif idx == 0:
            # print("dos")
            # This hole is before all the cafes, so the distance
            # is from this hole to the cafe after it
            dist = cafes[idx] - hole
            # print(dist)

        elif cafes[idx] == hole:
            # print("tres")
            # This hole is a cafe, so no travel is needed!
            dist = 0

        else:
            # print("kwatros")
            # This hole is between two cafes, so use the smaller
            # distance between them
            dist = min(hole - cafes[idx - 1], cafes[idx] - hole)
            # print(dist)

        # Keep track of the longest distance we've seen
        worst = max(worst, dist)

    return worst


def furthest_best_time(num_holes, cafes):
    """Find longest distance between a hole and a cafe. Linear runtime."""


# We can simply measure the distance between cafes in a single loop:

# find the distance from the left edge to the first cafe; this is the distance a lemming in the first hole would have to travel.
# find the distance from the right edge to the last cafe; this is the distance a lemming in the last hole would have to travel.
# find the distance from every cafe (except the first) to the cafe to its left; a lemming in this gap would have to travel half that distance (half since it has a choice of whether to go left or right)
# This code is simple and linear.
    
    dist = 0
    worst = 0

    for hole in range(num_holes):
        if hole == 0:
            dist = cafes[0]
        elif hole == num_holes - 1:
            dist = hole - cafes[-1]
        # else:
            # print("gosia")

        worst = max(worst, dist)

    return worst















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
