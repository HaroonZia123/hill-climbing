def count_successors(state):
    """Count the total number of successors for a given state."""
    n = len(state)
    total_successors = 0

    for row in range(n):
        for col in range(n):
            if state[row] != col:
                total_successors += 1

    return total_successors

def generate_successors(state):
    """Generate successor states by moving queens within their rows."""
    successors = []
    n = len(state)

    for row in range(n):
        for col in range(n):
            if state[row] != col:
                successor = state[:]
                successor[row] = col
                successors.append(successor)

    return successors

# Example usage
state = [0, 1, 2, 3]  # Example state
successor_count = generate_successors(state)
print("Total successors:", successor_count)
