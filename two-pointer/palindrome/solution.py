class Solution:
    def isPalindrome(self, s: str) -> bool:

        input = []

        for c in s:
            if c.isalnum():
                input.append(c.lower())

        return input == input[::-1]
