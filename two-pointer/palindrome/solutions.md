# Problem

[125. Valid Palindrom](https://leetcode.com/problems/valid-palindrome/description/)

> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

> Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

```python
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

Example 2:

```python
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

Example 3:

```python
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```


Constraints:

```
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
```

## Solution 1 (Two Pointers | Beats 99.99%)

Time complexity: O(n)
Space complexity: O(1)

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
```


### Solution 2: (Simple two liner)


```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        return s == s[::-1]
```
