"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    nums_set = set()
    nums_dictionary = {}
    for item in nums:
        if item not in nums_dictionary:
            nums_dictionary[item] = 1
        else:
            nums_dictionary[item] += 1


    max_value = 0

    for key, value in nums_dictionary.items():
        if value > max_value:
            max_value = value


    for key, value in nums_dictionary.items():
        if value == max_value:
            nums_set.add(key)

    return nums_set








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")