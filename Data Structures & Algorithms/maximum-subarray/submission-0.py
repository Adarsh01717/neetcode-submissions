class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = nums[0]
        ans = nums[0]
        i = 1
        while i <= len(nums)-1:
            v1 = max_ending + nums[i]
            v2 = nums[i]
            max_ending = max(v1, v2)
            ans = max(ans, max_ending)
            i += 1
        return ans