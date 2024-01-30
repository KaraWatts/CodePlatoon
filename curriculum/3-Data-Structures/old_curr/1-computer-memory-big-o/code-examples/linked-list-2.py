class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LL:
    def __init__(self, head=None):
        self.head = head
        self.last_index = None

        current = self.head

        while current.next:
            current = current.next
        else:
            self.last_index = current

    def __str__(self):
        output_str = ""

        current = self.head

        while current.next:
            output_str += repr(current.value) + " --> "
            current = current.next
        else:
            output_str += repr(current.value) + " --/\n"

        return output_str

    def walkthrough(self):
        current = self.head
        index = 0

        while current:
            print(
                f"ll[{index}] = [ value: {repr(current.value)}, next: {id(current.next)} @ {id(current)}")
            index += 1
            current = current.next


ll = LL(Node(4, Node(44, Node(-72))))

print(ll)
ll.walkthrough()

arr = [1, 2, 3]
print(arr[0], id(arr[0]))
print(arr[1], id(arr[1]))
print(arr[2], id(arr[2]))

arr.append(4)
print(arr[3], id(arr[3]))
