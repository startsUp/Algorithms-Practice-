## Two City Scheduling [Easy]
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 
Example 1:
```

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
```


## Solution
We need to ensure we get the best savings for each person. Meaning, sort by abs savings and send to the place where we save the most.
```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[1]-x[0]), reverse=True)
        a = len(costs) / 2
        b = a
        ans = 0
        for c in costs:
            if c[0] > c[1] and b > 0:
                ans+=c[1]
                b-=1
            elif c[1] > c[0] and a > 0:
                ans+=c[0]
                a-=1
            else:
                ans+= c[0] if a > 0 else c[1]
                a-= 1 if a > 0 else 0
                b-= 1 if b > 0 else 0
        return ans
```
We can optimize by sorting according to savings for one place.
```
costs.sort(key=lambda x: x[0] - x[1])
```
And just send the first half to `A` since we save to most if we do.