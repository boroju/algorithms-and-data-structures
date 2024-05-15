from collections import deque


# Define the TreeNode class for the binary tree nodes
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Function to construct a binary tree from the input series
def construct_binary_tree(inorder):
    # If input list is empty, return None
    if not inorder:
        return None

    # Create the root node using the first element of the input series
    root = TreeNode(inorder[0])

    # Initialize a queue to store nodes during construction
    queue = deque([root])

    # Index to traverse the input series
    i = 1

    # Iterate through the input series, starting from the second element
    while queue and i < len(inorder):
        # Dequeue a node from the queue
        node = queue.popleft()

        # Create a left child node with the current element and enqueue it
        left_val = inorder[i]
        i += 1
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)

        # Increment the index to get the next element from the input series
        # Create a right child node with the next element and enqueue it
        if i < len(inorder):
            right_val = inorder[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)

    # Return the root of the binary tree
    return root


# Function to perform level-order traversal of the binary tree
def level_order_traversal(root):
    # If the root is None, return an empty list
    if not root:
        return []

    # Initialize a list to store the traversal result
    result = []

    # Initialize a queue with the root node
    queue = deque([root])

    # Perform level-order traversal
    while queue:
        # Initialize a list to store the nodes at the current level
        level = []
        # Get the number of nodes at the current level
        level_size = len(queue)
        # Traverse all nodes at the current level
        for _ in range(level_size):
            # Dequeue a node from the queue
            node = queue.popleft()
            # Append the value of the node to the current level list
            level.append(node.val)
            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)
            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)
        # Append the current level list to the result
        result.append(level)

    # Return the level-order traversal result
    return result


if __name__ == "__main__":

    # Example usage
    inorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = construct_binary_tree(inorder)
    result = level_order_traversal(root)
    print(result)
