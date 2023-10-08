def rotate_array_right(arr, n):
    # Solution 1
    
    # temp = arr[-1]
    # i = len(arr)-1
    # j = 0
    # while j < n:
    #     while i >= 0:
    #         if i == 0:
    #             arr[i] = temp
    #             i = len(arr)-1
    #             break
    #         arr[i] = arr[i-1]
    #         i-=1
    #     j += 1
    #     temp = arr[-1]
    
    # Solution 2 
    
    n = n % len(arr)
    l,r = 0, len(arr)-1
    while l<r:
        arr[l],arr[r] = arr[r], arr[l]
        l, r = l+1, r-1
    l, r = 0, n-1
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1,r-1
    l,r = n,len(arr)-1
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l,r = l+1,r-1
    return arr

arr = [1,2,3,4,5,6,7]
arr1 = [-1,-100,3,99]
print(rotate_array_right(arr1,2))