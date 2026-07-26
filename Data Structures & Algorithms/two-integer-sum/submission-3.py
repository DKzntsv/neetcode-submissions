class Solution:
    def twoSum(self, nums, target: int):
        visited = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in visited:
                return [visited[diff], i]
            visited[n] = i
