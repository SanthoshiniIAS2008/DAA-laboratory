class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []
        self.backtracks = 0

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return

        placed = False

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                placed = True
                self.solve(row + 1)

        if not placed:
            self.backtracks += 1

    def print_board(self, solution):
        n = self.n
        line = "+" + "---+" * n

        print(line)
        for r in range(n):
            print("|", end="")
            for c in range(n):
                if solution[r] == c:
                    print(" Q |", end="")
                else:
                    print(" . |", end="")
            print()
            print(line)


# ---------------- Driver Code ----------------

sizes = [4, 6, 8]

for n in sizes:
    solver = NQueens(n)
    solver.solve()

    print(f"N={n}: {len(solver.solutions)} solutions, {solver.backtracks} backtracks")

    if n == 4:
        print("\nAll solutions for 4-Queens:\n")
        for i, sol in enumerate(solver.solutions, 1):
            print(f"Solution {i}: {sol}")
            solver.print_board(sol)
            print()