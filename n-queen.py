grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def solve(grid):
    row = find_empty(grid)

    if row == None:
        return True

    for col in range(len(grid[0])):
        print(validate((row, col), grid), row, col)
        if validate((row, col), grid):
            grid[row][col] = 1

            if solve(grid):
                return True
            else:
                grid[row][col] = 0
    # if
    return False


def find_empty(grid):
    for i in range(len(grid)):
        if 1 not in grid[i]:
            return i


def validate(pos, grid):
    row, col = pos
    # Check Position
    if grid[row][col] == 1:
        return False

    # Check row
    if 1 in grid[row]:
        return False

    # Check col
    for i in range(len(grid)):
        if grid[i][col] == 1:
            return False

    n, m = pos
    if n == 0 or m == 0:
        back = False
    else:
        back = True
    # Check diagonal \
    while True:
        print(n, m)
        if n > len(grid)-1 or m > len(grid[0])-1:
            break
        if back:
            n -= 1
            m -= 1
            if grid[n][m] == 1:
                return False
            if n == 0 or m == 0:
                back = False
                n, m = pos
        if not back:
            if n == len(grid)-1 or m == len(grid[0])-1:
                break
            n += 1
            m += 1
            if grid[n][m] == 1:
                return False

    n, m = pos
    if n == 0 or m == 0:
        back = True
    else:
        back = False
    # Check Diagonal/
    while True:
        print(n, m)
        if n >= len(grid)-1 or m >= len(grid[0])-1:
            break
        if back:
            n += 1
            m -= 1
            if grid[n][m] == 1:
                return False
            if n == 0 or m == 0:
                back = False
                n, m = pos
        if not back:
            if n == len(grid)-1 or m == len(grid[0])-1:
                break
            n -= 1
            m += 1
            if grid[n][m] == 1:
                return False
    return True


def print_grid(grid):
    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if j == len(grid[0])-1:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


solve(grid)
print_grid(grid)
