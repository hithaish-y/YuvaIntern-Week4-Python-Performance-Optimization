import time


def calculate_total(numbers):
    total = 0

    for number in numbers:
        time.sleep(0.01)
        total += number

    return total


def find_duplicates(numbers):
    duplicates = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])

    return duplicates


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