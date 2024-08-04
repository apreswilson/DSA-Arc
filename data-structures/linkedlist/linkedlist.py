class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)          
        new_node.next = self.head          
        self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insertNewNode(self, key, newNodeData):
        curr = self.head
        
        while curr != None:
            if curr.data == key:
                break
            curr = curr.next

        newNode = Node(newNodeData)
        newNode.next = curr.next
        curr.next = newNode
        return self.head

if __name__ == "__main__":
    llist = LinkedList()
    llist.insertAtBeginning(5)
    llist.insertAtBeginning(4)
    llist.insertAtBeginning(3)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(1)

    llist.printList()

    llist.insertNewNode(2, 2.5)
    llist.printList()
