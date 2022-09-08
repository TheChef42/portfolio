import random
from timeit import default_timer as timer

def generate_sorted_list(low, high, size):
    """Generates a list of size elements of sorted numbers from start to end"""
    numbers = random.sample(range(low, high), size)
    numbers.sort()
    return numbers


def linear_search(numbers, key):
    """Return the index where key is found in numbers, -1 if not found"""
    # TODO: implement this
    index = -1
    i = 0
    while i < len(numbers) and index != key:
        if numbers[i] == key:
            index = i
        i += 1
    return index



def binary_search(numbers, start, end, key):
    """Return the index where key is found in numbers, -1 if not found"""
    # TODO: implement this
    index = -1
    while index != key:
        middle = start + (end - start) / 2
        if numbers[middle] < key:
            start = middle + 1
        if numbers[middle] > key:
            end = middle - 1
        if numbers[middle] == key:
            index == key
            return middle
    return key










def main():
    low = 0
    high = 1000
    size = 100
    numbers = generate_sorted_list(low, high, size)

    # Let's measure the time it takes to find a random number in the list and plot the times for both algorithms
    k = random.randint(low, high)

    # Linear search time
    time_start = timer()
    result = linear_search(numbers, k)
    elapsed_time = timer() - time_start
    print("linear_search ","Result", result, size, elapsed_time)

    # Binary search time
    time_start = timer()
    result2 = binary_search(numbers, low, high, k)
    elapsed_time = timer() - time_start
    print("binary_search","Result", result2, size, elapsed_time)


if __name__ == '__main__':
    main()