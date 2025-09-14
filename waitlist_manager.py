# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None
    
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        return(f'{name} added to the front of the waitlist.')

    def print_list(self):
        if not self.head:
            print('The waitlist is empty.')
            return
        print('Current waitlist:')
        current = self.head
        while current:
            print(f'- {current.name}')
            current = current.next
    
    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return f'{name} added to the end of the waitlist.'
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return f'{name} added to the end of the waitlist.'
    
    def remove(self, name):
        current = self.head
        previous = None

        while current:
            if current.name == name:
                if previous:  
                    previous.next = current.next
                else:  
                    self.head = current.next
                return f'Removed {name} from the waitlist.'
            previous = current
            current = current.next

        return f'{name} not found.'
    
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            print(waitlist.add_front(name))

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))
            
        elif choice == "4":
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
# This program uses a linked list to manage a waitlist. A linked list is a chain of nodes, where each node stores a customer’s 
# name and a link to the next node. The LinkedList class keeps track of the head, which points to the first node in the list. 
# The head is very important because it is the starting point to find every customer on the list. If we lose the head, we 
# would lose access to the entire waitlist.

# When we add a customer to the front, we create a new node and make its “next” pointer lead to the current head. Then we 
# update the head to point to this new node, making it the first in line. When we add a customer to the end, we walk through 
# the list until we reach the last node and connect the new node there. Removing a customer works by searching the list until 
# we find the matching name and then adjusting the links so that the node is skipped. Printing the list starts from the head 
# and goes through every node until the end, showing all the names in order. I added a dash to make it look better.

# A real engineer might use a custom linked list when they need quick inserts and deletes without moving other data, or when 
# the size of the list changes a lot. Linked lists are useful in situations like managing queues, undo/redo actions, or when 
# building systems where memory should grow as needed instead of in fixed chunks.

