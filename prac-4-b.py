# Insert an element at start of S.L.L

class Node: 
    def __init__(self, data):
        self.info = data
        self.next = None

def insert_operation(begin):
    node0 = Node(5)  # Create a new node with the value 5
    node0.next = begin  # Link new node to the current head
    begin = node0  # Set the new node as the head
    return begin  # Return the new head

def traversal(begin):
    if begin is None:
        print("Data is not inserted in S.L.L")
    else:
        ptr = begin
        while ptr is not None:
            print(ptr.info)  # Print the data of the node
            ptr = ptr.next  # Move to the next node

# Creating the initial linked list
begin = Node(10)
node1 = Node(15)
node2 = Node(20)
node3 = Node(25)
node4 = Node(30)

begin.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Insert a new node at the beginning
begin = insert_operation(begin)

# Traverse and print the linked list
traversal(begin)
