# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLL(head):
    while head != None:
        print(head.val, "-->", end=' ')
        head = head.next
    print()


class Solution:
    def mergeTwoLists(self, list1, list2):
        merged = ListNode(-101)
        temp = merged
        while list1 != None and list2 != None:
            # print(list1.val, list2.val)
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next

        temp.next = list1 if list1 != None else list2

        return merged


head1 = ListNode(1)
temp = head1
for i in range(2, 11, 2):
    temp.next = ListNode(i)
    temp = temp.next

head2 = ListNode(1)
temp = head2
for i in range(1, 11, 2):
    temp.next = ListNode(i)
    temp = temp.next

s = Solution()
printLL(head1)
printLL(head2)
printLL(s.mergeTwoLists(head1, head2))