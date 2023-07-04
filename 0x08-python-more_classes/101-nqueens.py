#!/usr/bin/python3
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def createBoard(size):
        board = []
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append("free")
        return board

    def takeCells(boardCopy, i, j):
        for m in range(n):
            boardCopy[i][m] = "attack"
            boardCopy[m][j] = "attack"

        k = i
        m = j
        while k >= 0 and m >= 0:
            boardCopy[k][m] = "attack"
            k -= 1
            m -= 1

        k = i
        m = j
        while k < n and m < n:
            boardCopy[k][m] = "attack"
            k += 1
            m += 1

        k = i
        m = j
        while k >= 0 and m < n:
            boardCopy[k][m] = "attack"
            k -= 1
            m += 1

        k = i
        m = j
        while k < n and m >= 0:
            boardCopy[k][m] = "attack"
            k += 1
            m -= 1

        return boardCopy

    solutions = []

    for posi in range(n):
        boardcopy = createBoard(n)
        solution = []
        for j in range(posi):
            boardcopy[0][j] = "attack"
        for i in range(n):
            for j in range(n):
                if boardcopy[i][j] != "attack":
                    solution.append([i, j])
                    boardcopy = takeCells(boardcopy, i, j)
                    break
        if len(solution) == n:
            solutions.append(solution)

    for solution in solutions:
        print(solution)
