class MinStack:

    def __init__(self):
        self.stack = []
        self.mintracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mintracker or val < self.mintracker[-1]:
            self.mintracker.append(val)
        else:
            self.mintracker.append(self.mintracker[-1])

    def pop(self) -> None:
        self.mintracker.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mintracker[-1]
