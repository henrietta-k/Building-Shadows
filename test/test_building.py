from building import*

def test_1():
    intervals = solve(8, [[6, 2, 2], [5, 3, 4], [0, 2, 1], [4, 2, 1], [0, 2, 1], [9, 6, 1], [0, 1, 1], [7, 1, 4]])
    print("Solution here: ", intervals)
    assert intervals == [(0, 1), (2, 0), (4, 1), (5, 4), (8, 0), (9, 1), (15, 0)]

def do_test_buildings(N, rect):
    N = int(input())
    rectangles = [[int(i) for i in input().split()] for _ in range(N)]
    intervals = solve(N, rectangles)

