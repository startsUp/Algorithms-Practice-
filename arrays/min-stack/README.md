## Question 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
 

Example:
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

## Solution:
Maintain stack and a global variable min. Update min on pop and append

```
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
```