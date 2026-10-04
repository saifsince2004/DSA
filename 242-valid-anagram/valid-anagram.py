class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        sort_t= sorted(t)
        sort_s = sorted(s)
        if sort_t == sort_s:
            return True
        else:
            return False

        