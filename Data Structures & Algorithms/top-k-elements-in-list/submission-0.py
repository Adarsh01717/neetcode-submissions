class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for c in range (len(nums)):
            count[nums[c]] = count.get(nums[c], 0) + 1
            sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
            res = sorted_keys[:k]
        return res
        