# TreeNode represents each node in the binary search tree
class TreeNode:
    def __init__(self, key):
        self.key = key      # Node's value
        self.left = None    # Left child
        self.right = None   # Right child

    def __str__(self):
        return str(self.key)


# BinarySearchTree class that supports insertion, deletion, search, and inorder traversal
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Root of the BST

    # Helper method to recursively insert a new key into the BST
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)  # If we reach a null spot, insert the key here

        # Recursively insert in left or right subtree
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node  # Return the unchanged node pointer

    # Public method to insert a key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Helper method to recursively search for a key
    def _search(self, node, key):
        # Base cases: empty tree or key is present at the node
        if node is None or node.key == key:
            return node

        # Key is smaller than root's key, search left subtree
        if key < node.key:
            return self._search(node.left, key)

        # Key is greater, search right subtree
        return self._search(node.right, key)

    # Public method to search for a key
    def search(self, key):
        return self._search(self.root, key)

    # Helper method to delete a node with a given key
    def _delete(self, node, key):
        if node is None:
            return node  # Base case: key not found

        # Recur down the tree
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            node.key = self._min_value(node.right)

            # Delete the inorder successor
            node.right = self._delete(node.right, node.key)

        return node

    # Public method to delete a key
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Helper function to find the minimum value in a given subtree
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    # Helper function for inorder traversal
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)  # Visit the node
            self._inorder_traversal(node.right, result)

    # Public method to perform inorder traversal
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result


# Example usage
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert nodes into BST
for node in nodes:
    bst.insert(node)

# Search for a key
print('Search for 80:', bst.search(80))  # Should return a TreeNode

# Inorder traversal before deletion
print("Inorder traversal:", bst.inorder_traversal())  # Sorted order

# Delete a node
bst.delete(40)

# Search for deleted node
print("Search for 40:", bst.search(40))  # Should return None

# Inorder traversal after deletion
print('Inorder traversal after deleting 40:', bst.inorder_traversal())
