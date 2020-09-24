## Copy List with Random Pointer [Medium]
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

`val`: an integer representing Node.val
`random_index`: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

## Solution (Extra space)
 - Create a hash map with all nodes and their index
 - Use an array to create copies and assign random or next nodes if `arr[map.get(random or next)]` is not null and create otherwise.
  
## Solution (No extra space)
As an optimised solution, we could reduce the space complexity into constant. The idea is to associate the original node with its copy node in a single linked list. In this way, we don't need extra space to keep track of the new nodes.

The algorithm is composed of the follow three steps which are also 3 iteration rounds.

1. Iterate the original list and duplicate each node. The duplicate
of each node follows its original immediately.
2. Iterate the new list and assign the random pointer for each
duplicated node.
3. sRestore the original list and extract the duplicated nodes.