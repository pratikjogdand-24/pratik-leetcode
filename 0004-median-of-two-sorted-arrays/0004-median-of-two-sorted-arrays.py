class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = nums1 + nums2
        nums.sort()

        length = len(nums)

        middle = length // 2

        if length % 2 == 0:
            return (nums[middle - 1] + nums[middle]) / 2.0

        return nums[middle]
       
   
      