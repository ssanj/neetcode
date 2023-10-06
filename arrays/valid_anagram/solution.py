class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i, c in enumerate(sorted_s):
            if sorted_t[i] != c:
                return False
        
        return True

