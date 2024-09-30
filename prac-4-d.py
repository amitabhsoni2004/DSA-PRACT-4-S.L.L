# Insertion after a particular element in S.L.L

class node: 
    def __init__(self, data):
        self.info = data  # Assign the value to the node
        self.next = None  # Initialize the next pointer as None
        
def insert_operation(node1, data1):
    node6 = node(35)  # Create a new node with the value 35
    
    if node1 is None:
        print("Linklist empty, data not found..")  # Handle empty linked list
        return
    else:
        ptr = node1  # Start from the head of the list
        while ptr is not None and ptr.info != data1: 
            ptr = ptr.next  # Traverse the list until the desired element is found

        if ptr is None:
            print(f"Element {data1} not found, insertion not possible.")  # Element not found
        else:
            node6.next = ptr.next  # Link new node to the next node
            ptr.next = node6  # Insert the new node after the found node
            return True  # Indicate successful insertion
      
def traversal(node1):
    if node1 is None:
        print("Linklist empty..")  # Handle empty linked list
    else:   
        ptr1 = node1  # Start from the head of the list
        while ptr1 is not None: 
            print(ptr1.info)  # Print the current node's data
            ptr1 = ptr1.next  # Move to the next node
          
# Creating nodes for the linked list
node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

# Linking the nodes together to form the linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

data1 = 30  # Element after which the new node will be inserted
inserted = insert_operation(node1, data1)  # Perform the insertion

# Check if the insertion was successful before traversal
if inserted:
    traversal(node1)  # Print the updated linked list
