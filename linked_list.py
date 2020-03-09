class Node:

    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.start_node = None

    def traverse(self):
        if self.start_node is None:
            print('List has no elements')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, ' ')
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self, data):

        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def insert_after_item(self, x, data):

        n = self.start_node

        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print('The item after which to insert is not in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):

        if self.start_node is None:
            print('List has no item')
            return

        if self.start_node.item == x:
            new_node = Node(data)
            new_node.ref = self.start_node.ref
            self.start_node = new_node
            return

        n = self.start_node

        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n is None:
            print('The item before which to insert is not in the list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_from_start(self):

        if self.start_node is None:
            print('List is empty')
            return
        self.start_node = self.start_node.ref

    def delete_from_end(self):
        if self.start_node is None:
            print('List is empty')
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_item(self, x):
        if self.start_node == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node

        while n is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n is None:
            print('Item is not in the list')
            return
        else:
            n.ref = n.ref.ref

    def print_reverse(self, start_node):
        if start_node is None:
            return
        self.print_reverse(start_node.ref)
        print(start_node.item)

    def merge_list(self, my_list):

        node1 = self.start_node
        node2 = my_list.start_node
        result = LinkedList()

        while node1 is not None and node2 is not None:
            if node1.item >= node2.item:
                result.insert_at_end(node2.item)
                node2 = node2.ref

            if node1.item < node2.item:
                result.insert_at_end(node1.item)
                node1 = node1.ref

        while node1 is not None:
            result.insert_at_end(node1.item)
            node1 = node1.ref
        while node2 is not None:
            result.insert_at_end(node2.item)
            node2 = node2.ref

        return result

    def print_middle(self):

        if self.start_node is None:
            print('List has no elements')
            return

        n = self.start_node
        elem_number = 0

        while n is not None:
            elem_number += 1
            n = n.ref
        n = self.start_node

        for i in range(int(elem_number / 2)):
            n = n.ref

        middle_element = n.item

        print('The middle element is {}'.format(middle_element))

    def print_middle2(self):

        if self.start_node is None:
            print('List has no elements')
            return
        n = self.start_node
        q = self.start_node

        while n is not None:
            n = n.ref.ref
            q = q.ref
        middle_element = q.item
        print('The middle element through the second method is {}'.format(middle_element))

    def k_last_element(self, k):
        if self.start_node is None:
            print('List has no elements')
            return
        n = self.start_node
        for i in range(k):
            if n is None:
                print('List out of range')
                return
            n = n.ref

        q = self.start_node
        while n is not None:
            q = q.ref
            n = n.ref
        k_last = q.item
        print('The {0}-last element is {1}'.format(k, k_last))

    def is_palindrome(self):
        if self.start_node is None:
            return True
        n = self.start_node
        palindrome_helper = ''

        while n is not None:
            palindrome_helper += str(n.item)
            n = n.ref

        for i in range(len(palindrome_helper)):
            if palindrome_helper[i] is not palindrome_helper[len(palindrome_helper) - 1 - i]:
                return False

        return True

    def remove_duplicates(self):
        if self.start_node is None:
            print('List is empty')
            return
        n = self.start_node
        while n.ref is not None:
            if n.item == n.ref.item:
                self.delete_item(n.item)
            n = n.ref

        if self.start_node.item == self.start_node.ref.item:
            self.delete_item(self.start_node)
        return


if __name__ == '__main__':
    my_linked_list = LinkedList()

    my_linked_list.insert_at_end(5)
    my_linked_list.insert_at_end(10)
    my_linked_list.insert_at_end(15)
    my_linked_list.insert_before_item(15, 11)
    my_linked_list.insert_at_end(20)
    my_linked_list.insert_at_end(25)

    # my_linked_list.traverse()

    # my_linked_list.delete_from_start()
    # my_linked_list.delete_from_end()
    # my_linked_list.delete_item(10)
    # my_linked_list.traverse()
    # print('Here comes the inverted list:')
    # my_linked_list.print_reverse(my_linked_list.start_node)
    #
    # my_second_list = LinkedList()
    # my_second_list.insert_at_end(4)
    # my_second_list.insert_at_end(6)
    # my_second_list.insert_at_end(13)
    # my_second_list.insert_at_end(18)
    #
    # my_linked_list.merge_list(my_second_list).traverse()
    my_linked_list.traverse()
    my_linked_list.print_middle()
    my_linked_list.k_last_element(2)
    my_linked_list.print_middle2()

    aux_list = LinkedList()
    # aux_list.insert_at_end(1)
    aux_list.insert_at_end(2)
    aux_list.insert_at_end(2)
    aux_list.insert_at_end(2)
    aux_list.insert_at_end(2)
    aux_list.insert_at_end(2)
    # aux_list.insert_at_end(3)
    # aux_list.insert_at_end(4)
    # aux_list.insert_at_end(4)
    # aux_list.insert_at_end(5)
    # aux_list.insert_at_end(6)
    # aux_list.insert_at_end(8)
    # aux_list.insert_at_end(8)
    # aux_list.insert_at_end(8)

    print(aux_list.is_palindrome())
    aux_list.remove_duplicates()
    print('After removing the duplicates, we got:')
    aux_list.traverse()
