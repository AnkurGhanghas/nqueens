import random


# Function to calculate heuristic (number of conflicts)
def calculate_conflicts(board):
    conflicts = 0
    n = len(board)

    # Check all pairs of queens
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:  # Same column
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):  # Same diagonal
                conflicts += 1

    return conflicts


# Function to perform hill climbing search with random restarts
def hill_climbing(n):
    # Randomly initialize the board (one queen per row)
    board = [random.randint(0, n - 1) for _ in range(n)]
    steps = 0

    while True:
        # Calculate the number of conflicts (heuristic)
        conflicts = calculate_conflicts(board)

        if conflicts == 0:
            # Found solution, no conflicts
            return board, steps

        # Generate all neighbors (move each queen to a different row in the same column)
        neighbors = []
        for i in range(n):
            for j in range(n):
                if board[i] != j:
                    new_board = board[:]
                    new_board[i] = j
                    neighbors.append(new_board)

        # Evaluate all neighbors and select the one with the least conflicts
        best_board = board
        best_conflicts = conflicts
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < best_conflicts:
                best_board = neighbor
                best_conflicts = neighbor_conflicts

        # If no improvement, restart the search
        if best_conflicts >= conflicts:
            board = [random.randint(0, n - 1) for _ in range(n)]  # Random restart
        else:
            board = best_board

        steps += 1


# Main function to execute the algorithm
def main():
    n = 8  # You can change N to test different board sizes
    solution, steps = hill_climbing(n)

    print(f"Solution found: {solution}")
    print(f"Steps taken: {steps}")


if __name__ == "__main__":
    main()
