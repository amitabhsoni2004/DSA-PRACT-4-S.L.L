# Insertion after a particular element in S.L.L

class node : 
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

data = 0
inserted = False
node6 = node(35)

ptr = node1
while ptr is not None and ptr.info is not data : 
    ptr = ptr.next

if ptr is not None:
    node6.next = ptr.next
    ptr.next = node6
    inserted = True
else:
    print(f"Data {data} is not found in S.L.L")
    
if inserted:
    ptr1 = node1
    while ptr1 is not None : 
        print(ptr1.info)
        ptr1 = ptr1.next
else:
    print('Insertion was not performed.')
