class Solution2:
    def isValidBracket(self, open: str, close: str ) -> bool:
        validBrackets = {
            "{": "}",
            "[": "]",
            "(": ")",
        }


        return open in validBrackets and validBrackets[open] == close

    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if len(stack) == 0:
                if c in "({[":
                    stack.append(c)
                else:
                    return False
            else:
                if self.isValidBracket(stack[-1], c):
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack) == 0
