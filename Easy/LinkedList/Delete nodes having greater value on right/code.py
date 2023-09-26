#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        # t = Node(-1)
        # t.next = head
        
        last = Node(10**7)
        last.next = head
        mainHead = last
        t = head

        while t.next != None:
            # print(t.data)
            if t.data < t.next.data:
                last.next = t.next
                t = last.next
                # return mainHead
            else:
                t = t.next
                last = last.next

        
        return mainHead.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Node Class
class Node:
    def __init__(self, data):   # data -> dataue stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given dataue and appends it at the end of the linked list
    def append(self, new_dataue):
        new_node = Node(new_dataue)
        if self.head is None:
            self.head = new_node
            self.tail =new_node
            return
        self.tail.next=new_node
        self.tail=new_node

    def getNode(self,dataue): # return node with given dataue, if not present return None
        curr_node=self.head
        while(curr_node.next and curr_node.data != dataue):
            curr_node=curr_node.next
        if(curr_node.data==dataue):
            return curr_node
        else:
            return None

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')





if __name__=="__main__":
    t=int(input())
    while(t>0):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        
        result=Solution().compute(a.head)
        a.head=result
        a.printList()
        t-=1
    
        
    
    
# } Driver Code Ends