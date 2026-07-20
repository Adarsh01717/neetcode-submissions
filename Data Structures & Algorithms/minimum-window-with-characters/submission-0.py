class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        need = len(t_count)
        
        have = 0
        window_count = {}
        low = 0
        best_len = float('inf')
        start = 0
        
        for high in range(len(s)):
            window_count[s[high]] = window_count.get(s[high], 0) + 1
            if s[high] in t_count and window_count[s[high]] == t_count[s[high]]:
                have += 1
            
            while have == need:
                if (high - low + 1) < best_len:
                    best_len = high - low + 1
                    start = low
                
                if s[low] in t_count and window_count[s[low]] == t_count[s[low]]:
                    have -= 1
                window_count[s[low]] -= 1
                low += 1
        
        if best_len == float('inf'):
            return ""
        return s[start:start + best_len]