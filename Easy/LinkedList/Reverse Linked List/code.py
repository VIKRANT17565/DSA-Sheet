# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        
        # #using for loop
        # prevNode = None
        # while head.next != None:
        #     nextNode = head.next
        #     head.next = prevNode
        #     prevNode = head
        #     head = nextNode
        #     nextNode = nextNode.next
        # head.next = prevNode

        #using recursion 
        if head == None or head.next == None:
            return head
        
        newHead = self.reverseList(head.next)
        # head.next.next = head
        temp = head.next
        head.next = None
        temp.next = head
        return newHead
    


    def printLL(self, head):
        print()
        while head != None:
            print(head.val, "-->", end=' ')
            head = head.next


head = ListNode(1)
temp = head
for i in range(2, 6):
    temp.next = ListNode(i)
    temp = temp.next

s = Solution()
s.printLL(head)
h = s.reverseList(head)
s.printLL(h)