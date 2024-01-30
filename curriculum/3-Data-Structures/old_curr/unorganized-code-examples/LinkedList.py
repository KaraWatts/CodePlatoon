# first, let's implement a Node for our LL
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# simple LL only needs these Nodes
simple_ll = Node(1, Node(2, Node(3)))

# we likely want to make a unique class LL though
# because we want to support unique methods it wouldn't
# make sense to add to the Node class

# for simplcitly a LL doesn't take any input initially


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    # add to end
    def append(self, value):
        # make a new node, unattached currently
        new_node = Node(value)
        # special case if head is None
        if self.head == None:
            self.head = new_node
        else:
            self.last.next = new_node
        # either way update last to the new_node
        self.last = new_node

    # add to beginning
    def prepend(self, value):
        new_node = Node(value)
        # special case if head is None
        if self.head == None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def peek(self, index):
        count = 0
        current = self.head

        while count < index:
            count += 1
            current = current.next
        else:
            return current.value

    def insert_at(self, index):
        pass

    def remove_at(self, index):
        pass

    # we want to be able to print our LL to visualize it
    def __str__(self):
        ll_str = ""
        current = self.head

        while current != None:
            ll_str += f"{repr(current.value)} --> "
            current = current.next

        ll_str += "None"

        return ll_str


ll = LinkedList()
print(ll)

ll.append(1)
ll.append(2)
ll.append(3)

print(ll)

ll.prepend(4)
ll.prepend(5)
ll.prepend(6)

print(ll)

print(ll.peek(5))
