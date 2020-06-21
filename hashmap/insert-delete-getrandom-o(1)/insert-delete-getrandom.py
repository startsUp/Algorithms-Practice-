import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = {}
        self.keys = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False
            
        self.size+=1
        self.set[val] = self.size
        self.keys[self.size] = val
        return True
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # since keys are index-based, when removing a element, we make the last element's index the index we removed

        if val in self.set:
            index = self.set[val]
            self.set[self.keys[self.size]] = index #chnage the last element's index
            self.keys[index] = self.keys[self.size]
            
            del self.set[val]
            del self.keys[self.size]
            self.size-=1

            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random.randint(1,self.size)
        return self.keys[r]
    
    def toString(self):
        print(self.set, self.keys, self.size)
        
obj = RandomizedSet()
param_1 = obj.insert(4)
param_2 = obj.insert(3)
obj.remove(3)
param_3 = obj.getRandom()
print(param_3)
obj.toString()