# Perform a traversal in S.L.L

# Define a class to represent a node in a singly linked list
class Node:
    def __init__(self, data):
        self.info = data  # Node data
        self.next = None  # Pointer to the next node

# Function to traverse the singly linked list
def traversl_SLL(begin):
    ptr = begin
    while ptr is not None:
        print(ptr.info)  # Print the current node's data
        ptr = ptr.next  # Move to the next node

# Creating nodes for the linked list
begin = Node(10)  # Head node
node1 = Node(20)  # Second node
node2 = Node(30)  # Third node
node3 = Node(40)  # Fourth node

# Linking the nodes together
begin.next = node1
node1.next = node2
node2.next = node3

# Call the traversal function to print the elements in the linked list
traversl_SLL(begin)

    