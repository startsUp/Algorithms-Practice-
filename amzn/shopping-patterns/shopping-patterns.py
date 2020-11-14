"""
Amazon is trying to understand customer shopping patterns and offer items that are regularly bought together to new customers. Each item that has been bought together can be represented as an undirected graph where edges join often bundled products. A group of n products is uniquely numbered from 1 of product_nodes. A trio is defined as a group of three related products that all connected by an edge. Trios are scored by counting the number of related products outside of the trio, this is referred as a product sum.

Given product relation data, determine the minimum product sum for all trios of related products in the group. If no such trio exists, return -1.

Example
products_nodes = 6
products_edges = 6
products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]

Product	Related Products
1	| 2
2	| 1, 4, 5
3	| 5
4	| 2, 5
5	| 2, 3, 4, 6
6	| 5
A graph of n = 6 products where the only trio of related products is (2, 4, 5).

The product scores based on the graph above are:

Product	Outside Products	Which Products Are Outside
2	1	1
4	0	 
5	2	3, 6
In the diagram above, the total product score is 1 + 0 + 2 = 3 for the trio (2, 4, 5).
"""

# we can find trios by going through the adjacency list and selecting pairs of two number that 

def getTrios(products_from, products_to):
    adj = [[] for _ in range(len(products_from) + 1)]
    print(adj)
    for p in range(len(products_from)):
        adj[products_from[p]].append(products_to[p])
        adj[products_to[p]].append(products_from[p])
    
    trios = {}
    for k in range(1, len(adj)): # brute force find trios
        l = adj[k]
        for i in range(0, len(l)-1):
            for j in range(i+1, len(l)):
                p1, p2 = l[i], l[j] 
                triplet = tuple(sorted([k, p1, p2]))
                if triplet in trios:
                    continue
                else:
                    if (p1 in adj[p2]):
                        trios[triplet] = True
    print(trios)

    
    for trio in trios:
        for 
    print(adj)

products_from = [1,2,2,3,4,5]
products_to = [2,4,5,5,5,6]
print(getTrios(products_from, products_to))
