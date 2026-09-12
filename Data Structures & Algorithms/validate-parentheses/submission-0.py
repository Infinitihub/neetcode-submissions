class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # if len(s) % 2 == 1:
        #     return False
        # for char in s:
        #     if char == '}':
        #         if stack.pop != '{':
        #             return False
        #     elif char == ']':
        #         if stack.pop != '[':
        #             return False
        #     elif char == ')':
        #         if stack.pop != '(':
        #             return False
        #     if char in ["(", "{", "["]:
        #         stack.append(char)
        # return True

        if len(s) % 2 == 1:
            return False

        stack = []
        matching = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in matching:
                # Pop the most recent opening bracket; fallback to dummy if empty
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)

        # Must be empty; leftover openings mean invalid syntax
        return len(stack) == 0