#Delete middle node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to delete middle node from linked list.
def deleteMid(head):
    # Edge case: return None if there is only
    # one node.
    if head.next is None:
        return None

    count = 0
    p1 = head
    p2 = head

    # First pass, count the number of nodes
    # in the linked list using 'p1'.
    while p1 is not None:
        count += 1
        p1 = p1.next

    # Get the index of the node to be deleted.
    middleIndex = count // 2

    # Second pass, let 'p2' move toward the predecessor
    # of the middle node.
    for i in range(middleIndex - 1):
        p2 = p2.next

    # Delete the middle node and return 'head'.
    p2.next = p2.next.next
    return head

def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    # Create a static hardcoded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5.
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original Linked List:", end=" ")
    printList(head)

    # Delete the middle node.
    head = deleteMid(head)

    print("Linked List after deleting the middle node:", end=" ")
    printList(head)
