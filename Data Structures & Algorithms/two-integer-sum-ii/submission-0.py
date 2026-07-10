class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        l = 0
        r = n-1

        while l < r:
            num_sum = numbers[l] + numbers[r]
            if num_sum == target:
                return [l + 1, r + 1]
            elif num_sum > target:
                r-=1
            else:
                l+=1


