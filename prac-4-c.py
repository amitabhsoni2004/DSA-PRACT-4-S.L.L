# Insert an element at the end of S.L.L

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

inserted = False

node6 = node(60)
node5.next = node6
inserted = True

if inserted:
    ptr = node1
    while ptr is not None : 
        print(ptr.info)
        ptr = ptr.next
else : 
    print("Data not inserted...")