# Perform a traversal in S.L.L

class node:
    def __init__(self,data):
        self.info = data
        self.next = None
        
begin = node(10)
node1 = node(20)
node2 = node(30)
node3 = node(40)

begin.next = node1
node1.next = node2
node2.next = node3


ptr = begin
while ptr is not None :
    print(ptr.info)
    ptr = ptr.next
    