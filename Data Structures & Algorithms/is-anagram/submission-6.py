class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        # if t in s+s :
        #     return True
        # else :
        #     return False
        return sorted(s)==sorted(t)