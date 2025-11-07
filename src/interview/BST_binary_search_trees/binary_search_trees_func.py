from typing import Optional, List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """Insert a value into the BST and return the root."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def search(root: Optional[TreeNode], val: int) -> bool:
    """Search for a value in the BST."""
    if root is None:
        return False
    if root.val == val:
        return True
    return search(root.left, val) if val < root.val else search(root.right, val)


def inorder(root: Optional[TreeNode]) -> List[int]:
    """Return values in sorted order (inorder traversal)."""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 70)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 60)
    root = insert(root, 80)
    
    print(f"Search 40: {search(root, 40)}")  # True
    print(f"Search 100: {search(root, 100)}")  # False
    print(f"Inorder: {inorder(root)}")  # [20, 30, 40, 50, 60, 70, 80]

