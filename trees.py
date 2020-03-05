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


if __name__ == '__main__':
    my_array = [1, 2, 3, 4, 5, 6, 7]
    my_first_tree = bst_from_sorted_array(my_array)
    pre_order(my_first_tree)
