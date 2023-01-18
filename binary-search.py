# Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[] and return the index of x in the array. Consider array is 0 base index.

# Recursive

def binarySearch(array, l, r, x):

    if r >= l:
        mid = l+(r-l)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, l, mid-1, x)
        else:
            return binarySearch(array, mid+1, r, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40, 50, 60]
x = 0
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element at index %d" % result)
else:
    print("Element not found")
