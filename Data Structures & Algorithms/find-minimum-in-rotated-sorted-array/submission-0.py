class Solution:
    def findMin(self, nums: list):
        i = 0
        j = len(nums)-1
        while nums[i] > nums[j]:
            mid = (i+j)//2 
            if nums[mid] > nums[j]:
                i = mid + 1
            else: 
                j = mid


        return min(nums[i], nums[j])