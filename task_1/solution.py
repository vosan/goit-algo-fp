from linked_list import LinkedList, Node


def reverse_linked_list(ll: LinkedList) -> LinkedList:
    """Reverses a linked list in-place

    Args:
        ll: The linked list to be reversed.

    Returns:
        The same linked list instance with its head updated to the reversed list.
    """
    prev = None
    curr = ll.head

    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    ll.head = prev
    return ll


def sort_linked_list(ll: LinkedList, key=None) -> LinkedList:
    """Sort a singly linked list

    Args:
        ll: The linked list to sort.
        key: Optional function mapping node data to a comparison key.

    Returns:
        The same linked list instance with its head updated to the sorted order.
    """

    # Empty or one-element list
    if ll.head is None or ll.head.next is None:
        return ll

    # Collect nodes
    nodes = []
    cur = ll.head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next

    # Sort nodes by their data (with an optional key)
    if key is None:
        nodes.sort(key=lambda n: n.data)
    else:
        nodes.sort(key=lambda n: key(n.data))

    # Re-link in sorted order
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = None

    # Update head and return
    ll.head = nodes[0]
    return ll


def merge_two_sorted_lists(a: LinkedList, b: LinkedList, key=None) -> LinkedList:
    """Merge two sorted singly linked lists into one sorted list.

    Args:
        a: First sorted linked list.
        b: Second sorted linked list.
        key: Optional key function to extract a comparison key from node data.

    Returns:
        A new LinkedList whose head points to the merged sorted sequence.
    """
    key_fn = (lambda x: x) if key is None else key

    pa = a.head
    pb = b.head

    dummy = Node(None)
    tail = dummy

    while pa and pb:
        if key_fn(pa.data) <= key_fn(pb.data):
            tail.next = pa
            pa = pa.next
        else:
            tail.next = pb
            pb = pb.next
        tail = tail.next

    tail.next = pa or pb

    merged = LinkedList()
    merged.head = dummy.next
    return merged


if __name__ == "__main__":
    def _vals(ll: LinkedList):
        """A simple visualization of a linked list"""
        out = []
        cur = ll.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out


    # Reverse demo
    ll = LinkedList()
    for x in [1, 2, 3, 4, 5]:
        ll.insert_at_end(x)
    print("=== Reverse demo ===")
    print("Original:", _vals(ll))
    reverse_linked_list(ll)
    print("Reversed:", _vals(ll))
    print()

    # Sort demo (numbers)
    ll2 = LinkedList()
    for x in [5, 1, 4, 2, 3]:
        ll2.insert_at_end(x)
    print("=== Sort demo (numbers) ===")
    print("Before:", _vals(ll2))
    sort_linked_list(ll2)
    print("After: ", _vals(ll2))
    print()

    # Sort demo (tuples with key)
    people = [("Alice", 30), ("Bob", 25), ("Carol", 35), ("Dave", 25)]
    ll3 = LinkedList()
    for p in people:
        ll3.insert_at_end(p)
    print("=== Sort demo (tuples with key) ===")
    print("Before:", _vals(ll3))
    sort_linked_list(ll3, key=lambda t: t[1])
    print("After: ", _vals(ll3))
    print()

    # Merge demo
    a = LinkedList()
    for x in [1, 3, 5, 7]:
        a.insert_at_end(x)
    b = LinkedList()
    for x in [2, 4, 6, 8]:
        b.insert_at_end(x)
    print("=== Merge demo ===")
    print("A:", _vals(a))
    print("B:", _vals(b))
    merged = merge_two_sorted_lists(a, b)
    print("Merged:", _vals(merged))
    print()
