# Deletion at start of S.L.L

class node: 
    def __init__(self,data):
        self.info = data
        self.next = None


node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

deleted = False

if node1 is None:
    print("Deletion not possible, Linked list is empty")
else:
    data = node1.info
    node1 = node1.next # it will handle in case of only one node in link list have
    deleted = True

if deleted:
    ptr = node1
    while ptr is not None:
        print(ptr.info)
        ptr = ptr.next
    print(f"The element {data} is deleted")
else:
    print("Deletion operation not performed")