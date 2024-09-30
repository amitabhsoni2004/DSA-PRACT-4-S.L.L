# Insertion at start of C.L.L

class node: 
    def __init__(self, data): 
        self.info = data  # Store data in the node
        self.next = None  # Pointer to the next node

def insert_operation(node1):
    node0 = node(5)  # Create a new node to insert

    if node1 is None:  # If the list is empty
        node0.next = node0  # Point to itself, circular behavior
        node1 = node0  # New node becomes the first node
        return node1
    else:
        ptr = node1  # Start from the head node
        # Traverse until we find the last node (where next points to head)
        while ptr.next != node1:
            ptr = ptr.next
        
        node0.next = node1  # Link new node to head
        ptr.next = node0  # Last node now points to new node
        node1 = node0  # New node becomes the head
        return node1

def traversal(node1):
    if node1 is None:  # If the list is empty
        print("Linklist empty,Insertion not performed")
    else:
        ptr = node1  # Start from the head
        # Traverse and print nodes until we reach the head again
        while ptr is not None:
            print(ptr.info)
            ptr = ptr.next
            if ptr == node1:  # Stop when we return to the head
                break

# Creating a circular linked list with nodes
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Linking nodes circularly
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1  # Last node points to the first node, forming a circle

# Insert a node at the start
node1 = insert_operation(node1)

# Traverse and print the circular linked list
traversal(node1)
