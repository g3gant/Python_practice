
# Definition for a Node.
class Node:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        print (node.val)
        clone = Node(node.val)
        self.visited[node]= clone
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone


adjList = [[2,4],[1,3],[2,4],[1,3]]
nd1 = Node(1,[2,4])
nd2 = Node(2,[1,3])
nd3 = Node(3,[2,4])
nd4 = Node(4,[1,3])
#print(nd1.val)
print(Solution().cloneGraph(nd1))