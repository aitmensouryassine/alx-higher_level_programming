#!/usr/bin/python3
import sys


""" Nqueens solution with backtracking """


class Nqueens():
    """ Nqueens class """

    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for i in range(n)]

        self.cols = set()
        self.rDigs = set()
        self.lDigs = set()

        self.solutions = []

    def backtrack(self, row=0):
        if row == self.n:
            result = []
            for row in self.board:
                for position in row:
                    position and result.append(position)
            self.solutions.append(result)
            return

        for col in range(self.n):
            if col in self.cols or \
               (row + col) in self.rDigs or (row - col) in self.lDigs:
                continue

            self.cols.add(col)
            self.rDigs.add(row + col)
            self.lDigs.add(row - col)
            self.board[row][col] = [row, col]

            self.backtrack(row + 1)

            self.cols.remove(col)
            self.rDigs.remove(row + col)
            self.lDigs.remove(row - col)
            self.board[row][col] = 0

    def solution(self):
        self.backtrack()
        for solution in self.solutions:
            print(solution)


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

    nq = Nqueens(n)
    nq.solution()
