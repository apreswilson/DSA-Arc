class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None

    def add_to_front(self, dataToAdd):
        new_node = Node(dataToAdd)
        new_node.next = self.head
        self.head = new_node

    def remove_duplicate(self):
        current = self.head

        if current is None:
            return

        while current.next is not None:
            if current.data == current.next.data:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next
        return self.head

    def print_list(self):
        current = self.head

        while (current):
            print(current.data)
            current = current.next

if __name__ == "__main__":
    llist = linkList()
    llist.add_to_front(1)
    llist.add_to_front(2)
    llist.add_to_front(3)
    llist.add_to_front(4)
    llist.add_to_front(4)
    llist.add_to_front(5)
    llist.print_list()
    llist.remove_duplicate()
    llist.print_list()
