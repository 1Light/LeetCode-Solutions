# N-Queens II (Mode: Hard)

def totalNQueens(n: int) -> int:
    def solve(row, cols, diag1, diag2):
        if row == n:
            return 1

        total = 0
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place the queen and move to the next row
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            total += solve(row + 1, cols, diag1, diag2)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return total

    # Start solving from row 0 with empty sets for columns and diagonals
    return solve(0, set(), set(), set())
