class Solution:
    def threeSum(self, nums: list):
        triplets = set()
        for i in range(len(nums)):
            triplet_candidates = set()
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in triplet_candidates:
                    triplets.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
                triplet_candidates.add(nums[j]) 
        return list(triplets)


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
