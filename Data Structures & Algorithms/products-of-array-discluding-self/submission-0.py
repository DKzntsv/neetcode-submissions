class Solution:
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        for i in range(len(nums)):
            prod = 1
            except_self = nums[:i]+nums[i+1:]
            for n in except_self:
                prod *= n
            res[i] = prod


        return res