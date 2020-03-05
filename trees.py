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
