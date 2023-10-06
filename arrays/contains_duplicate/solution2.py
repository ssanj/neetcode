class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        already_seen = set()
        for n in nums:
            if n in already_seen:
                return True

            already_seen.add(n)

        return False

