class Solution:
    def threeSum(self, nums: list):
        nums.sort()
        triplets = []
        for k in range(len(nums)):
            if nums[k] > 0:
                break

            elif k >= 1 and nums[k] == nums[k-1]:
                continue

            else:
                i = k+1
                j = len(nums) - 1
                while j > i:
                    if (nums[i] + nums[j]) == -nums[k]:
                        triplets.append([nums[k], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        i += 1
                        j -= 1
                    
                    elif (nums[i] + nums[j]) < -nums[k]:
                        i += 1
                    
                    elif (nums[i] + nums[j]) > -nums[k]:
                        j -= 1
        return triplets

