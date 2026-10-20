class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.mini:
            self.mini.append(val) 
        else:
            self.mini.append(min(val,self.mini[-1]))

    def pop(self) -> None:
        self.arr.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
