# Deletion at end of S.L.L

class node: 
    def __init__(self, data):
        self.info = data  # Store the data value in the node
        self.next = None  # Pointer to the next node, initially None

def delete_operation(node1):
    if node1 is None:  # Check if the linked list is empty
        print("Deletion not possible, Linklist empty")
    else: 
        if node1.next is None:  # If the list has only one node
            data1 = node1.info  # Store data of the only node
            node1 = node1.next  # Set head to None (list becomes empty)
            return node1, data1
        else:
            ptr1 = node1  # Pointer to keep track of the second last node
            ptr2 = node1.next  # Pointer to traverse the list
            while ptr2.next is not None:  # Traverse till the last node
                ptr1 = ptr1.next  # Move ptr1 to the next node
                ptr2 = ptr2.next  # Move ptr2 to the next node
            data1 = ptr2.info  # Store the data of the last node
            ptr1.next = None  # Remove the last node by setting the second last node's next to None
            return node1, data1

def traversal(node1, data1):
    if node1 is None:  # Check if the list is empty after deletion
        print("Linklist Empty after deletion")
    else:
        ptr = node1  # Pointer to traverse the list from the head
        while ptr is not None:
            print(ptr.info)  # Print the data of each node
            ptr = ptr.next  # Move to the next node
    print(f"The element {data1} has been deleted")  # Print which element was deleted

# Creating the linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)
node6 = node(60)

# Linking the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Delete the last node and traverse the remaining list
node1, data1 = delete_operation(node1)
traversal(node1, data1)


