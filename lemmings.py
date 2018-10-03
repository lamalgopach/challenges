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

"""

def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""


    max_dist = 0
    for hole in range(num_holes):
        
        dist = min([abs(hole - cafe) for cafe in cafes])

        max_dist = max(dist, max_dist)

    return max_dist

def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""


# In this approach, we’ll use binary search to find the location where we’d insert each hole into the cafes list. We have four cases to consider:

# this hole is after all cafes, so find the distance to the last cafe
# this hole is before all cafes, so find the distance to the first cafe
# this hole is a cafe (so distance is zero)
# this hole is between two cafes, so find the smallest travel distance between them
# This search is done for each hole, so the runtime is O(num_holes * log num_cafes). (Binary search is logarithmic, and we do that num_holes number of times.)

# We could write our own binary search, but Python includes one the standard library, bisect. We’ll use this.

    # dist_last = num_holes - cafes[-1]
    # dist_fst = cafes[0]
    # dist_in_cf = 0 # if len(cafes) == num_holes
    # dist_btw = 


    from bisect import bisect_left

    worst = 0

    for hole in range(num_holes):

        # Find the place we'd insert this hole into the
        # sorted cafes list.

        idx = bisect_left(cafes, hole)

        if idx == len(cafes):
            print("uno")
            # This hole is after all the cafes, so the distance
            # is from this hole to the cafe before it
            dist = hole - cafes[idx - 1]

        elif idx == 0:
            print("dos")
            # This hole is before all the cafes, so the distance
            # is from this hole to the cafe after it
            dist = cafes[idx] - hole
            print(dist)

        elif cafes[idx] == hole:
            print("tres")
            # This hole is a cafe, so no travel is needed!
            dist = 0

        else:
            print("kwatros")
            # This hole is between two cafes, so use the smaller
            # distance between them
            dist = min(hole - cafes[idx - 1], cafes[idx] - hole)
            print(dist)

        # Keep track of the longest distance we've seen
        worst = max(worst, dist)

    return worst





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
