class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Solution():
    def addNumbers(self,l1,l2):
        result = Node(0)
        carry = 0
        sum = 0
        ref = current = None
        while (l1 or l2):
            sum = l1.value + l2.value + carry
            carry = sum // 10
            
            if not current:
                ret = current = Node(sum % 10)
            else:
                current.next = Node(sum % 10)
                current = current.next

            if l1.next or l2.next:
                if not l1.next:
                    l1.next = Node(0)
                if not l2.next:
                    l2.next= Node(0)
            elif carry:
                current.next = Node(carry)
            l1 = l1.next
            l2 = l2.next

        return ret


num1 = Node(2,(Node(4,Node(3))))
num2 = Node(5,(Node(6,Node(4))))

answer = Solution().addNumbers(num1, num2)
while answer:
  print(answer.value, end=' ')
  answer = answer.next