def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    return sorted(nums1)


nums1 = [10,20,20,40,0,0]
m = 4
nums2 = [1,2]
n = len(nums2)

print(merge(nums1, m, nums2, n))