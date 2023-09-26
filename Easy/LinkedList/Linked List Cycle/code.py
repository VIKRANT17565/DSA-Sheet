# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        h1 = head
        h2 = head

        while h2.next != None:
            print(h2.val)
            h1 = h1.next
            h2 = h2.next.next if h2.next.next != None else h2.next
            if h1.val == h2.val:
                return True

        return False
    
    def printLL(self, head):
        print()
        while head != None:
            print(head.val, "-->", end=' ')
            head = head.next

    
head = ListNode(1)
temp = head
for i in range(2, 7):
    temp.next = ListNode(i)
    temp = temp.next

temp2 = head 
for _ in range(3):
    temp2 = temp2.next

# temp.next = temp2

s = Solution()
x = s.hasCycle(head)
print(x)