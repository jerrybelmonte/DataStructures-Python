# Data Structures in Python
Data structures and algorithm implementations in Python.

## Table of Contents
* [Objective](#objective)
* [List ADT](#list-adt)
  - [Binary Search on Sorted List](#binary-search-on-sorted-list)
  - [Quicksort Unsorted List](#quicksort-unsorted-list)
  - [Linked List](#linked-list)
* [Stack ADT](#stack-adt)
  - [Check Brackets In Text](#check-brackets-in-text)
* [Queue ADT](#queue-adt)
  - [Convert Array Into Heap](#convert-array-into-heap)
* [Technologies](#technologies)
* [License](#license)

## Objective
Practice implementing various data structures to gain experience designing data structures and algorithms in Python.

## List ADT

### Binary Search on Sorted List
[Binary Search](binarysearch.py "binarysearch.py")

### Quicksort Unsorted List
[Quicksort](quicksort.py "quicksort.py")

### Linked List
[LinkedList](linkedlist.py "linkedlist.py")


## Stack ADT
[Stack](stack.py "stack.py")

### Check Brackets In Text
[Check Brackets](check_brackets.py "check_brackets.py")

## Queue ADT
[Queue](queue.py "queue.py")

### Convert Array Into Heap
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. Implement the first step 
and convert a given array of integers into a heap. Goal is to convert the array into a heap using only **O(n)** swaps. 
Note: implementation is a min-heap.  
**Input:** First line contains a single integer _n_. Next line contains _n_ space-separated integers _ai_ 
(_1 <= n <= 100,000; 0 <= i,j <= n-1; 0 <= a0,...,an-1 <= 10e9_).  
**Output:** First line should containt single integer _m_ (the total number of swaps) and _m_ **must satisfy conditions** 
_0 <= m <= 4n_. The next _m_ lines should contain the swap operations used to convert the array _a_ into a heap.  
[Heapify](build_heap.py "build_heap.py")


## Technologies
Python 3.8

## License
This project is licensed under the terms of the **MIT** license. See the [LICENSE](LICENSE) file for details.
