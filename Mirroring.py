class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self._insert_rec(self.root, x)

    def _insert_rec(self, node, x):
        if x < node.data:
            if node.left is None:
                node.left = Node(x)
            else:
                self._insert_rec(node.left, x)
        else:
            if node.right is None:
                node.right = Node(x)
            else:
                self._insert_rec(node.right, x)

    def mirror(self, node):
        if node is None:
            return None
        
        left = self.mirror(node.left)
        right = self.mirror(node.right)

        node.left = right
        node.right = left

        return node

    def copy(self, node):
        if node is None:
            return None
        
        new_node = Node(node.data)
        new_node.left = self.copy(node.left)
        new_node.right = self.copy(node.right)

        return new_node

    def print_parents_and_children(self, node):
        if node:
            if node.left or node.right:
                print(f"Parent: {node.data}, Left Child: {node.left.data if node.left else None}, Right Child: {node.right.data if node.right else None}")
            self.print_parents_and_children(node.left)
            self.print_parents_and_children(node.right)

    def print_leaf_nodes(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            self.print_leaf_nodes(node.left)
            self.print_leaf_nodes(node.right)

if __name__ == "__main__":
    bst = BST()
    
    # Input elements for the BST
    elements = input("Enter the elements of the BST (space-separated): ")
    arr = list(map(int, elements.split()))
    
    for element in arr:
        bst.insert(element)

    print("\nOriginal BST (In-order):")
    bst.print_parents_and_children(bst.root)

    # Mirror the BST
    bst.mirror(bst.root)
    print("\nMirrored BST (In-order):")
    bst.print_parents_and_children(bst.root)

    # Create a copy of the BST
    copied_tree = bst.copy(bst.root)
    print("\nCopied BST (In-order):")
    bst.print_parents_and_children(copied_tree)

    print("\nLeaf nodes of the original BST:")
    bst.print_leaf_nodes(bst.root)
