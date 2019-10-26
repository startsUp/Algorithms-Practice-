## Question [Medium]
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

### Example 1:
```
Input: 2
Output: [0,1,1]
```

## Solution

```
# all powers of two will have bit count = 1
# any other number x for 2^a < x < 2^b
# x = 2^a + z (z < 2^a)
# bit count of x = bit count of 2^a + bit count of (x - 2^a)
class Solution:
    def countBits(self, num: int) -> List[int]:
        bitCount = [0 for i in range(num+1)]
        x = 1
        while(x<=num): 
            bitCount[x] = 1 #all powers of 2 will only have 1 bit set
            x = x*2
            
        x = 3
        power = 1
        while(x<=num):
            if(bitCount[x] != 1):
                bitCount[x] = bitCount[2**power] + bitCount[x - (2**power)]
            else:
                power += 1
            x+=1
        
        return bitCount
```