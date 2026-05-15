# Function to print solution
def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


# Function to solve N-Queens using Branch & Bound
def solve_n_queens(n):

    # Create board
    board = [["." for _ in range(n)] for _ in range(n)]

    # 🔹 Arrays for Branch and Bound
    col = [False] * n
    diag1 = [False] * (2 * n - 1)   # row + col
    diag2 = [False] * (2 * n - 1)   # row - col + (n-1)

    # Backtracking function
    def backtrack(row):

        # If all queens are placed
        if row == n:
            print_solution(board, n)
            return

        # Try placing queen in each column
        for c in range(n):

            # Check if safe
            if not col[c] and not diag1[row + c] and not diag2[row - c + n - 1]:

                # Place queen
                board[row][c] = "Q"
                col[c] = diag1[row + c] = diag2[row - c + n - 1] = True

                # Move to next row
                backtrack(row + 1)

                # 🔹 Backtrack (remove queen)
                board[row][c] = "."
                col[c] = diag1[row + c] = diag2[row - c + n - 1] = False

    backtrack(0)


# 🔹 User Input
n = int(input("Enter value of N: "))
 
solve_n_queens(n)

