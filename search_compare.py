"""Compare four search algorithms using 100 lists per size."""

import random
from time import perf_counter


def sequential_search(numbers, item):
    start = perf_counter()
    position = 0
    found = False
    while position < len(numbers) and not found:
        if numbers[position] == item:
            found = True
        else:
            position += 1
    return found, perf_counter() - start


def ordered_sequential_search(numbers, item):
    """Search an ascending sorted list."""
    start = perf_counter()
    position = 0
    found = False
    stop = False
    while position < len(numbers) and not found and not stop:
        if numbers[position] == item:
            found = True
        elif numbers[position] > item:
            stop = True
        else:
            position += 1
    return found, perf_counter() - start


def binary_search_iterative(numbers, item):
    """Search an ascending sorted list."""
    start = perf_counter()
    first = 0
    last = len(numbers) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if numbers[midpoint] == item:
            found = True
        elif item < numbers[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return found, perf_counter() - start


def binary_search_recursive(numbers, item):
    """Time the entire recursive search, including list slicing."""
    def search(values):
        if not values:
            return False
        midpoint = len(values) // 2
        if values[midpoint] == item:
            return True
        if item < values[midpoint]:
            return search(values[:midpoint])
        return search(values[midpoint + 1:])

    start = perf_counter()
    found = search(numbers)
    return found, perf_counter() - start


def main():
    algorithms = [
        ("Sequential Search", sequential_search),
        ("Ordered Sequential Search", ordered_sequential_search),
        ("Iterative Binary Search", binary_search_iterative),
        ("Recursive Binary Search", binary_search_recursive),
    ]
    for size in (500, 1000, 5000):
        totals = [0.0] * len(algorithms)
        for _ in range(100):
            # The missing target is greater than every generated number.
            numbers = [random.randint(1, 1000000) for _ in range(size)]
            _, elapsed = sequential_search(numbers, 99999999)
            totals[0] += elapsed
            numbers.sort()  # Sorting is outside every search timer.
            for index in range(1, len(algorithms)):
                _, elapsed = algorithms[index][1](numbers, 99999999)
                totals[index] += elapsed
        print(f"\nList size: {size}")
        for (name, _), total in zip(algorithms, totals):
            time_taken = total / 100
            print(f"{name} took {time_taken:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
