class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        n = len(s)
        i = 0
        j = n-1

        while i < j:
            if s[i] != s[j]:
                return False

            i = i + 1
            j = j - 1

        return True