# Deletion at end of C.L.L

class node: 
    def __init__(self, data):  # Initialize a new node
        self.info = data  # Store the data in the node
        self.next = None  # Initialize the next pointer to None


def delete_operation(node1):
    if node1 is None:  # Check if the list is empty
        print("Deletion not possible, LinkList Empty...")  # Inform user
        return  # Exit the function
    else:
        if node1.next == node1:  # Check if there is only one node in the list
            data1 = node1.info  # Store the data of the node to be deleted
            node1 = None  # Set the head to None, list is now empty
            return node1, data1  # Return None and the deleted data
        else:
            ptr1 = node1  # Start at the head of the li st
            ptr2 = node1.next  # Start from the second node
            while ptr2.next != node1:  # Traverse to the last node
                ptr1 = ptr1.next  # Move ptr1 to the next node
                ptr2 = ptr2.next  # Move ptr2 to the next node
            
            data1 = ptr2.info  # Store the data of the last node to be deleted
            ptr1.next = ptr2.next  # Link the second last node to the head
            return node1, data1  # Return the head and the deleted data


def traversal(node1, data1):
    if node1 is None:  # Check if the list is empty after deletion
        print("Linklist empty after deletion")  # Inform user
    else:
        ptr = node1  # Start at the new head
        while True:  # Loop until we come back to the head
            print(ptr.info)  # Print the data of the current node
            if ptr.next == node1:  # Check if we are back at the head
                break  # Exit the loop
            ptr = ptr.next  # Move to the next node
    print(f"Element {data1} has been deleted")  # Confirm the deletion of the element


# Create circular linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Link nodes to form a circular linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

node1, data1 = delete_operation(node1)  # Perform deletion operation

traversal(node1, data1)  # Display the updated linked list after deletion
