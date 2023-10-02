class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        else:
            sorted = nums.sort()
            index = 0
            first = nums[index]
            length = len(nums)-1

            while index < length:
                first = nums[index]
                index = index + 1
                next = nums[index]
                
                print(f"index:{index}, first:{first}, next:{next}")
                if first == next:
                    print("returning True")
                    return True
                else:
                    continue

            return False

# This solution is n (logn), which is worse than n.
# https://stackoverflow.com/questions/56506410/why-is-on-better-than-o-nlogn
