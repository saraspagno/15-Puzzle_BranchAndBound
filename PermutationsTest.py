import ast

N = 4


def getInvCount(arr):
    arr1 = []
    for y in arr:
        for x in y:
            arr1.append(x)
    arr = arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1

    return inv_count


# find Position of blank from bottom
def findXPosition(puzzle):
    # start from bottom-right corner of matrix
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if (puzzle[i][j] == 0):
                return N - i


def isSolvable(puzzle):
    invCount = getInvCount(puzzle)

    if (N & 1):
        return ~(invCount & 1)

    else:  # grid is even
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1


if __name__ == '__main__':
    file = open('permutatations.txt', 'r')
    while True:
        line = file.readline().strip()
        if not line:
            break
        tiles = ast.literal_eval(line)
        print("Solvable") if isSolvable(tiles) else print("Not Solvable")
