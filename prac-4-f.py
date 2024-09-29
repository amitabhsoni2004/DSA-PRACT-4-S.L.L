# Deletion at end of S.L.L

class node: 
    def __init__(self,data):
        self.info = data
        self.next = None
        
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)
node6 = node(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

deleted = False



if node1 is None:
    print("Deletion not possible, Linklist empty")
else: 
    
    if node1.next is None:
        data = node1.info
        node1 = node1.next
        deleted = True
    else:
        ptr1 = node1
        ptr2 = node1.next
        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        data = ptr2.info
        ptr1.next = ptr2.next
        deleted = True
    
if deleted:
    ptr = node1
    while ptr is not None :
        print(ptr.info)
        ptr = ptr.next
    print(f"Data {data} is deleted")
else:
    print("Deletion not performed")

