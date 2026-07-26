class Solution:
    def topKFrequent(self, nums: list, k: int):
        max_nums, min_nums = max(nums), min(nums)
        freq_counts = [0 for i in range(max_nums-min_nums+1)]

        for n in nums:
            freq_counts[n-min_nums] += 1
        
        freq_baskets = [[] for _ in range(len(nums)+1)]
        
        for num, f in enumerate(freq_counts):
            freq_baskets[f].append(num + min_nums)

        output = []
        for b in freq_baskets:
            output += b

        return output[-k:]