from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_s = Counter(s)
        counts_t = Counter(t)

        if counts_s == counts_t:
            return True
        return False

