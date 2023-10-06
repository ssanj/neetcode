# time: O(n2), space: O(1)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for left in range(length - 1): # skip the last element on left pointer
            for right in range(left + 1, length): # skip the left element on the right pointer
                if nums[left] + nums[right] == target:
                    return [left, right]

        return []
