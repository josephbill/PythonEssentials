# a doubly linked list contains two pointers , the next node and the previous node file
# defining a doubly linked list is as simple as adding a previous node defination in the constructor of a node in the list
class Node:
  def __init__(self, data, next_node = None, prev_node = None):
    self.data = data
    self.next_node = next_node
    self.prev_node = prev_node

# we can then make the append method more efficient by keeping track of the previous node
# in a single linked lists , we need to trasverse through all nodes to get to the last node

class SinglyLinkedList:

  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def append(self, node):
    # Add element to the beginning of the list if the list is empty
    if self.head == None:
        self.head = node
        self.tail = node
        return
    # no need to traverse! we can access the last node directly (self.tail)
    # 1 -> 2 -> 3
    self.tail.next_node = node
    # 1 -> 2 -> 3 -> 4
    # we also need to make sure to keep track of the new tail

    self.tail = node


# say we wanted to remove the last node in a singlylinked list this means we have to trasverse the list to get to the end
# with a doublylinked list we can get the last node by referencing the tails

class DoublyLinkedList:

  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

 # adding node to end or root of the list
  def append(self, node):
    if self.head == None:
        self.head = node
        self.tail = node
        return
    node.prev_node = self.tail
    self.tail.next_node = node
    self.tail = node

 #updating node value , according to a target data
  def update_node(self, target_data, new_data):
      current_node = self.head
      while current_node:
          if current_node.data == target_data:
              current_node.data = new_data
              break
          current_node = current_node.next_node

  #printing all elements in a linked list.
  def print_all_elements(self):
      current_node = self.head
      while current_node:
          print(current_node.data)
          current_node = current_node.next_node


# linked list use pointers to reference their nodes and not indexes , next_node points to next node , prev_node points to previous node ,
# current_node points to the current node

examplelist = DoublyLinkedList()
# append
examplelist.append(Node("Manchester City"))
examplelist.append(Node("Liverpool"))
examplelist.append(Node("Arsenal"))
# print elements
examplelist.print_all_elements()
# update elements
examplelist.update_node("Arsenal", "Newcastle United")
# print elements
examplelist.print_all_elements()