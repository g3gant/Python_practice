class Node(object):
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.right = right
        self.left = left



class Solution(object):
    
    def _isValid(self,n,low,high):
        if not n: return True
        if (n.val < high and n.val > low and 
        self._isValid(n.left,low,n.val) and self._isValid(n.right,n.val,high)):
            return True
        return False

    
    def isValid(self,n):
        return self._isValid(n,float('-inf'),float('inf'))
    


node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.right = Node(9)

print (Solution().isValid(node))

