#Nolan Frost
#Sorting Methods

def bubbleSort(alist):
    '''
Bubble Sort:
1. Stable
2. In-place
3. Typically multiple swaps are made per pass, so it requires the most swaps in total. Run-time is always O(n^2).
4. Should usually be avoided because of the high amount of swaps compared to other methods, but it is one of the easiest sorting methods to code.
    '''
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp

def selectionSort(alist):
    '''
Selection Sort:
1. Not stable
2. In-place, but requires extra space for four temporary variables
3. At most only n swaps are made. Run-time is always O(n^2).
4. Minimizes swaps, so use when cost of swapping items is high.
    '''
    for i in range(len(alist) - 1, 0, -1):
       maxIndex = 0
       for j in range(1, i + 1):
           if alist[j] > alist[maxIndex]:
               maxIndex = j

       temp = alist[i]
       alist[i] = alist[maxIndex]
       alist[maxIndex] = temp

def insertionSort(alist):
    '''
Insertion Sort:
1. Stable
2. In-place, but requires extra space for three temporary variables
3. Best Case: O(n) if list is sorted. Average and Worst Cases: O(n^2). At most n + 1 comparisons and n copies.
4. Works best on small lists because the sorted sublists minimize the number of swaps.
    '''
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue

def mergeSort(alist):
    '''
Merge Sort:
1. Stable
2. Not in-place, requires extra n memory for the sublists and three variables
3. Run-time of O(nlogn) maintained regardless of the order of the list
4. Best to use when run-time is prioritized over memory because it is fast but requires more extra storage than the rest of the sorting methods
    '''
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1

def quickSort(alist):
    '''
Quick Sort:
1. Not stable
2. Sorts in-place but requires temporary space to swap variables as well as space for activation records from recursive calls
3. Best Case: O(nlogn) when pivot is in middle. Worst Case: O(n^2) when pivot is at beginning or end (meaning the list is sorted).
4. Best used on large unordered data sets because it can be much faster than merge sort and use less memory. Weak when list is ordered.
    '''
    quickSortRecursion(alist, 0, len(alist) - 1)

def quickSortRecursion(alist, first, last):
   if first < last:

       split = partition(alist, first, last)

       quickSortRecursion(alist, first, split - 1)
       quickSortRecursion(alist, split + 1, last)

def partition(alist, first, last):
   pivotValue = alist[first]

   leftmark = first + 1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotValue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotValue and rightmark >= leftmark:
           rightmark = rightmark - 1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def main():

    print("List is [7, -3, 4, 9, 7, 2, 1, 4, 2, 7, 0, 9, -5, 16, 2, 27, -3], sorting using Bubble Sort.")
    list1 = [7, -3, 4, 9, 7, 2, 1, 4, 2, 7, 0, 9, -5, 16, 2, 27, -3]
    bubbleSort(list1)
    print("Sorted List: ", list1)
    print(bubbleSort.__doc__)
    print()
    print("List is [9, 5, -3, 42, 19, -27, -4, 0, 13, 30, -11, 2, 6], sorting using Selection Sort.")
    list2 = [9, 5, -3, 42, 19, -27, -4, 0, 13, 30, -11, 2, 6]
    selectionSort(list2)
    print("Sorted List: ", list2)
    print(selectionSort.__doc__)
    print()
    print("List is [0, 56, 21, -1, -8, 16, -12, 31, 11, 15, 13, 0, -2], sorting using Insertion Sort.")
    list3 = [0, 56, 21, -1, -8, 16, -12, 31, 11, 15, 13, 0, -2]
    insertionSort(list3)
    print("Sorted List: ", list3)
    print(insertionSort.__doc__)
    print()
    print("List is [3, 19, 22, -9, -92, 17, 4, 8, -3, 23, 52], sorting using Merge Sort.")
    list4 = [3, 19, 22, -9, -92, 17, 4, 8, -3, 23, 52]
    mergeSort(list4)
    print("Sorted List: ", list4)
    print(mergeSort.__doc__)
    print()
    print("List is [-7, 12, 3, 6, 3, 19, 43, -6, -2, 25, 10, 41, 29, -20, 8], sorting using Quick Sort.")
    list5 = [-7, 12, 3, 6, 3, 19, 43, -6, -2, 25, 10, 41, 29, -20, 8]
    quickSort(list5)
    print("Sorted List: ", list5)
    print(quickSort.__doc__)
    print()


main()

