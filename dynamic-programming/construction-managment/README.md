## Construction Management
A construction is building a new neighborhood. Houses are built using 
three materials (wood, brick or concrete) but no side-by-side house can have the same
material. 

Given materials and their costs return the minimum costs.


## Solution



```
# [[3,2,1], [2,2,1], [3,5,1],[2,4,2]]
# if pick index i for n 
# three choices first
# x = [1, 2, 3].filter(j) 
# min at index i dp[i][j]= n[i] + dp[i-1][min(dp[i-1][j])] 
```