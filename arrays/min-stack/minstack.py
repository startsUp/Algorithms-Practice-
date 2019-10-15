class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = None        

    def push(self, x: int) -> None:
        self.s.append(x)
        if(self.min == None or self.min > x):
            self.min = x

    def pop(self) -> None:
        if(len(self.s) == 0):
            return
        pE = self.s.pop()
        if pE == self.min:
            if(len(self.s) != 0):
                self.min = min(self.s)
            else:
                self.min = None 
            
    def top(self) -> int:
        if(len(self.s) != 0):
            return self.s[-1]
        return None

    def getMin(self) -> int:
        return self.min
