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


def main():
    list_sizes = [500, 1000, 5000]

    n500 = list_sizes[0]
    n1000 = list_sizes[1]
    n5000 = list_sizes[2]

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(n500)
        mylist1000 = get_me_random_list(n1000)
        mylist5000 = get_me_random_list(n5000)
        start = time.time()
        sequential_search(mylist500, 9999)
        sequential_search(mylist1000, 9999)
        sequential_search(mylist5000, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")
    print(f"sequential search took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")
    print(f"sequential search {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(n500)
        mylist1000 = get_me_random_list(n1000)
        mylist5000 = get_me_random_list(n5000)
        start = time.time()
        ordered_sequential_search(mylist500, 9999)
        ordered_sequential_search(mylist1000, 9999)
        ordered_sequential_search(mylist5000, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"ordered_sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")
    print(f"ordered_sequential_search  took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")
    print(f"ordered_sequential_search  took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(n500)
        mylist1000 = get_me_random_list(n1000)
        mylist5000 = get_me_random_list(n5000)
        start = time.time()
        binary_search_iterative(mylist500, 9999)
        binary_search_iterative(mylist1000, 9999)
        binary_search_iterative(mylist5000, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")
    print(f"binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")
    print(f"binary_search_iterative took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(n500)
        mylist1000 = get_me_random_list(n1000)
        mylist5000 = get_me_random_list(n5000)
        start = time.time()
        ordered_sequential_search(mylist500, 9999)
        ordered_sequential_search(mylist1000, 9999)
        ordered_sequential_search(mylist5000, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"ordered_sequential_search took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")
    print(f"ordered_sequential_search  took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")
    print(f"ordered_sequential_search  took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")

    total_time = 0
    for i in range(100):
        mylist500 = get_me_random_list(n500)
        mylist1000 = get_me_random_list(n1000)
        mylist5000 = get_me_random_list(n5000)
        start = time.time()
        binary_search_recursive(mylist500, 9999)
        binary_search_recursive(mylist1000, 9999)
        binary_search_recursive(mylist5000, 9999)
        time_spent = time.time() - start
        total_time += time_spent

    avg_time = total_time / 100
    print(f"binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {n500} elements")
    print(f"binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {n1000} elements")
    print(f"binary_search_recursive took {avg_time:10.7f} seconds to run, on average for a list of {n5000} elements")


main()

if __name__ == "__main__":
    """Main entry point"""
