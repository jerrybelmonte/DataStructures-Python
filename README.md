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
  - [Stack With Maximum](#stack-with-maximum)
* [Queue ADT](#queue-adt)
  - [Maximum In Sliding Window](#maximum-in-sliding-window)
  - [Convert Array Into Heap](#convert-array-into-heap)
  - [Parallel Processing](#parallel-processing)
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
Implement a feature for a text editor to find errors in the usage of brackets in the code.  
**Input:** Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and 
brackets from the set []{}() _(The length of 𝑆 is at least 1 and at most 10E5)_.  
**Output:** If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 
1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 
1-based index of the first unmatched opening bracket.  
[Check Brackets](check_brackets.py "check_brackets.py")

### Stack With Maximum
Stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implement it in a way 
that both these operations work in constant time. In this problem, you goal will be to implement a stack that also 
supports finding the maximum value and to ensure that all operations still work in constant time.  
**Input:** The first line of the input contains the number 𝑞 of queries. Each of the following 𝑞 lines specifies a query 
of one of the following formats: push v, pop, or max _(1 ≤ 𝑞 ≤ 40,0000; 0 ≤ 𝑣 ≤ 10E5)_.  
**Output:** For each max query, output (on a separate line) the maximum value of the stack.  
[Max Stack](max_stack.py "max_stack.py")

## Queue ADT
[Queue](queue.py "queue.py")

### Maximum In Sliding Window
Given a sequence 𝑎1,...,𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖,...,𝑎𝑖+𝑚−1} for every 
1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Your goal is to 
design an 𝑂(𝑛) algorithm.  
**Input:** The first line contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1,...,𝑎𝑛 separated by spaces, 
the third line contains an integer 𝑚 _(1 ≤ 𝑛 ≤ 10E5,1 ≤ 𝑚 ≤ 𝑛,0 ≤ 𝑎𝑖 ≤ 10E5 for all 1 ≤ 𝑖 ≤ 𝑛)_.  
**Output:** Output max{𝑎𝑖,...,𝑎𝑖 + 𝑚 − 1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.  
[Max Sliding Window](max_sliding_window.py "max_sliding_window.py")

### Convert Array Into Heap
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. Implement the first step 
and convert a given array of integers into a heap. Goal is to convert the array into a heap using only **O(n)** swaps. 
Note: implementation is a min-heap.  
**Input:** First line contains a single integer _n_. Next line contains _n_ space-separated integers _ai_ 
(_1 <= n <= 100,000; 0 <= i,j <= n-1; 0 <= a0,...,an-1 <= 10e9_).  
**Output:** First line should containt single integer _m_ (the total number of swaps) and _m_ **must satisfy conditions** 
_0 <= m <= 4n_. The next _m_ lines should contain the swap operations used to convert the array _a_ into a heap.  
[Heapify](build_heap.py "build_heap.py")

### Parallel Processing
You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads 
take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from 
the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. 
If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each 
job you know exactly how long will it take any thread to process this job, and this time is the same for all the threads. 
You need to determine for each job which thread will process it and when will it start processing.  
**Input:** The first line of the input contains integers 𝑛 and 𝑚. The second line contains 𝑚 integers 𝑡𝑖 — the times in 
seconds it takes any thread to process 𝑖-th job. The times are given in the same order as they are in the list from 
which threads take jobs. Threads are indexed starting from 0. _(1 ≤ 𝑛 ≤ 10; 1 ≤ 𝑚 ≤ 10; 0 ≤ 𝑡𝑖 ≤ 10)_.  
**Output:** Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two space separated integers, the 
0-based index of the thread which will process the 𝑖-th job and the time in seconds when it will start processing that job.  
[Priority Queue](job_queue.py "job_queue.py")


## Technologies
Python 3.8

## License
This project is licensed under the terms of the **MIT** license. See the [LICENSE](LICENSE) file for details.
