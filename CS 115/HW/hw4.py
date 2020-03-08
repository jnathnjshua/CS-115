"""I pledge my honor that I have abided by the Stevens Honor System. - Jonathan Joshua"""
import sys

sys.setrecursionlimit(10000)



def pascal_row(n):
    def pascal_add(row):
        if len(row) <= 1:
            return []
        return [row[0] + row[1]] + pascal_add(row[1:])
    def pascal_helper(n, row):
        if n == 0:
            return row
        return pascal_helper(n - 1, [1] + pascal_add(row) + [1])
    return pascal_helper(n, [1])


def pascal_triangle(n):
    if n < 0:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]

def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
