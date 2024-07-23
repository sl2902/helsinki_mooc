# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    if root is None:
        return 0
    max_val = root.value

    left_val = greatest_node(root.left_child)
    right_val = greatest_node(root.right_child)
    if left_val > right_val:
        max_val = left_val
    elif right_val > left_val:
        max_val = right_val
    return max_val

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))
    