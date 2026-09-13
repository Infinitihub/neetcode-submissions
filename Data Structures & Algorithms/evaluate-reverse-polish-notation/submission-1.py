class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sol = 0
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif c == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(c))
        return stack[0]