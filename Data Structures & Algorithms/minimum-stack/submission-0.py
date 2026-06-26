class MinStack:

    def __init__(self):
        self.STACK = []
        

    def push(self, val: int) -> None:
        self.STACK.append(val)
        

    def pop(self) -> None:
        if self.STACK :
            self.STACK.pop()
        

    def top(self) -> int:
        if self.STACK :
            return self.STACK[-1]
        

    def getMin(self) -> int:
        if self.STACK :
            return min(self.STACK)
        
