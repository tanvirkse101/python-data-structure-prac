class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new):
        new = Node(new)
        new.next = self.head
        self.head = new

    def insertAfter(self, prev, new):
        if prev is None:
            print("The previous node must be in the linked list")
            return
        new = Node(new)
        new.next = prev.next
        prev.next = new

    def append(self, new):
        new = Node(new)
        if self.head is None:
            self.head = new
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()
    array = [1, 5, 9, 6, 8, 9, 33, 0]
    for i in range(0, len(array)):
        linked_list.append(array[i])
    linked_list.printList()
