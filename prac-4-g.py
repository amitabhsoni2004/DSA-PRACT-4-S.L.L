# Deletion of particular element in S.L.L

class node:
    def __init__(self, data):
        self.info = data  # Node stores data in 'info'
        self.next = None  # Pointer to the next node initialized to None


def delete_operation(node1, data_to_delete):
    if node1 is None:  # Case when the list is empty
        print("Deletion not possible, Linklist empty...")
        return  # Exit as there's nothing to delete
    else:
        if node1.info == data_to_delete:  # If the first node is the one to delete
            data = node1.info  # Store the data of the node to be deleted
            node1 = node1.next  # Move the head to the next node
            return node1, data  # Return the new head and the deleted data
        else:
            ptr1 = node1  # Pointer to the current node
            ptr2 = node1.next  # Pointer to the next node
            # Traverse the list until the node to delete is found
            while ptr2 is not None and ptr2.info != data_to_delete:
                ptr1 = ptr1.next  # Move ptr1 forward
                ptr2 = ptr2.next  # Move ptr2 forward
            
            if ptr2 is None:  # If the element is not found
                print(f"Data {data_to_delete} not found in the Linklist, deletion not possible.")
                return node1, None  # Return the original list with no deletion
            else:
                data = ptr2.info  # Store the data of the node to be deleted
                ptr1.next = ptr2.next  # Bypass the node to delete
                return node1, data  # Return the modified list and the deleted data


def traversal(node1, data):
    if node1 is None:  # Case when the list is empty
        print("Linklist empty after deletion")
    else:
        ptr = node1  # Start traversal from the head node
        while ptr is not None:
            print(ptr.info)  # Print the current node's data
            ptr = ptr.next  # Move to the next node
    if data:  # If data was deleted, print the deleted message
        print(f"Data {data} has been deleted.")


# Constructing the linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Element to delete
data_to_delete = 500

# Perform deletion
node1, data = delete_operation(node1, data_to_delete)

# Traverse and print the linked list after deletion
traversal(node1, data)
