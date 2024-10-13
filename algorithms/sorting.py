"""
sorting.py - Sorting algorithms for sorting a list of numbers.

This file contains the following sorting algorithms:
    - quicksort: An efficient, recursive algorithm that uses a pivot to partition the array into two halves.
                 Average time complexity is O(n log n), worst-case is O(n^2).
    - bubblesort: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements,
                  and swaps them if they are in the wrong order. Average and worst-case time complexity is O(n^2).
    - mergesort: A divide-and-conquer algorithm that divides the list into halves, sorts them, and merges them back together.
                 Time complexity is O(n log n).
    - insertion_sort: A simple algorithm that builds the sorted array one item at a time,
                      by repeatedly picking the next element and inserting it into the correct position.
                      Average and worst-case time complexity is O(n^2).
    - selection_sort: An in-place comparison-based algorithm that divides the input list into a sorted and an unsorted region,
                      and iteratively selects the smallest (or largest) element from the unsorted region to place into the sorted region.
                      Time complexity is O(n^2).
    - heap_sort: An efficient comparison-based sorting algorithm that uses a binary heap data structure to create a sorted array.
                 Time complexity is O(n log n).
    - shell_sort: A generalization of insertion sort that allows the exchange of items far apart.
                  The idea is to arrange the list of elements so that, starting anywhere, taking every h-th element produces a sorted list.
                  Average time complexity is O(n log n).
    - counting_sort: A non-comparison based sorting algorithm that counts the number of occurrences of each unique element.
                     It is efficient for sorting integers within a limited range. Time complexity is O(n + k), where k is the range of the input.
    - radix_sort: A non-comparison based sorting algorithm that sorts integers by processing individual digits.
                  Time complexity is O(nk), where k is the number of digits.
    - bucket_sort: A distribution-based sorting algorithm that divides the elements into several buckets,
                   sorts each bucket, and then concatenates the results. Time complexity is O(n + k).
    - tim_sort: A hybrid sorting algorithm derived from merge sort and insertion sort, used in Python’s built-in sorted() function.
                Time complexity is O(n log n).
    - cocktail_sort: A variation of bubble sort that sorts in both directions on each pass through the list.
                     Average and worst-case time complexity is O(n^2).
    - gnome_sort: A simple comparison-based sorting algorithm that is similar to insertion sort but uses a different approach for sorting.
                  Average and worst-case time complexity is O(n^2).
    - bitonic_sort: A parallel sorting algorithm that works by dividing the array into bitonic sequences and merging them.
                    Time complexity is O(log^2 n) in parallel computing.
    - pancake_sort: A sorting algorithm that uses a series of flips to sort an array, similar to sorting pancakes by size.
                    Time complexity is O(n).
    - cycle_sort: An in-place, non-comparison based sorting algorithm that is optimal in terms of the number of writes.
                  Time complexity is O(n^2).
    - stooge_sort: A recursive sorting algorithm that sorts in O(n^(log 3 / log 1.5)) time, primarily for educational purposes.
    - strand_sort: A stable sorting algorithm that recursively builds a sorted list from the input list by removing "strands" of sorted elements.
                   Average time complexity is O(n^2).
    - bogo_sort: A highly ineffective sorting algorithm that randomly permutes the array until it is sorted.
                 Average time complexity is O((n + 1)!) and is impractical for real sorting tasks.
    - sleep_sort: A joke sorting algorithm that sleeps for a duration proportional to the value of each element.
                  Time complexity is unbounded due to sleep time.
    - gravity_sort: A non-standard, humorous sorting algorithm that simulates the effect of gravity on balls of different weights.
                    Time complexity is not defined.
    - quantum_bogo_sort: A theoretical sorting algorithm that uses quantum mechanics to sort the elements, not practically feasible.
                          Time complexity is unbounded.
    - miracle_sort: A humorous concept that suggests a sorting algorithm that sorts elements instantly.
                    Time complexity is not defined.

(Yes, even the joke ones are included)
"""

import threading
from typing import List
import time
import random


def quicksort(arr: List[int]) -> List[int]:
    """
    Quicksort is an efficient, recursive algorithm that uses a pivot to partition the array into two halves.
    Average time complexity is O(n log n), worst-case is O(n^2).

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def quantum_bogo_sort(arr: List[int]) -> List[int]:
    """
    Quantum Bogo Sort is a theoretical sorting algorithm that uses quantum mechanics to sort the elements.
    It is not practically feasible and is included here for humor.

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    return (
        arr  # The elements are already in a superposition of sorted and unsorted states
    )


def bogo_sort(arr: List[int]) -> List[int]:
    """
    Bogo Sort is a highly ineffective sorting algorithm that randomly permutes the array until it is sorted.
    Average time complexity is O((n + 1)!) and is impractical for real sorting tasks.

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    while not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        random.shuffle(arr)
    return arr


def miracle_sort(arr: List[int]) -> List[int]:
    """
    Miracle Sort is a humorous concept that suggests a sorting algorithm that sorts elements instantly.
    It is not practically feasible and is included here for humor.

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    return sorted(arr)


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Sleep Sort is a joke sorting algorithm that sleeps for a duration proportional to the value of each element.
    Time complexity is unbounded due to sleep time.

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    sorted_arr = []

    def sleep_and_append(x):
        time.sleep(x)
        sorted_arr.append(x)

    threads = [threading.Thread(target=sleep_and_append, args=(x,)) for x in arr]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return sorted_arr


def gravity_sort(arr: List[int]) -> List[int]:
    """
    Gravity Sort is a non-standard, humorous sorting algorithm that simulates the effect of gravity on balls of different weights.
    Time complexity is not defined.

    :param arr: List[int] - The list of numbers to sort.
    :return: List[int] - The sorted list.
    """
    return sorted(arr, reverse=True)
