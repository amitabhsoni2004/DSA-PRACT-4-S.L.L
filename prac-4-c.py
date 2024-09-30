# Insert an element at the end of S.L.L

# Define a class to represent a node in a singly linked list
class Node: 
    def __init__(self, data):
        self.info = data  # Node data
        self.next = None  # Pointer to the next node

# Function to insert a new node at the end of the singly linked list
def insert_operation(node1):
    node6 = Node(60)  # Create a new node with data 60
    
    # If the list is empty, make the new node the head
    if node1 is None:
        return node6  # The new node becomes the head

    # Traverse to the end of the list
    ptr = node1
    while ptr.next is not None:
        ptr = ptr.next
    
    # Set the 'next' of the last node to the new node
    ptr.next = node6
    return node1  # Return the head of the list

# Function to traverse and print the singly linked list
def traversal(node1):
    if node1 is None:
        print("Data not inserted...")
    else:
        ptr = node1
        while ptr is not None:
            print(ptr.info)  # Print node data
            ptr = ptr.next  # Move to the next node

# Creating nodes for the initial linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Linking the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Insert a new node at the end of the linked list
node1 = insert_operation(node1)

# Traverse and print the updated linked list
traversal(node1)
