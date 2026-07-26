class Solution:
    def hasDuplicate(self, nums):
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        
        return False