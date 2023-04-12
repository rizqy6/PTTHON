class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
    def insertAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertAtMiddle(self, middle_node, data):
        new_node = Node(data)
        if middle_node is None:
            print("Middle node tidak ditemukan")
            return
        new_node.next = middle_node.next
        middle_node.next = new_node
        
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
    def print_list(self):
        if self.head is None:
            print("LinkedList kosong")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
                
    def hitung_nodes(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
# membuat object LinkedList
my_list = LinkedList()

# menambahkan node baru ke akhir LinkedList
my_list.insertAtEnd(1)
my_list.insertAtEnd(2)
my_list.insertAtEnd(3)

# menambahkan node baru di awal LinkedList
my_list.insertAtStart(0)

# menyisipkan node baru sebelum node dengan nilai 2
node2 = my_list.head.next.next
my_list.insertAtMiddle(node2, 2.5)

# mencetak isi LinkedList
my_list.print_list() # output: 0 1 2 2.5 3

# menghapus node dengan nilai 2.5
my_list.delete(2.5)

# mencetak isi LinkedList
my_list.print_list() # output: 0 1 2 3

# menghitung jumlah node dalam LinkedList
print(my_list.hitung_nodes()) # output: 4

# membalik urutan node dalam LinkedList
my_list.reverse()

# mencetak isi LinkedList yang sudah dibalik
my_list.print_list() # output: 3 2 1 0
