# Brute Force (me), O(n^2)
# class Solution:
#     def productExceptSelf(self, nums):
#         res = [0] * len(nums)
#         for i in range(len(nums)):
#             prod = 1
#             except_self = nums[:i]+nums[i+1:]
#             for n in except_self:
#                 prod *= n
#             res[i] = prod


#         return res

class Solution:
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        prod = 1
        contains_zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if contains_zero:
                    return res
                zero_index = i
                contains_zero = True
                continue
            prod *= nums[i]

        if contains_zero:
            res[zero_index] = prod

        else:
            for i in range(len(nums)):
                res[i] = int(prod/nums[i])
        
        return res
            
            
