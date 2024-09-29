# Insertion at end of C.L.L

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
node5.next = node1

inserted = False
node6 = node(60)

if node1 is None:
    node6.next = node6
    node1 = node6
    inserted = True
else:
    if node1.next == node1:
        node6.next = node1.next
        node1.next = node6
        inserted = True
    else:
        ptr = node1
        while ptr.next != node1:
            ptr = ptr.next
        node6.next = ptr.next
        ptr.next = node6
        inserted = True
    
if inserted:
    ptr = node1
    while ptr is not None:
        print(ptr.info)
        ptr = ptr.next
        if ptr == node1:
            break
    print("Data inserted at the end of the Circular Linked List.")
else:
    print("Insertion not performed")