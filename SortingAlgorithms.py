
def insertionsort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        j = i
        key = unsorted_list[i]
        while j > 0 and unsorted_list[j - 1] > key:
            unsorted_list[j] = unsorted_list[j - 1]     # inner loop over sorted part
            j -= 1
            unsorted_list[j] = key


def selectionsort(unsorted_list):
    for i in range(0, len(unsorted_list)):
        jmin = i
        j = i + 1
        key = unsorted_list[i]
        while j < len(unsorted_list):
            if unsorted_list[j] < unsorted_list[jmin]:      # inner loop over unsorted part
                key = unsorted_list[j]
                jmin = j
            j += 1
        unsorted_list[jmin], unsorted_list[i] = unsorted_list[i], unsorted_list[jmin]


def bubblesort(unsorted_array):
    for k in range(1, len(unsorted_array)):
        flag = 0
        for i in range(0, len(unsorted_array) - k):
            if unsorted_array[i] > unsorted_array[i+1]:
                unsorted_array[i], unsorted_array[i+1] = unsorted_array[i+1], unsorted_array[i]
                flag = 1
        if flag == 0:
            break


def mergesort(unsorted_array):
    if len(unsorted_array) < 2:
        return unsorted_array
    else:
        mid = len(unsorted_array)//2
        return merge(mergesort(unsorted_array[:mid]), mergesort(unsorted_array[mid:]))


def merge(left, right):
    combined = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combined.append(left[i])
            i += 1
        elif left[i] > right[j]:
            combined.append(right[j])
            j += 1
    while i < len(left):
        combined.append(left[i])
        i += 1
    while j < len(right):
        combined.append(right[j])
        j += 1
    return combined

def quicksort(unsorted_array, start, end):
    if start < end:
        pindex = partition(unsorted_array, start, end)
        quicksort(unsorted_array, start, pindex - 1)
        quicksort(unsorted_array, pindex + 1, end)


def partition(array, start, end):
    pivot = array[end]
    pindex = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[pindex] = array[pindex], array[i]
            pindex += 1
    array[pindex], array[end] = array[end], array[pindex]
    return pindex


numbers = [9,4,5,35,7,5,31,85,87,632,15,66,4,44,9,6,416,94,9,166,98,6]
quicksort(numbers, 0, len(numbers) - 1)
print(numbers)     # [4, 4, 5, 5, 6, 6, 7, 9, 9, 9, 15, 31, 35, 44, 66, 85, 87, 94, 98, 166, 416, 632]



