class Node:
  def __init__(self, data = None, next = None, prev = None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None
  
  def print_foward(self):
    if self.head is None:
      print("Doubly Linked List is empty")
      return

    curr = self.head
    dllstr = ''

    while curr:
      dllstr += str(curr.data) + ' --> '
      curr = curr.next
    print("DLL in order: ", dllstr)

  def print_backward(self):
    if self.head is None:
      print("DLL is empty")
      return
    
    last_node = self.get_last_node()
    curr = last_node
    dllstr = ''

    while curr:
      dllstr += curr.data + ' --> '
      curr = curr.prev
    print("DLL in reverse: ", dllstr)
  
  def get_last_node(self):
    curr = self.head
    while curr.next:
      curr = curr.next
    
    return curr

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return

    itr = self.head

    while itr.next:
      itr = itr.next

    itr.next = Node(data, None, itr)

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
  
if __name__ == '__main__':
  dll = DoublyLinkedList()
  dll.insert_values(['Queens', 'FocusedPotato', 'Selly', 'b.ngoc'])
  dll.print_foward()
  dll.print_backward()
