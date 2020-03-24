"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = ListNode(value)

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1


    def remove_from_head(self):
        if not self.head:
            return None

        value = self.head.value
        self.delete(self.head)

        return value

    def add_to_tail(self, value):
        node = ListNode(value)
        
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail.prev = self.tail
            self.tail = node
        
        self.length += 1

    def remove_from_tail(self):
        if not self.tail:
            return None
        
        value = self.tail.value
        self.delete(self.tail)

        return value

    def move_to_front(self, node):
        if node is self.head:
            return
        
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if self.head is self.tail:
            self.head = None
            self.tail = None

        elif node is self.head:
            self.head = self.head.next
            node.delete()
        
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        
        self.length -= 1

    def get_max(self):
        max_value = self.head.value
        current = self.head

        while current:
            if current.value > max_value:
                max_value = current.value

            current = current.next            
        
        return max_value


