# Deletion at start of S.L.L

# Define a class for the node in the singly linked list
class node: 
    def __init__(self, data):
        self.info = data  # Store the node's data
        self.next = None  # Pointer to the next node


# Function to delete the first node in the list
def delete_operation(node1):
    if node1 is None:  # If the list is empty, deletion is not possible
        print("Deletion not possible, Linked list already empty")
    else:
        data1 = node1.info  # Store the info of the node being deleted
        node1 = node1.next  # Update the head to the next node
        return data1, node1  # Return the data of the deleted node and the new head

# Function to traverse and print the list
def traversal(node1, data1):
    if node1 is None:  # If the list becomes empty after deletion
        print("Linklist empty after deletion of the only node")    
    else:
        ptr = node1
        while ptr is not None:
            print(ptr.info)  # Print each node's data
            ptr = ptr.next
    print(f"The element {data1} has been deleted")  # Confirm deletion

# Create nodes and form the linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Perform deletion of the first node
data1, node1 = delete_operation(node1)

# Traverse the updated list and display the result
traversal(node1, data1)
