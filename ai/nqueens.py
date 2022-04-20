from sympy import false, re, true


def is_Safe (arr, x, y, n) :
    for r in range (0, x) : 
        if (arr[r][y] == 1) :
            return False


    row = x
    col = y

    while (row >= 0 and col >= 0) :
        if (arr[row][col] == 1) :
            return False

        row -= 1
        col -= 1

    row = x
    col = y

    while (row >= 0 and col < n) :
        if (arr[row][col] == 1) :
            return False

        row -= 1
        col += 1

    return True

def n_Queen (arr, x, n) :
    if (x >= n) :
        return True

    for c in range (0, n) :
        if (is_Safe (arr, x, c, n)) :
            arr[x][c] = 1

            if (n_Queen (arr, x + 1, n)) :
                return True

            arr[x][c] = 0


    return False

def main():
    n = int(input())
    a = [['0' for x in range(n)] for y in range(n)]

    if (n_Queen(a, 0, n)) :
        for i in range (0, n) :
            for j in range (0, n) :
                print(a[i][j], end = ' ')
            print("")


main()