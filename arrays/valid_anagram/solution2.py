class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        smap = {}
        tmap = {}

        for c in s:
            smap[c] = smap.get(c, 0) + 1

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1


        for (k, v) in smap.items():
            if k in tmap and tmap[k] == v:
                continue
            else:
                return False
        
        return True
