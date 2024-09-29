# Insert an element at start of S.L.L

class node : 
    def __init__(self,data):
        self.info = data
        self.next = None
        
begin = node(10)
node1 = node(15)
node2 = node(20)
node3 = node(25)
node4 = node(30)

begin.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

inserted = False

node0 = node(5)
node0.next = begin
begin = node0
inserted = True

if inserted: 
    ptr = begin
    while ptr is not None:
        print(ptr.info)
        ptr = ptr.next
else : 
    print("Data is not inserted in S.L.L")