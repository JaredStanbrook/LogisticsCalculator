import math
from collections import defaultdict


def cutting_stock(raw_lengths, orders):
    num_orders = len(orders)
    num_raw_lengths = len(raw_lengths)

    # Initialize memoization table
    memo = [[math.inf] * (num_orders + 1) for _ in range(num_raw_lengths + 1)]

    # Initialize base cases
    for i in range(num_raw_lengths + 1):
        memo[i][0] = 0

    # Dynamic programming to fill the memoization table
    for i in range(1, num_raw_lengths + 1):
        for j in range(1, num_orders + 1):
            for k in range(1, min(j + 1, num_orders + 1)):
                length_used = sum(order[0] * order[1] for order in orders[j - k : j])
                if length_used <= raw_lengths[i - 1]:
                    memo[i][j] = min(memo[i][j], 1 + memo[i][j - k])

    # Trace back to find the optimal solution
    remaining_orders = num_orders
    remaining_lengths = num_raw_lengths
    solution = []
    repeats = defaultdict(int)
    while remaining_orders > 0:
        for k in range(min(remaining_orders, num_orders), 0, -1):
            length_used = sum(
                order[0] * order[1]
                for order in orders[remaining_orders - k : remaining_orders]
            )
            if (
                length_used <= raw_lengths[remaining_lengths - 1]
                and memo[remaining_lengths][remaining_orders]
                == 1 + memo[remaining_lengths][remaining_orders - k]
            ):
                pattern = tuple(orders[remaining_orders - k : remaining_orders])
                solution.append(pattern)
                repeats[pattern] += 1
                remaining_orders -= k
                break
        remaining_lengths -= 1

    return solution, repeats


def main():
    # Example input: raw lengths and orders with (length, quantity) pairs
    raw_lengths = [100, 200, 300]
    orders = [(30, 3), (60, 2), (80, 4), (90, 1), (120, 5), (150, 2), (180, 3)]

    # Solve the Cutting Stock Problem
    solution, repeats = cutting_stock(raw_lengths, orders)

    # Print the solution
    print("Optimal cutting pattern:")
    for pattern in solution:
        print(pattern)

    # Print repeats
    print("\nRepeats:")
    for pattern, count in repeats.items():
        print(f"{pattern}: {count} times")


if __name__ == "__main__":
    main()
