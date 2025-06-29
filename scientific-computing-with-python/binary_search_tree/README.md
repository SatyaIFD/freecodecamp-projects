# 🌳 Binary Search Tree in Python

A simple Python implementation of a **Binary Search Tree (BST)** that supports the following operations:

- ✅ Insertion
- 🔍 Search
- ❌ Deletion
- 🔄 Inorder Traversal

---

## 📂 Features

- Object-oriented design with `TreeNode` and `BinarySearchTree` classes.
- Recursive logic for insert, delete, and search operations.
- Inorder traversal returns nodes in sorted order.
- Clean and beginner-friendly Python code.

---

## 📌 Example Usage

```python
bst = BinarySearchTree()

# Insert elements
nodes = [50, 30, 20, 40, 70, 60, 80]
for node in nodes:
    bst.insert(node)

# Search
print(bst.search(80))  # Output: <TreeNode object> or node value

# Inorder traversal
print(bst.inorder_traversal())  # Output: [20, 30, 40, 50, 60, 70, 80]

# Delete node
bst.delete(40)

# Inorder traversal after deletion
print(bst.inorder_traversal())  # Output: [20, 30, 50, 60, 70, 80]
