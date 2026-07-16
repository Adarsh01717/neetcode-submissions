class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_freq = 0
        low = 0
        max_len = 0
        
        for high in range(len(s)):
            char_count[s[high]] = char_count.get(s[high], 0) + 1
            max_freq = max(max_freq, char_count[s[high]])
            
            if (high - low + 1) - max_freq > k:
                char_count[s[low]] = char_count[s[low]] - 1
                low += 1
            
            max_len = max(max_len, high - low + 1)
    
        return max_len