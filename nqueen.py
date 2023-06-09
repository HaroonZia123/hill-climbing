import random


class Node:
    def __init__(self, state=0, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class NQueensProblem:
    def __init__(self, n):
        self.n = n

    def initial_state(self):
        state = list(range(self.n))
        random.shuffle(state)
        print("Intial State is ")
        print(state)
        return state

    def value(self, state):
        return -self.conflicts(state)  # Negative conflicts as we want to maximize value

    def conflicts(self, state):
        count = 0
        n = len(state)
        for i in range(n):
            for j in range(i + 1, n):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    count += 1
        return count

    def successors(self, state):
        successors = []
        for i in range(self.n):
            for j in range(self.n):
                if state[i] != j:
                    successor = state[:]
                    successor[i] = j
                    successors.append(successor)
        return successors


def hill_climbing(problem):
    current = Node(problem.initial_state())
    count=0
    while True:
        neighbors = problem.successors(current.state)
        if not neighbors:
            return current.state
        neighbor = max(neighbors, key=lambda x: problem.value(x))
        #print(problem.value(neighbor))
        # print(neighbors)
        if problem.value(neighbor) < problem.value(current.state):
            return current.state
        elif problem.value(neighbor) ==problem.value(current.state) and count!=100:
             count+=1
        elif problem.value(neighbor) ==problem.value(current.state) and count==100:
             return current.state    
        current = Node(neighbor)
        print()


# Usage
n = int(input("Enter the number of queens: "))
problem = NQueensProblem(n)
solution = hill_climbing(problem)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
