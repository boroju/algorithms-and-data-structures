from typing import Optional, List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, val: int) -> None:
        """Insert a value into the BST."""
        self.root = self._insert(self.root, val)
    
    def _insert(self, root: Optional[TreeNode], val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)
        return root
    
    def search(self, val: int) -> bool:
        """Search for a value in the BST."""
        return self._search(self.root, val)
    
    def _search(self, root: Optional[TreeNode], val: int) -> bool:
        if root is None:
            return False
        if root.val == val:
            return True
        return self._search(root.left, val) if val < root.val else self._search(root.right, val)
    
    def inorder(self) -> List[int]:
        """Return values in sorted order (inorder traversal)."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, root: Optional[TreeNode], result: List[int]) -> None:
        if root:
            self._inorder(root.left, result)
            result.append(root.val)
            self._inorder(root.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    print(f"Search 40: {bst.search(40)}")  # True
    print(f"Search 100: {bst.search(100)}")  # False
    print(f"Inorder: {bst.inorder()}")  # [20, 30, 40, 50, 60, 70, 80]

