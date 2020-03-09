class TreeNode:
    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None


def bst_from_sorted_array(tree_array):
    if not tree_array:
        return
    middle = len(tree_array) // 2
    node = TreeNode(tree_array[middle])
    node.left = bst_from_sorted_array(tree_array[:middle])
    node.right = bst_from_sorted_array(tree_array[middle + 1:])
    return node


def pre_order(node):
    if node is None:
        return
    print(node.item, " ")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.item, " ")
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.item, " ")


def binary_search(root, key):
    if root is None:
        return False
    if root.item == key:
        return True
    if key < root.item:
        return binary_search(root.left, key)
    elif key > root.item:
        return binary_search(root.right, key)


def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


def get_level(node, level, data):
    if node is None:
        return 0
    if node.item == data:
        return level
    down_level = get_level(node.left, level + 1, data)
    if down_level:
        return down_level
    down_level = get_level(node.right, level + 1, data)
    return down_level


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5, 6, 7]
    my_first_tree = bst_from_sorted_array(my_array)
    print('Here comes the pre-order traversal')
    pre_order(my_first_tree)
    print('Here comes the in-order traversal')
    in_order(my_first_tree)
    print('Here comes the post-order traversal')
    post_order(my_first_tree)
    print("The root is:", my_first_tree.item)
    print('The element has been found? {}'.format(binary_search(my_first_tree, 5)))
    print('The height of our bst is {}.'.format(height(my_first_tree)))
    print(get_level(my_first_tree, 1, 4))
