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
* [Hashing](#hashing)
  - [Phone Book](#phone-book)
* [Technologies](#technologies)
* [License](#license)


## Objective
Practice implementing various data structures to gain experience designing data structures and algorithms in Python.


## List ADT

### Binary Search on Sorted List
Implementation for a simple binary search algorithm on a sorted list.  
**Code:** [Binary Search](binarysearch.py "binarysearch.py")

### Quicksort Unsorted List
Implementation for a simple Quicksort algorithm on an unsorted list.  
**Code:** [Quicksort](quicksort.py "quicksort.py")

### Linked List
Implementation for a simple LinkedList data structure.  
**Code:** [LinkedList](linkedlist.py "linkedlist.py")


## Stack ADT
Implementation for a simple stack data structure.  
**Code:** [Stack](stack.py "stack.py")

### Check Brackets In Text
Implement a feature for a text editor to find errors in the usage of brackets in the code.  

**Input:** Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and 
brackets from the set []{}().  
**Constraints:** _The length of 𝑆 is at least 1 and at most 10^5_.  
**Output:** If the code in 𝑆 uses brackets correctly, outputs “`Success`". Otherwise, outputs the 1-based index of the 
first unmatched closing bracket, and if there are no unmatched closing brackets, outputs the 1-based index of the first 
unmatched opening bracket.  
**Code:** [Check Brackets](check_brackets.py "check_brackets.py")

### Stack With Maximum
Stack is an abstract data type supporting the operations `Push()` and `Pop()`. Implement both these operations to work 
in constant time. Implement a stack that also supports finding the maximum value and to ensure that all operations 
still work in constant time.  

**Input:** The first line of the input contains the number 𝑞 of queries. Each of the following 𝑞 lines specifies a query 
of one of the following formats: `push v`, `pop`, or `max`.  
**Constraints:** _1 ≤ 𝑞 ≤ 40,0000; 0 ≤ 𝑣 ≤ 10^5_.  
**Output:** For each max query, output (on a separate line) the maximum value of the stack.  
**Code:** [Max Stack](max_stack.py "max_stack.py")


## Queue ADT
Implementation for a simple queue data structure.  
**Code:** [Queue](queue.py "queue.py")

### Maximum In Sliding Window
Given a sequence 𝑎1,...,𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖,...,𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 
𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Design an 𝑂(𝑛) algorithm.  

**Input:** The first line contains an integer 𝑛, the second line contains 𝑛 integers 𝑎1,...,𝑎𝑛 separated by spaces, 
the third line contains an integer 𝑚.  
**Constraints:** _1 ≤ 𝑛 ≤ 10^5, 1 ≤ 𝑚 ≤ 𝑛, 0 ≤ 𝑎𝑖 ≤ 10^5 for all 1 ≤ 𝑖 ≤ 𝑛_.  
**Output:** Output max{𝑎𝑖,...,𝑎𝑖 + 𝑚 − 1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1.  
**Code:** [Max Sliding Window](max_sliding_window.py "max_sliding_window.py")

### Convert Array Into Heap
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. Implement the first step 
and convert a given array of integers into a min-heap. Convert the array into a heap using only 𝑂(𝑛) swaps.  

**Input:** First line contains a single integer 𝑛. Next line contains 𝑛 space-separated integers 𝑎𝑖.  
**Constraints:** _1 ≤ 𝑛 ≤ 100,000; 0 ≤ i,j ≤ 𝑛-1; 0 ≤ 𝑎0,...,𝑎𝑛-1 ≤ 10^9_.  
**Output:** First line should contain a single integer 𝑚 (the total number of swaps) and 𝑚 **must satisfy conditions** 
_0 ≤ 𝑚 ≤ 4𝑛_. The next 𝑚 lines should contain the swap operations used to convert the array 𝑎 into a heap.  
**Code:** [Heapify](build_heap.py "build_heap.py")

### Parallel Processing
You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads 
take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from 
the list. If a thread has started processing a job, it doesn't interrupt or stop until it finishes processing the job. 
If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each 
job you know exactly how long will it take any thread to process this job, and this time is the same for all the 
threads. You need to determine for each job which thread will process it and when will it start processing.  

**Input:** The first line of the input contains integers 𝑛 and 𝑚. The second line contains 𝑚 integers 𝑡𝑖 — the times in 
seconds it takes any thread to process 𝑖-th job. The times are given in the same order as they are in the list from 
which threads take jobs. Threads are indexed starting from 0.  
**Constraints:** _1 ≤ 𝑛 ≤ 10; 1 ≤ 𝑚 ≤ 10; 0 ≤ 𝑡𝑖 ≤ 10_.  
**Output:** Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two space separated integers, 
the 0-based index of the thread which will process the 𝑖-th job and the time in seconds when it will start processing 
that job.  
**Code:** [Priority Queue](job_queue.py "job_queue.py")


## Hashing

### Phone Book
Implement a simple phone book manager that should be able to process the following types of user's queries:
- **`add`** _`number name`_. The user adds a person with name `name` and phone number `number` to the phone book. 
If there exists a user with such number already, then the manager overwrites the corresponding name.
- **`del`** _`number`_. The manager erases a person with number `number` from the phone book. If there is no such 
person, then it ignores the query.
- **`find`** _`number`_. The user looks for a person with phone number `number`. The manager replies with the 
appropriate name, or with string “`not found`" if there is no such person in the book.

**Input:** There is a single integer 𝑁 in the first line (the number of queries). It’s followed by 𝑁 lines, each of 
them contains one query in the format described above.  
**Constraints:** _1 ≤ 𝑁 ≤ 10^5_. All phone numbers consist of decimal digits, 
they don’t have leading zeros, and each of them has no more than 7 digits. All names are non-empty strings of latin 
letters, and each of them has length at most 15. It’s guaranteed that there is no person with name “not found".  
**Output:** Print the result of each find query — the name corresponding to the phone number or “not found" (without 
quotes) if there is no person in the phone book with such phone number. Output one result per line in the same order 
as the find queries are given in the input.  
**Code:** [Phone Book](phone_book.py "phone_book.py")


## Technologies
* Python 3.8
* PyCharm (Professional Edition) - Version: 2020.2.5
* Visual Studio Code - Version: 1.51.1


## License
This project is licensed under the terms of the **MIT** license. See the [LICENSE](LICENSE) file for details.
