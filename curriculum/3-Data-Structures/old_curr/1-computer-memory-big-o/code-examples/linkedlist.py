class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LL:
    def __init__(self, head):
        self.head = head
        self.last_index = head

    def get_by_index(self, index):
        current = self.head
        current_index = 0

        while (current_index < index):
            assert current.next != None, "Out of bounds!"
            current = current.next
            current_index += 1

        return current.value

    def append(self, value):
        new_node = Node(value)
        self.last_index.next = new_node
        self.last_index = new_node


ll = LL(Node(1))
ll.append(4)

print(ll.get_by_index(1))  # 4

ll.append(12)
ll.append(2)
ll.append(7)

print(ll.get_by_index(4))  # 7
