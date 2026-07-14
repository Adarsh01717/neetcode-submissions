class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = {}
        low = 0
        sub_count = 0

        for high in range (len(s)):
            if s[high] in f and f[s[high]] >= low:
                low = f[s[high]] + 1
            f[s[high]] = high
            sub_count = max(sub_count, high - low + 1)

        return sub_count