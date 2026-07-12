Problem

Given an undirected graph with n vertices and a list of edges, return the number of complete connected components.

A connected component is complete if every pair of distinct vertices in that component has an edge between them.

Solution Approach

This solution is based on the observation that all vertices belonging to the same complete component have the same adjacency set (including themselves).

Steps
Initialize an adjacency list for every vertex.
Add the vertex itself to its adjacency list.
Build the graph using the given edges.
Sort each adjacency list and convert it into a tuple so it can be used as a dictionary key.
Count the frequency of every unique adjacency pattern.
A component is complete if:
The size of the adjacency tuple equals the number of vertices sharing that same adjacency pattern.

The final answer is the number of such valid patterns.

Complexity Analysis
Time Complexity: O(n + m + n log n)
m = number of edges.
Sorting the adjacency lists dominates the complexity.
Space Complexity: O(n + m)
For storing the graph and frequency map.
Why This Works

In a complete connected component containing k vertices, every vertex is connected to all other k - 1 vertices. After adding the vertex itself, every vertex has the exact same adjacency set of size k.

Therefore:

All vertices in the component produce the same sorted adjacency tuple.
That tuple appears exactly k times.
If the tuple length is also k, the component is complete.

        
Notes
This approach avoids performing a DFS/BFS to verify every component explicitly.
Instead, it leverages identical adjacency signatures to identify complete connected components efficiently.

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [1331-rank-transform-of-an-array](https://github.com/nehamukhare16/Leetcode_Solutions/tree/master/1331-rank-transform-of-an-array) |
## Hash Table
|  |
| ------- |
| [1331-rank-transform-of-an-array](https://github.com/nehamukhare16/Leetcode_Solutions/tree/master/1331-rank-transform-of-an-array) |
## Sorting
|  |
| ------- |
| [1331-rank-transform-of-an-array](https://github.com/nehamukhare16/Leetcode_Solutions/tree/master/1331-rank-transform-of-an-array) |
<!---LeetCode Topics End-->