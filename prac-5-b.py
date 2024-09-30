# Insertion at end of C.L.L

class node: 
    def __init__(self, data):  # Node initialization
        self.info = data  # Store data
        self.next = None  # Next pointer

def insert_operation(node1):
    node6 = node(60)  # New node with value 60

    if node1 is None:  # If list is empty
        node6.next = node6  # Point to itself
        node1 = node6  # Update head
        return node1  # Return new head
    else:
        ptr = node1  # Start at head
        while ptr.next != node1:  # Traverse to last node
            ptr = ptr.next  # Move to next
        node6.next = ptr.next  # Link new node
        ptr.next = node6  # Update last node
        return node1  # Return head

def traversal(node1):
    if node1 is None:  # Check if empty
        print("Linklist empty, Insertion not performed")  # Notify
    else:
        ptr = node1  # Start from head
        while True:  # Loop until back to head
            print(ptr.info)  # Print current node
            ptr = ptr.next  # Move to next
            if ptr == node1:  # Check for circle
                break  # Exit loop
    print("Data inserted at the end of the Circular Linked List.")  # Confirm

# Create circular linked list
node1 = node(10)  # First node
node2 = node(20)  # Second node
node3 = node(30)  # Third node
node4 = node(40)  # Fourth node
node5 = node(50)  # Fifth node

# Link nodes
node1.next = node2  # Link first to second
node2.next = node3  # Link second to third
node3.next = node4  # Link third to fourth
node4.next = node5  # Link fourth to fifth
node5.next = node1  # Close the circle

node1 = insert_operation(node1)  # Insert new node

traversal(node1)  # Display list