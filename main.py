def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]
    lower = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    higher = [value for value in values if value > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)


if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print("Original:", sample)
    print("Sorted:", quick_sort(sample))
