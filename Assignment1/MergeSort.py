'''
Andrew Cunningham
CSC505 - Assignment 1

Task: Compile, run, and submit a program.

Implementation of MergeSort
Usage: py MergeSort.py *array to be sorted, integers seperated by a space*(optional, generates a random array len 5-10 if blank)
Ref:
https://www.geeksforgeeks.org/merge-sort/
https://towardsdatascience.com/sorting-algorithms-with-python-4ec7081d78a1
'''

import random
import sys

DEBUG = False

def merge(arr_i, arr_j):
    '''returns a list of the two arrays merged and sorted in incrementing order'''
    merged = [] # empty array to start
    i = 0 # tracks location in arr_i
    j = 0 # tracks location in arr_j

    # merge the arrays togehter until one of them have run out
    while(i <= len(arr_i) - 1 and j <= len(arr_j) - 1):
        if arr_i[i] < arr_j[j]:
            merged.append(arr_i[i])
            i += 1
        else:
            merged.append(arr_j[j])
            j += 1

    # one of the arrays is now empty and we can safely append the rest of both arrays
    while i < len(arr_i):
        merged.append(arr_i[i])
        i += 1
    while j < len(arr_j):
        merged.append(arr_j[j])
        j += 1
    return merged


def merge_sort(arr):
    '''
    Recursively sorts the array by splitting it in half until length is 1
    Then merge the 2 halves together, placing the smallest int first for each step
    '''
    # if length = 1, return
    if len(arr) <= 1:
        return arr
    # split the array in half

    mid = (len(arr) - 1) // 2
    
    # merge sort left
    list1 = arr[:mid+1]
    list2 = arr[mid+1:]

    list1 = merge_sort(arr[:mid+1])
    list2 = merge_sort(arr[mid+1:])

    # merge sort right
    merged = merge(list1, list2)

    return merged



if __name__ == "__main__":
    # First, determine if args has been provided
    if len(sys.argv) > 1:
        # args has been provided, convery the array of strings into an array of ints
        base_array = list(map(int, sys.argv[1].split()))
    else:
        # No args has been given, generate an array of len 5-10 with random ints 0-100
        base_array = [random.randint(0,100) for _ in range(random.randint(5,10))]

    debug(len(base_array))

    print(f"Inputted array: {" ".join(map(str, base_array))}")

    sorted_array = merge_sort(base_array)
    
    print(f"Sorted Array:   {" ".join(map(str, sorted_array))}")




