# time: O(n), space: O(n)
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        length = len(nums)

        for n in range(length):
            rem = target - nums[n]
            if rem in seen:
                return [n, seen[rem]]

            seen[nums[n]] = n


        return []
