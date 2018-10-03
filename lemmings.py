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
"""
    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2



def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    max_dist = 0
    
    if len(cafes) == num_holes:
        return max_dist
    elif len(cafes) == 1:
        max_dist = num_holes - len(cafes)
    else:
        max_dist = cafes[0]
        for cafe in range(len(cafes)-1):
            diff = int((cafes[cafe + 1] - cafes[cafe])/2)
            if diff > max_dist:
                max_dist = diff
    return max_dist



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
