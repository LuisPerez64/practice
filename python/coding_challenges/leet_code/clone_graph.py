"""
Question: https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed).
For example, the first node with val = 1, the second node with val = 2, and so on.
The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""
from implementations.data_structures import GraphNode as Node


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        return self.first_implementation(node)

    def first_implementation(self, node: Node) -> Node:
        """
        Store the nodes adjacency list, and then recreate it based on that.
        Do a DFS on the nodes in the graph first to ensure that all of the children
        are visited, and that the infinite cycle doesn't come into play.
        """
        if not node:
            return node
        visited = {}

        def dfs(cur_node):
            """
            Depth first search for the nodes. Each recursive instance of this function will return new copies
            of the child node, and its neighbors as well.
            """
            if cur_node in visited:
                return visited[cur_node]

            visited[cur_node] = Node(val=cur_node.val, neighbors=[])
            neighbors = []
            for neighbor in (cur_node.neighbors or []):
                neighbors.append(dfs(neighbor))
            visited[cur_node].neighbors = neighbors
            return visited[cur_node]

        return dfs(node)
