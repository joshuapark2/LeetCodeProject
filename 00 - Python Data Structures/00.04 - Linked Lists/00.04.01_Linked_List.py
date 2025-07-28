class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next # next literally means go to the next node and establish the link

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node # Updating Head
  
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    
    while itr.next:
      itr = itr.next
    
    itr.next = Node(data, None)

  def insert_values(self, data_list):
    self.head = None # Wipping out all values
    for data in data_list:
      self.insert_at_end(data)
  
  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      raise Exception("Invalid Index")

    if index == 0: # Trying to remove the head - at the beginning
      self.head = self.head.next # Garbage Collection Automatically in Python
      return

    count = 0 # LinkedList must manually keep track of count
    itr = self.head
    while itr:
      # Must remove element prior is what we want to remove and remove that link
      if count == index - 1:
        itr.next = itr.next.next # We simply re-configure out link
        break

      itr = itr.next
      count += 1
    
  def insert_at(self, index, data):
    if index < 0 or index > self.get_length():
      raise Exception("Invalid Index")
    
    if index == 0:
      self.insert_at_beginning(data)
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1: # At the element prior to where we want to insert
        node = Node(data, itr.next)
        itr.next = node
        break

      itr = itr.next

      count += 1
  
  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next

    return count
  
  # Exercise: LinkedList
  # Goal: find specific data name and insert data after that values
  def insert_after_value(self, data_after, data_to_insert):
    if self.head is None: # If we don't have any values available - ADDING SOLUTION
      return
    
    if self.head.data == data_after: # If the swap is the first element - ADDING SOLUTION
      self.head.next = Node(data_to_insert, self.head.next)
      return

    itr = self.head
    while itr:
      if itr.data == data_after:
        node = Node(data_to_insert, itr.next)
        itr.next = node
        break
      itr = itr.next
  
  def remove_by_value(self, data):
    if self.head is None:
      return

    if self.head.data == data:
      self.head = self.head.next # Automatic garbage collecting
      return

    itr = self.head
    while itr.next: # While there is a next node and not NULL
      if itr.next.data == data:
        itr.next = itr.next.next
        break
      itr = itr.next

  def print(self):
    if self.head is None:
      print("Linked List is Empty")
      return

    iterator = self.head
    linkListString = ''

    while iterator:
      linkListString += str(iterator.data) + ' --> '
      iterator = iterator.next # Iterating one by one
    print(linkListString)

if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_at_beginning(5)
  ll.insert_at_beginning(89)
  ll.insert_at_end(23)
  
  ll.insert_values(['iron', 'gold', 'diamond'])
  ll.remove_at(1)

  ll.insert_at(0, 'bronze')
  ll.insert_at(3, 'obsidian')

  ll.insert_after_value('iron', 'cobblestone')
  ll.remove_by_value('obsidian')

  ll.print()
  print(ll.get_length())