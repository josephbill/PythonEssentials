# a linear , ordered collection of data consisting of several elements called nodes
# each node points to a next node in the lists
# linked lists are not indexed
# the nodes have a value and a pointer to another node
# otherwise points to a nil if its the end of the list
# linked list increase efficiency of algorithms by allowing access to any item in the list and allowing iterable methods
# to be performed more efficiently i.e. adding and removing items in a list
# if the collection is big and you need to access or remove sth simply use a linked list for efficiency

# defining a linked list
# first define the node class
class Node:
    # the constructor of the node will have a data and next node values as the intialization for the object
    # as each node needs a value and zero or more next node's
    # each node needs to keep track of some data , as well as reference the next node in the list
    def __init__(self, data , next_node = None):
        self.data = data
        self.next_node = next_node

# next we can define the linked list class
class LinkedList:
    #here the head points to the root node i.e. start of the linked lists
    def __init__(self, head = None):
        self.head = head

    # next we define an append method that should add a node to the start of the list if empty or end of list if not empty
    def append(self,node):
        # add element to root if empty
        if self.head == None:
            self.head = node
            return
        # else if not empty , look through the list to find the last node
        last_node = self.head
        # last_node.next_node : check if current last_node exists
        while last_node.next_node:
            # update the value of the last_node to the next node in the list
            last_node = last_node.next_node
        # add node to the end
        last_node.next_node = node


# so lets build out the linked lists : of pl teams
list = LinkedList()
list.append(Node("Manchester City"))
list.append(Node("Arsenal"))
list.append(Node("Newcastle United"))
list.append(Node("Liverpool"))
print(list)