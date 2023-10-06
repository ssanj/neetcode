# time: O(n2), space: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = 1        
        length = len(nums)
        while (right < length):
            while (right < length):
                if nums[left] + nums[right] == target:
                    return [left, right]
                
                right += 1

            left += 1
            right = left + 1
        
        return []
