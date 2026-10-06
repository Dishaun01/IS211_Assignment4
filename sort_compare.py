"""Compare three sorting algorithms using 100 lists per size."""

import random
from time import perf_counter


def insertion_sort(numbers):
    start = perf_counter()
    for index in range(1, len(numbers)):
        current = numbers[index]
        position = index
        while position > 0 and numbers[position - 1] > current:
            numbers[position] = numbers[position - 1]
            position -= 1
        numbers[position] = current
    return numbers, perf_counter() - start


def shell_sort(numbers):
    start = perf_counter()
    gap = len(numbers) // 2
    while gap > 0:
        for start_position in range(gap):
            for index in range(start_position + gap, len(numbers), gap):
                current = numbers[index]
                position = index
                while position >= gap and numbers[position - gap] > current:
                    numbers[position] = numbers[position - gap]
                    position -= gap
                numbers[position] = current
        gap //= 2
    return numbers, perf_counter() - start


def python_sort(numbers):
    start = perf_counter()
    numbers.sort()
    return numbers, perf_counter() - start


def main():
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Python Sort", python_sort),
    ]
    for size in (500, 1000, 5000):
        totals = [0.0] * len(algorithms)
        for _ in range(100):
            numbers = [random.randint(1, 1000000) for _ in range(size)]
            for index, (_, algorithm) in enumerate(algorithms):
                # Give each algorithm identical unsorted data; copy before timing.
                _, elapsed = algorithm(numbers.copy())
                totals[index] += elapsed
        print(f"\nList size: {size}")
        for (name, _), total in zip(algorithms, totals):
            time_taken = total / 100
            print(f"{name} took {time_taken:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
