import argparse
import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


list_sizes = [500, 1000, 5000]

n500 = list_sizes[0]
n1000 = list_sizes[1]
n5000 = list_sizes[2]


def getAverageTimesequential_search(list):
    total_time = 0
    for i in range(100):
        myList = get_me_random_list(list)
        start = time.time()
        sequential_search(myList, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    return total_time / 100

def getAverageTimeordered_sequential_search(list):
    total_time = 0
    for i in range(100):
        myList = get_me_random_list(list)
        start = time.time()
        ordered_sequential_search(myList, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    return total_time / 100

def getAverageTimebinary_search_iterative(list):
    total_time = 0
    for i in range(100):
        myList = get_me_random_list(list)
        start = time.time()
        binary_search_iterative(myList, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    return total_time / 100

def getAverageTimebinary_search_recursive(list):
    total_time = 0
    for i in range(100):
        myList = get_me_random_list(list)
        start = time.time()
        binary_search_recursive(myList, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    return total_time / 100
def main():
    avg_time = getAverageTimesequential_search(n500)
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")

    avg_time = getAverageTimesequential_search(n1000)
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")

    avg_time = getAverageTimesequential_search(n5000)
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    avg_time = getAverageTimeordered_sequential_search(n500)
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")

    avg_time = getAverageTimeordered_sequential_search(n1000)
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")

    avg_time = getAverageTimeordered_sequential_search(n5000)
    print(f"ordered sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    avg_time = getAverageTimebinary_search_iterative(n500)
    print(f"binary search iterative took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")

    avg_time = getAverageTimebinary_search_iterative(n1000)
    print(f"binary search iterative took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")

    avg_time = getAverageTimebinary_search_iterative(n5000)
    print(f"binary search iterative took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    avg_time = getAverageTimebinary_search_recursive(n500)
    print(f"binary search recursive took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")

    avg_time = getAverageTimebinary_search_recursive(n1000)
    print(f"binary search recursive took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")

    avg_time = getAverageTimebinary_search_recursive(n5000)
    print(f"binary search recursive took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")


main()

if __name__ == "__main__":
    """Main entry point"""
