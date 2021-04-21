#Sorted array
#linear search->O(n)
#Binary search->o(logn+c)

def binarySearch(arr, l, r, x):
    if (r < l):
        return -1
    mid = int( l + (r - l) / 2)
    if arr[mid] == x:
        return mid

    if arr[mid] > x:
        return binarySearch(arr, l,
                            mid - 1, x)
 
   
    return binarySearch(arr, mid + 1,
                                r, x)
 

def countOccurrences(arr, n, x):
    l = binarySearch(arr, 0, n - 1, x)
    if l == -1:
        return 0

    c=1
    left =l- 1
    while (left >= 0 and
           arr[left] == x):
        c += 1
        left -= 1
 
    right = l + 1;
    while (right < n and
           arr[right] == x):
        c += 1
        right += 1
 
    return c

arr = [ 1, 3,4,4,7,3, 4, 7, 8, 8 ]
n = len(arr)
x = 8
print(countOccurrences(arr, n, x))
