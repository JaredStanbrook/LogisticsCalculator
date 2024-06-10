def first_fit_decreasing(item_sizes, bin_capacity):
    # Sort items in descending order
    item_sizes.sort(reverse=True)

    bins = [[]]  # Initialize the first bin

    for item in item_sizes:
        # Try to place the item in the first bin where it fits
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                break
        else:
            # If no bin can accommodate the item, start a new bin
            bins.append([item])

    return bins


def main():
    # Example input: item sizes and warehouse space
    item_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    bin_capacity = 100

    # Apply the first-fit decreasing algorithm
    bins = first_fit_decreasing(item_sizes, bin_capacity)

    # Print the results
    for i, bin in enumerate(bins):
        print(f"Bin {i + 1}: {bin}")
    print(f"Total bins used: {len(bins)}")


if __name__ == "__main__":
    main()
