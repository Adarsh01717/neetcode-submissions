class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        i = 0
        j = i+1
        while j < n:
            if nums[i] == nums[j]:
                return True
            i = i+1
            j+=1
        return False