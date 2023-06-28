'''Lorenzo, Jonathan, Erasmo, Konstantinos and Clover like to take long walks
and discuss problems for next week. On one of those days, they were looking at
downtown Chicago from the Promontory Point in Hyde Park and were wondering how
an algorithm would construct a rendering of the view given information about the
location and height of the buildings. Thankfully, the student in Theory of
Algorithms can definitely help.

Assume every building is given as three integers $(left_i, width_i, height_i)$,
where $left_i$ indicates the distance at which building $i$ starts,  $width_i$
is the building's width and $height_i$ is its height. You need to return a list
of intervals $(x_j, h_j)$, denoting the distance at which $x_j$ which correspond
with where a height change starts and what the new height is.

{\\bf Input:}
The first line contains a single integer $N$, the number of buildings. $N$ lines
follow. Each line has three integers; where the building starts on the $x$-axis,
its width and its height. DO NOT ASSUME THEY ARE ORDERED.

{\\bf Output:}
You need to print out the height segments. In every line there should be two
integers. The first one designates where the segment startsand the second is the
height.'''


# Add your functions here


def solve(N, rectangles):
    '''Solver function'''
    ...
    if N == 1:
        build = rectangles[0]
        shadow_1 = (build[0], build[2])
        shadow_2 = (build[0] + build[1], 0)
        return [shadow_1, shadow_2]
    else:
        mid_n = N // 2
        return merge(solve(mid_n, rectangles[ :mid_n]), solve(N - mid_n, rectangles[mid_n: ]))


def merge(shadow_1, shadow_2):
    result = []
    prev_h_1, prev_h_2 = 0, 0

    while len(shadow_1) or len(shadow_2):
        if not len(shadow_1) or not len(shadow_2):
            result.extend(shadow_2 or shadow_1)
            break

        x1, h1 = shadow_1[0]
        x2, h2 = shadow_2[0]

        if x1 <= x2:
            prev_h_1 = h1
            update_result(x1, max(prev_h_2, h1), result)
            shadow_1.pop(0) #maintain a pointer or index 
        else:
            prev_h_2 = h2
            update_result(x2, max(prev_h_1, h2), result)
            shadow_2.pop(0)

    return result

def update_result(x, h, result):
    if result:
        last_x, last_h = result[-1]
        if last_x == x:
            result[-1] = ((x, max(last_h, h)))
        elif last_h == 0 and h == 0:
            result[-1] = (max(x, last_x), 0)
        elif last_h != h:
            result.append((x, h))
    else:
        result.append((x, h))

def print_solution(intervals):
    for x, h in intervals:
        print(x, h)

def main():
    N = int(input())
    rectangles = [[int(i) for i in input().split()] for _ in range(N)]
    intervals = solve(N, rectangles)
    print_solution(intervals)


if __name__ == '__main__':
    main()
