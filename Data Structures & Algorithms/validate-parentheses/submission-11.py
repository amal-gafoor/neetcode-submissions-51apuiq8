class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(",
                    "]":"[",
                    "}":"{"}

        stack = []
        for val in s:
            if val in brackets:
                if stack and brackets[val] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)

        return len(stack) == 0