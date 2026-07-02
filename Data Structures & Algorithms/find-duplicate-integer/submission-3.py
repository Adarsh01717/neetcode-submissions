class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == nums [i + 1]:
                return nums[i]
            i = i + 1
        return -1


