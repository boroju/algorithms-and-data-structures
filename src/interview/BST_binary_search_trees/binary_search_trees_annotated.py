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
    
    ═══════════════════════════════════════════════════════════════
    🎯 WHEN TO USE BST vs WHEN NOT TO USE BST
    ═══════════════════════════════════════════════════════════════
    
    ✅ USE BST WHEN:
    
    1. Need Fast Search (O(log n))
       Use Case: User database lookup
       Example: Finding a user by ID in a system with 1M users
       - BST: ~20 comparisons (log₂(1M) ≈ 20)
       - Array: Up to 1M comparisons in worst case
       - Winner: BST ✅
    
    2. Need Sorted Order Maintained
       Use Case: Leaderboard system
       Example: Game scores that need to stay sorted as players update scores
       - BST: Automatically maintains sorted order on insert/delete
       - Array: Need to sort after every change (O(n log n))
       - Winner: BST ✅
    
    3. Need Range Queries
       Use Case: Calendar application finding events between two dates
       Example: "Show all meetings between Jan 15 and Feb 20"
       - BST: Efficiently find all values in range (O(log n + k) where k = results)
       - Hash Table: Must check every entry (O(n))
       - Winner: BST ✅
    
    4. Frequent Insertions/Deletions with Search
       Use Case: Real-time inventory system
       Example: Products added/removed frequently, need to search by price
       - BST: O(log n) for all operations (insert, delete, search)
       - Array: O(n) for insert/delete, O(log n) for search (if sorted)
       - Winner: BST ✅
    
    5. Need Inorder Traversal (Sorted Output)
       Use Case: Displaying sorted data
       Example: Showing products sorted by price
       - BST: Inorder traversal gives sorted order automatically
       - Hash Table: Need to extract and sort (O(n log n))
       - Winner: BST ✅
    
    ❌ DON'T USE BST WHEN:
    
    1. Need O(1) Lookups → Use Hash Table Instead
       Use Case: User session cache
       Example: Looking up user session by session ID (no ordering needed)
       - BST: O(log n) lookup
       - Hash Table: O(1) average lookup
       - Winner: Hash Table ✅
       Real Example: Redis cache, browser cookies
    
    2. Need Priority Queue → Use Heap Instead
       Use Case: Task scheduler
       Example: Always need the highest priority task (don't need full sorted order)
       - BST: O(log n) to get min/max, but overkill
       - Heap: O(log n) insert, O(1) to peek min/max, O(log n) to pop
       - Winner: Heap ✅
       Real Example: Operating system task scheduling, Dijkstra's algorithm
    
    3. Simple Sequential Access → Use Array/List Instead
       Use Case: Twitter feed (chronological order)
       Example: Displaying tweets in order they were posted
       - BST: O(n) to traverse, unnecessary complexity
       - Array/List: O(1) to append, O(n) to display (natural order)
       - Winner: Array/List ✅
       Real Example: News feed, chat messages, log files
    
    4. No Ordering Needed → Use Hash Table Instead
       Use Case: Word frequency counter
       Example: Counting how many times each word appears (order doesn't matter)
       - BST: Maintains order you don't need
       - Hash Table: O(1) insert/update, simpler
       - Winner: Hash Table ✅
       Real Example: Cache systems, counting occurrences
    
    5. Need Index-Based Access → Use Array Instead
       Use Case: Image pixel data
       Example: Accessing pixel at position [x][y]
       - BST: Can't access by index
       - Array: O(1) access by index
       - Winner: Array ✅
       Real Example: Matrices, images, grids
    
    6. Very Small Dataset (< 100 items) → Use Array Instead
       Use Case: Small shopping cart
       Example: Cart with 10-20 items
       - BST: Overhead of tree structure not worth it
       - Array: Simple, fast enough for small data
       - Winner: Array ✅
       Real Example: Small lists, simple counters
    
    ═══════════════════════════════════════════════════════════════
    📊 QUICK DECISION GUIDE
    ═══════════════════════════════════════════════════════════════
    
    Ask yourself:
    
    1. Do I need sorted order? 
       YES → Consider BST
       NO → Consider Hash Table
    
    2. Do I need O(1) lookups?
       YES → Use Hash Table
       NO → Consider BST
    
    3. Do I need range queries?
       YES → Use BST ✅
       NO → Consider Hash Table
    
    4. Do I need priority queue (min/max)?
       YES → Use Heap
       NO → Consider BST
    
    5. Is my data small (< 100 items)?
       YES → Use Array (simpler)
       NO → Consider BST
    
    6. Do I need index-based access?
       YES → Use Array
       NO → Consider BST
    
    ═══════════════════════════════════════════════════════════════
    💡 REAL-WORLD EXAMPLES
    ═══════════════════════════════════════════════════════════════
    
    ✅ BST IS USED IN:
    - Database indexes (B-trees are BST variants)
    - Python's sortedcontainers library
    - Java's TreeMap, TreeSet
    - C++'s std::map, std::set
    - Calendar applications (range queries for dates)
    - Event schedulers (finding events in time range)
    - Auto-complete systems (prefix matching with Trie, which is tree-based)
    
    ❌ BST IS NOT USED IN:
    - Web session storage → Hash Table (O(1) lookup)
    - Task queues → Heap (priority-based)
    - Simple lists → Array (sequential access)
    - Caching → Hash Table (no ordering needed)
    - Counting frequencies → Hash Table (no ordering needed)
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
        # If val == root.val, we don't insert duplicates (BST property)
        
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
    
    def has_cycle(self) -> bool:
        """
        Detect if the BST contains a cycle (making it a graph).
        
        When a BST has a cycle:
        - It becomes a Directed Graph (specifically a Directed Cyclic Graph)
        - BST operations (search, traversal) will cause INFINITE LOOPS
        - The tree structure is broken - it's no longer a valid tree
        
        Time Complexity: O(n) where n is number of nodes
        Space Complexity: O(n) for recursion stack and visited set
        
        Returns:
            True if cycle exists, False otherwise
        """
        visited = set()
        rec_stack = set()  # Track nodes in current recursion path
        return self._has_cycle_dfs(self.root, visited, rec_stack)
    
    def _has_cycle_dfs(self, node: Optional[TreeNode], visited: set, rec_stack: set) -> bool:
        """
        Helper method to detect cycles using DFS with recursion stack.
        
        A cycle exists if we encounter a node that's already in the current
        recursion path (not just visited, but actively being processed).
        """
        if node is None:
            return False
        
        # If node is in recursion stack, we found a back edge (cycle)
        if node in rec_stack:
            return True
        
        # If node already visited (but not in current path), no cycle through this path
        if node in visited:
            return False
        
        # Mark as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Check left and right children
        if self._has_cycle_dfs(node.left, visited, rec_stack):
            return True
        if self._has_cycle_dfs(node.right, visited, rec_stack):
            return True
        
        # Remove from recursion stack (backtracking)
        rec_stack.remove(node)
        
        return False
    
    def get_graph_info(self) -> dict:
        """
        Analyze the structure: Is it a Tree or Graph?
        
        Returns:
            Dictionary with structure information
        """
        has_cycle = self.has_cycle()
        is_valid_bst = self.is_valid() if not has_cycle else False
        
        return {
            "has_cycle": has_cycle,
            "structure_type": "Directed Cyclic Graph" if has_cycle else "Binary Tree",
            "is_valid_bst": is_valid_bst,
            "can_perform_operations": not has_cycle,
            "warning": "⚠️  INFINITE LOOP RISK: Operations will cause RecursionError!" if has_cycle else None
        }


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
    
    print("\n" + "="*70)
    print("🔴 CYCLE DETECTION DEMONSTRATION")
    print("="*70)
    
    # Create a BST with a cycle
    print("\n=== Creating BST with cycle ===")
    bst_cycle = BinarySearchTree()
    bst_cycle.insert(50)
    bst_cycle.insert(30)
    bst_cycle.insert(70)
    bst_cycle.insert(20)
    bst_cycle.insert(40)
    
    print("Normal BST structure:")
    print("        [50]")
    print("       /    \\")
    print("    [30]    [70]")
    print("    /  \\")
    print("  [20][40]")
    
    # Manually create a cycle: 40 -> 30 (loops back)
    print("\n⚠️  Adding cycle: 40.right -> 30 (loops back to parent)")
    node_30 = bst_cycle.root.left  # Get node 30
    node_40 = bst_cycle.root.left.right  # Get node 40
    node_40.right = node_30  # Create cycle: 40 -> 30
    
    print("BST with cycle:")
    print("        [50]")
    print("       /    \\")
    print("    [30]    [70]")
    print("    /  \\")
    print("  [20][40]─┐")
    print("           │")
    print("           └─── (loops back to 30)")
    
    # Test cycle detection and get graph info
    print("\n=== Testing cycle detection ===")
    graph_info = bst_cycle.get_graph_info()
    print(f"Has cycle: {graph_info['has_cycle']}")
    print(f"Structure type: {graph_info['structure_type']}")
    print(f"Is valid BST: {graph_info['is_valid_bst']}")
    print(f"Can perform operations: {graph_info['can_perform_operations']}")
    if graph_info['warning']:
        print(f"{graph_info['warning']}")
    
    print("\n" + "="*70)
    print("📊 WHAT HAPPENS WHEN BST BECOMES A GRAPH?")
    print("="*70)
    
    print("\n1. STRUCTURE CHANGE:")
    print("   Tree → Directed Cyclic Graph (DCG)")
    print("   - Trees: No cycles, one path between any two nodes")
    print("   - Graphs: Can have cycles, multiple paths possible")
    
    print("\n2. OPERATIONS BREAK:")
    print("   ❌ Search: Will loop infinitely in cycle")
    print("   ❌ Traversal: Will loop infinitely in cycle")
    print("   ❌ Insert/Delete: May cause infinite recursion")
    print("   ❌ Height calculation: Will stack overflow")
    
    print("\n3. WHY IT HAPPENS:")
    print("   - Normal BST: Each node visited once (tree property)")
    print("   - With cycle: Node can be visited multiple times")
    print("   - Recursive algorithms assume tree structure → infinite loop")
    
    print("\n4. VISUAL REPRESENTATION:")
    print("   Normal BST (Tree):")
    print("        [50]")
    print("       /    \\")
    print("    [30]    [70]")
    print("    /  \\")
    print("  [20][40]")
    print("   ✅ Each node has one parent, no cycles")
    
    print("\n   BST with Cycle (Graph):")
    print("        [50]")
    print("       /    \\")
    print("    [30]◄───┐")
    print("    /  \\    │")
    print("  [20][40]──┘")
    print("   ❌ Cycle: 30 → 40 → 30 (infinite loop)")
    
    print("\n5. DETECTION:")
    print("   Use DFS with visited set to detect cycles")
    print("   Time: O(n), Space: O(n)")
    
    print("\n6. SOLUTION:")
    print("   - Detect cycles before operations")
    print("   - Use iterative algorithms with visited tracking")
    print("   - Or fix the structure (remove cycle)")
