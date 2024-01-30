class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def peek(self, index):
        if index < 0:
            raise IndexError("Can't use negative index")

        current = self.head
        count = 0

        while current != None:
            if count == index:
                return current.val
            count += 1
            current = current.next
        else:
            raise IndexError("Out of bounds")

    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
        else:
            self.last.next = new_node

        self.last = new_node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, index, val):
        if index == 0:
            self.prepend(val)
            return

        count = 0
        current = self.head

        while current != None:
            if count == index-1:
                new_node = Node(val)
                new_node.next = current.next
                current.next = new_node
                return
            else:
                count += 1
                current = current.next

    def __str__(self):
        current = self.head
        ll_as_str = ""

        while current != None:
            ll_as_str += f"{repr(current.val)} --> "
            current = current.next
        else:
            ll_as_str += "None"

        return ll_as_str


ll = LinkedList()
print(ll)
ll.prepend(1)
print(ll)
ll.prepend(2)
print(ll)
ll.prepend(3)
print(ll)
ll.prepend(4)
print(ll)
ll.insert_at(4, 5)
print(ll)
