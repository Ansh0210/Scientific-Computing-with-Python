# Define a TreeNode class to represent each node in the binary search tree.
class TreeNode:
    def __init__(self, key):
        self.key = key       # Node's value.
        self.left = None     # Pointer to left child.
        self.right = None    # Pointer to right child.

    def __str__(self):
        return str(self.key) # String representation of the node.


# Define a BinarySearchTree class to encapsulate BST operations.
class BinarySearchTree:
    def __init__(self):
        self.root = None    # Initialize the root of the BST.

    # Public method to insert a new key in the BST.
    def insert(self, key):
        self.root = self._insert(self.root, key) # Start insertion from the root.

    # Helper method to insert a new key into the BST, used recursively.
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key) # Create a new node if the spot is found.
        if key < node.key:
            node.left = self._insert(node.left, key) # Recurse left for smaller keys.
        elif key > node.key:
            node.right = self._insert(node.right, key) # Recurse right for larger keys.
        return node # Return the unchanged node pointer.

    # Public method to search for a key in the BST.
    def search(self, key):
        return self._search(self.root, key) # Start searching from the root.

    # Helper method to search for a key in the BST, used recursively.
    def _search(self, node, key):
        if node is None or node.key == key:
            return node # Return the node if found or end of path.
        if key < node.key:
            return self._search(node.left, key) # Recurse left for smaller keys.
        return self._search(node.right, key) # Recurse right for larger keys.

    # Public method to delete a key from the BST.
    def delete(self, key):
        self.root = self._delete(self.root, key) # Start deletion from the root.

    # Helper method to delete a key from the BST, used recursively.
    def _delete(self, node, key):
        if node is None:
            return node # If the node is not found, return None.
        if key < node.key:
            node.left = self._delete(node.left, key) # Recurse left for smaller keys.
        elif key > node.key:
            node.right = self._delete(node.right, key) # Recurse right for larger keys.
        else:
            # Node with only one child or no child.
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children: Get the inorder successor (smallest in the right subtree).
            node.key = self._min_value(node.right)
            # Delete the inorder successor.
            node.right = self._delete(node.right, node.key)
        return node

    # Helper method to find the minimum value node in a given subtree.
    def _min_value(self, node):
        current = node
        # Loop down to find the leftmost leaf.
        while current.left is not None:
            current = current.left
        return current.key

    # Public method for inorder traversal of the BST.
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result) # Populate result starting from the root.
        return result

    # Helper method to perform inorder traversal of a BST, used recursively.
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result) # Traverse left subtree.
            result.append(node.key) # Visit node.
            self._inorder_traversal(node.right, result) # Traverse right subtree.


# Example usage of the BinarySearchTree class.
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node) # Insert nodes into the BST.
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40) # Delete a node from the BST.
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))