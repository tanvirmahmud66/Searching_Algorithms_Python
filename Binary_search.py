def BinarySearch(arr, target):
    s=0
    l=len(arr)-1
    while s < l:
        mid = (s+l)//2
        if arr[mid] == target:
            return True 
        else:
            if arr[mid] < target:
                s = mid
            else:
                l = mid




arr = [1,2,4,5,7,12,33,55,66]
find = 55
if BinarySearch(arr, find):
    print("Found")
else:
    print("Not Found")