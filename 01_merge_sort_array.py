def merge_sorted_array(arr1, arr2):
    for i in range(len(arr2)):
        arr1.pop()
    for i in arr2:
        arr1.append(i)
    arr1.sort()
    return arr1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge_sorted_array(nums1,nums2))