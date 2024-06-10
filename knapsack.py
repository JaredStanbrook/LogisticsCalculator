class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

def knapsack_branch_and_bound(items, capacity):
    # Sort items by decreasing cost (value/weight ratio)
    items.sort(key=lambda x: x.cost, reverse=True)

    # Initialize variables
    max_value = 0
    current_weight = 0
    solution = [0] * len(items)
    best_solution = solution[:]

    # Define a function to calculate the upper bound of a node
    def upper_bound(level, value, weight):
        bound = value
        total_weight = weight
        j = level + 1
        while j < len(items) and total_weight + items[j].weight <= capacity:
            bound += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            bound += (capacity - total_weight) * items[j].cost
        return bound

    # Define the recursive branch and bound function
    def branch_and_bound(level, value, weight):
        nonlocal max_value, current_weight

        if weight <= capacity and value > max_value:
            max_value = value
            best_solution[:] = solution[:]

        if level < len(items):
            if weight + items[level].weight <= capacity:
                solution[level] = 1
                branch_and_bound(level + 1, value + items[level].value, weight + items[level].weight)
            bound = upper_bound(level, value, weight)
            if bound > max_value:
                solution[level] = 0
                branch_and_bound(level + 1, value, weight)

    # Start the branch and bound process
    branch_and_bound(0, 0, 0)

    return max_value, best_solution

def main():
    # Example input: list of items, each represented by weight and value
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    capacity = 40

    max_value, best_solution = knapsack_branch_and_bound(items, capacity)

    print("Maximum value:", max_value)
    print("Selected items:", [i for i, selected in enumerate(best_solution) if selected])

if __name__ == "__main__":
    main()
