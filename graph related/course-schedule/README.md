## Course Schedule [Medium]
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

## Solution
1. Using DFS keep two sets, one to track visiting nodes and the other for visited.
   -  If node has been encountered and is in the visiting set, then we have detected a cycle
2. Perform a topolocial sort and see if the graph satifies the following conditions of a DAG
    - Has at least one node with indegree 0
    - Has at least one node with outdefree 0

  