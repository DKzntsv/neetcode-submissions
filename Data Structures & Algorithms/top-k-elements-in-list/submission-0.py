class Solution:
    def topKFrequent(self, nums: list, k: int):
        max_nums, min_nums = max(nums), min(nums)
        freq_counts = [0] * (max_nums-min_nums+1)
        for n in nums:
            freq_counts[n-min_nums] += 1
        
        freq_buckets = [[] for _ in range(len(nums)+1)]
        
        for i in range(len(freq_counts)):
            freq_buckets[freq_counts[i]].append(i+min_nums)
        
        output=[]
        for freq in range(len(freq_buckets)-1, -1, -1):
            output+=freq_buckets[freq]
            
        return output[:k]