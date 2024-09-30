# Deletion at start of C.L.L

class node: 
    def __init__(self, data):  # Initialize a new node
        self.info = data  # Store the data in the node
        self.next = None  # Initialize the next pointer to None

def delete_operation(node1):
    if node1 is None:  # Check if the list is empty
        print("Deletion not possible, L.L empty")  # Inform user
        return  # Exit the function
    else:
        data1 = node1.info  # Store the data of the node to be deleted
        if node1.next == node1:  # Check if there is only one node in the list
            node1 = None  # Set the head to None, list is now empty
            return node1, data1  # Return None and the deleted data
        else:
            ptr = node1  # Start at the head of the list
            while ptr.next != node1:  # Traverse to the last node
                ptr = ptr.next  # Move to the next node
            
            ptr.next = node1.next  # Link the last node to the new head
            node1 = node1.next  # Move the head pointer to the next node
            return node1, data1  # Return the new head and the deleted data

def traversal(node1, data1):
    if node1 is None:  # Check if the list is empty after deletion
        print("Linklist empty after deletion")  # Inform user
    else:
        ptr = node1  # Start at the new head
        while True:  # Loop until we come back to the head
            print(ptr.info)  # Print the data of the current node
            ptr = ptr.next  # Move to the next node
            if ptr == node1:  # If we have completed the circle
                break  # Exit the loop
    print(f"Element {data1} has been deleted")  # Confirm the deletion of the element

# Create circular linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4 
node4.next = node5
node5.next = node1

node1, data1 = delete_operation(node1)  # Perform deletion

traversal(node1, data1)  # Display updated list
