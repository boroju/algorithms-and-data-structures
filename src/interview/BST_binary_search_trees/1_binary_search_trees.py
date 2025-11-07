from typing import Optional, List


class TreeNode:
    """A node in a Binary Search Tree."""
    
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation.
    
    BST Property: For each node, all values in the left subtree are < node.val,
    and all values in the right subtree are > node.val.
    
    Time Complexity:
    - Search: O(h) where h is height, O(log n) average, O(n) worst case
    - Insert: O(h) where h is height, O(log n) average, O(n) worst case
    - Delete: O(h) where h is height, O(log n) average, O(n) worst case
    - Traversals: O(n) where n is number of nodes
    
    Space Complexity:
    - Operations: O(h) for recursion stack, O(1) for iterative
    - Storage: O(n) for n nodes
    
    📚 VISUAL EXPLANATION OF TIME COMPLEXITY:
    See BST_TIME_COMPLEXITY_EXPLAINED.md for detailed graphical explanations!
    
    Quick Visual:
    
    BALANCED TREE (O(log n)) ✅          SKEWED TREE (O(n)) ❌
    ─────────────────────────            ───────────────────
            [50]                         [10]
           /    \                          \
        [30]    [70]                       [20]
        /  \    /  \                         \
      [20][40][60][80]                       [30]
                                               \
    Height: 2, Comparisons: ~2-3              [40]
    ✅ FAST - eliminates 50% each step!        \
                                               [50]
    Height: 6, Comparisons: 7                  \
    ❌ SLOW - eliminates 1 node each step!     [60]
                                               \
                                               [70]
                                                \
                                               [80]
    
    """
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root: Optional[TreeNode] = None
    
    def insert(self, val: int) -> None:
        """
        Insert a value into the BST.
        
        Time Complexity: O(h) where h is height
        - Average case: O(log n) for balanced tree
        - Worst case: O(n) for skewed tree
        
        Args:
            val: The value to insert
        """
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, root: Optional[TreeNode], val: int) -> TreeNode:
        """Helper method for recursive insertion."""
        # Base case: create new node
        if root is None:
            return TreeNode(val)
        
        # Recursive case: traverse to appropriate subtree
        if val < root.val:
            root.left = self._insert_recursive(root.left, val)
        elif val > root.val:
            root.right = self._insert_recursive(root.right, val)
        # If val == root.val, don't insert duplicates (BST property)
        
        return root
    
    def search(self, val: int) -> bool:
        """
        Search for a value in the BST.
        
        Time Complexity: O(h) where h is height
        - Average case: O(log n) for balanced tree
        - Worst case: O(n) for skewed tree
        
        Args:
            val: The value to search for
            
        Returns:
            True if value exists, False otherwise
        """
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, root: Optional[TreeNode], val: int) -> bool:
        """Helper method for recursive search."""
        # Base case: value not found
        if root is None:
            return False
        
        # Base case: value found
        if root.val == val:
            return True
        
        # Recursive case: search appropriate subtree
        if val < root.val:
            return self._search_recursive(root.left, val)
        else:
            return self._search_recursive(root.right, val)
    
    def delete(self, val: int) -> None:
        """
        Delete a value from the BST.
        
        Time Complexity: O(h) where h is height
        - Average case: O(log n) for balanced tree
        - Worst case: O(n) for skewed tree
        
        Args:
            val: The value to delete
        """
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Helper method for recursive deletion."""
        # Base case: value not found
        if root is None:
            return root
        
        # Find the node to delete
        if val < root.val:
            root.left = self._delete_recursive(root.left, val)
        elif val > root.val:
            root.right = self._delete_recursive(root.right, val)
        else:
            # Node to delete found
            # Case 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None
            
            # Case 2: Node has one child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Case 3: Node has two children
            # Find inorder successor (smallest value in right subtree)
            successor = self._find_min(root.right)
            root.val = successor.val
            root.right = self._delete_recursive(root.right, successor.val)
        
        return root
    
    def _find_min(self, root: TreeNode) -> TreeNode:
        """Find the node with minimum value in a subtree."""
        while root.left is not None:
            root = root.left
        return root
    
    def inorder_traversal(self) -> List[int]:
        """
        Perform inorder traversal (Left, Root, Right).
        Returns values in sorted order for BST.
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) for recursion stack
        
        Returns:
            List of values in inorder order
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, root: Optional[TreeNode], result: List[int]) -> None:
        """Helper for inorder traversal."""
        if root is not None:
            self._inorder_recursive(root.left, result)
            result.append(root.val)
            self._inorder_recursive(root.right, result)
    
    def preorder_traversal(self) -> List[int]:
        """
        Perform preorder traversal (Root, Left, Right).
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) for recursion stack
        
        Returns:
            List of values in preorder order
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, root: Optional[TreeNode], result: List[int]) -> None:
        """Helper for preorder traversal."""
        if root is not None:
            result.append(root.val)
            self._preorder_recursive(root.left, result)
            self._preorder_recursive(root.right, result)
    
    def postorder_traversal(self) -> List[int]:
        """
        Perform postorder traversal (Left, Right, Root).
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) for recursion stack
        
        Returns:
            List of values in postorder order
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, root: Optional[TreeNode], result: List[int]) -> None:
        """Helper for postorder traversal."""
        if root is not None:
            self._postorder_recursive(root.left, result)
            self._postorder_recursive(root.right, result)
            result.append(root.val)
    
    def height(self) -> int:
        """
        Calculate the height of the BST.
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) for recursion stack
        
        Returns:
            Height of the tree (number of edges from root to deepest leaf)
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, root: Optional[TreeNode]) -> int:
        """Helper to calculate height."""
        if root is None:
            return -1  # Return -1 for empty tree (edges, not nodes)
        
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)
        
        return 1 + max(left_height, right_height)
    
    def is_valid(self) -> bool:
        """
        Check if the tree satisfies BST properties.
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(h) for recursion stack
        
        Returns:
            True if valid BST, False otherwise
        """
        return self._is_valid_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_recursive(self, root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        """Helper to validate BST property."""
        if root is None:
            return True
        
        # Check if current node violates BST property
        if root.val <= min_val or root.val >= max_val:
            return False
        
        # Recursively check left and right subtrees
        return (self._is_valid_recursive(root.left, min_val, root.val) and
                self._is_valid_recursive(root.right, root.val, max_val))
    

# Example usage and testing
if __name__ == "__main__":
    # Create a BST
    bst = BinarySearchTree()
    
    # Insert values
    print("=== Inserting values ===")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
        print(f"Inserted {val}")
    
    print("\n=== Traversals ===")
    print(f"Inorder (sorted): {bst.inorder_traversal()}")
    print(f"Preorder: {bst.preorder_traversal()}")
    print(f"Postorder: {bst.postorder_traversal()}")
    
    print("\n=== Search operations ===")
    print(f"Search 40: {bst.search(40)}")  # Should be True
    print(f"Search 100: {bst.search(100)}")  # Should be False
    
    print("\n=== Tree properties ===")
    print(f"Height: {bst.height()}")
    print(f"Is valid BST: {bst.is_valid()}")
    
    print("\n=== Delete operations ===")
    print(f"Before deletion - Inorder: {bst.inorder_traversal()}")
    bst.delete(20)  # Delete leaf node
    print(f"After deleting 20 (leaf) - Inorder: {bst.inorder_traversal()}")
    
    bst.delete(30)  # Delete node with one child
    print(f"After deleting 30 (one child) - Inorder: {bst.inorder_traversal()}")
    
    bst.delete(50)  # Delete node with two children
    print(f"After deleting 50 (two children) - Inorder: {bst.inorder_traversal()}")
    