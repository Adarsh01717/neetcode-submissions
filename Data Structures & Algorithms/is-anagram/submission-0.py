class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        f, g = {},{}

        i = 0
        while i < len(s):
            f[s[i]] = f.get(s[i], 0) + 1
            g[t[i]] = g.get(t[i], 0) + 1

            i+=1

        return f == g
        
        # if len(s) != len(t):
        #     return False

        # f, g = {}, {}

        # for i in range(len(s)):
        #     f[s[i]] = f.get(s[i], 0) + 1
        #     g[t[i]] = g.get(t[i], 0) + 1

        # return f == g