import time


def calculate_total(numbers):
    return sum(numbers)


def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return sorted(duplicates)


def process_data(numbers):
    total = calculate_total(numbers)
    duplicates = find_duplicates(numbers)

    return total, duplicates


if __name__ == "__main__":
    data = list(range(1, 101)) + [25, 50, 75]

    start_time = time.time()

    total, duplicates = process_data(data)

    end_time = time.time()

    print("Total:", total)
    print("Duplicates:", duplicates)
    print("Execution time:", round(end_time - start_time, 4), "seconds")