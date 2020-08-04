# QuickSort implementation with first index as the pivot
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller = [i for i in array[1:] if i <= pivot]
        larger = [i for i in array[1:] if i > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quick_sort(test))
