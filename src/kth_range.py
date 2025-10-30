# kth_range.py

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    """Insert val into BST (ignore duplicates) and return root."""
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    # if duplicate, just ignore
    return root


def kth_smallest(root, k):
    """Return the k-th smallest element (1-indexed). Raise IndexError if k too large."""
    stack = []
    curr = root
    count = 0

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right

    # if k > number of nodes
    raise IndexError("k exceeds number of nodes in tree")


def range_sum_bst(root, low, high):
    """Return the sum of all node values in [low, high]."""
    if root is None:
        return 0

    total = 0
    if root.val > low:
        total += range_sum_bst(root.left, low, high)
    if low <= root.val <= high:
        total += root.val
    if root.val < high:
        total += range_sum_bst(root.right, low, high)
    return total
