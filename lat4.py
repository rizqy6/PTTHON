class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtMiddle(self, middle_node, data):
        if not middle_node:
            print("The mentioned node is absent")
            return
        new_node = Node(data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = None
        curr_node = self.head
        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def hitung_nodes(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
linked_list = LinkedList()
linked_list.insertAtEnd(5)
linked_list.insertAtEnd(10)
linked_list.insertAtStart(3)
middle_node = linked_list.head.next
linked_list.insertAtMiddle(middle_node, 7)
linked_list.print_list() # Output: 3 5 7 10
print(linked_list.hitung_nodes()) # Output: 4
linked_list.reverse()
linked_list.print_list() # Output: 10 7 5 3
