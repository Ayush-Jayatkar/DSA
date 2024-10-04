class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def createNewNode(self, data):
        return Node(data)

    def insert(self, root, newNode):      

        if root is None:
            return newNode
        else:
            if newNode.data >= root.data:
                root.right = self.insert(root.right, newNode)
                print("Node added to right!")
            else:
                root.left = self.insert(root.left, newNode)
                print("Root added to left!")
        return root
    

    def preOrder(self, root):
        if root is None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def menu(self):
        print("1. Insert")
        print("2. Display (Preorder)")
        print("3. Exit")

    def run(self):
        while True:
            self.menu()
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                data = int(input("Enter data: "))
                newNode = self.createNewNode(data)
                self.root = self.insert(self.root, newNode)
            elif choice == 2:
                print("Preorder Traversal:")
                self.preOrder(self.root)
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

# Create an instance of BST and run the menu
objectBST = BST()
objectBST.run()



