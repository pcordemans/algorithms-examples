def binarySearch(arr, n):  
    
    def innerSearch(arr, n, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid
        elif n > arr[mid]:
            return innerSearch(arr, n, mid+1, high)
        else:
            return innerSearch(arr, n, low, mid-1)

    return innerSearch(arr, n, 0, len(arr)-1)         
        

arr = [1,2,3,4,5,6,7,8,9]

print (binarySearch(arr, 10))
