import random

def generate_numbers(count, low, high):
<<<<<<< HEAD
    return [random.randint(low, high) for _ in range(count)]
=======
    return [random.randint(low, high) for _ in range(count)]
>>>>>>> feature/login-page

def average(numFbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def find_odd(numbers):
    return [n for n in numbers if n % 2 != 0]

def summarize(numbers):
    if not numbers:
        return {}
    return {
        "count": len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "average": round(average(numbers), 2),
        "sum": sum(numbers)
    }

def main():
    numbers = generate_numbers(20, 1, 100)

    print("Random numbers:")
    print(numbers)

    print("\nSummary:")
    stats = summarize(numbers)

    for key, value in stats.items():
        print(f"{key}: {value}")

    even = find_even(numbers)
    odd = find_odd(numbers)

    print("\nEven numbers:")
    print(even)

    print("\nOdd numbers:")
    print(odd)

    largest = max(numbers)
    smallest = min(numbers)

    print(f"\nLargest number: {largest}")
    print(f"Smallest number: {smallest}")

    shuffled = numbers.copy()
    random.shuffle(shuffled)

    print("\nShuffled numbers:")
    print("3, 2, 5, 7, 4, 3, 4")


if __name__ == "__main__":
    main()
