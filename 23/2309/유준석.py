# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
        
#         count1 = 0
#         count2 = 0
#         nums3 = []
#         for i in range(m+n):
#             if nums1[count1] > nums2[count2] :
#                 nums3.append(nums2[count2])
#                 count2 += 1
#             else :
#                 nums3.append(nums1[count1])
#                 count1 += 1
        
#         print(nums3)
        
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """





nums1 = [1,0,0,0,2,3]
nums2 = [2,5,6]
m = 3
n = 3


count1 = 0
count2 = 0
nums3 = []
while(1):
    if nums1[count1] > nums2[count2] :
        nums3.append(nums2[count2])
        count2 += 1
    else :
        nums3.append(nums1[count1])
        count1 += 1
    
    
    if m == count1 :
        while n != count2 :
            nums3.append(nums2[count2])
            count2 += 1
        break
    
    if n == count2 :
        while m != count1 :
            nums3.append(nums1[count1])
            count1 += 1
        break

print(nums3)