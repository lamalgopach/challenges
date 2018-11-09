"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""
    
    if len(lst) == 1:
    	return lst[0]

    print(lst[0])
    lst = lst[1:]
    return print_recursively(lst)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. GREAT JOB!\n")