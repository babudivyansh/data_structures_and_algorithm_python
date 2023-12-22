"""
@Author: Divyansh Babu

@Date: 2023-12-22 15:20

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-22 15:20

@Title : doubly Linked list curd operation.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def prepend(self, data):
        new_node = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        self.__size += 1

    def append(self, data):
        new_node = Node(data)
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        self.__size += 1

    def list_size(self):
        return self.__size

    def traverse_fw(self):
        if self.__head is None:
            print("list is empty")
            return
        else:
            current_node = self.__head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def traverse_bw(self):
        if self.__tail is None:
            print("list is empty")
            return
        else:
            current_node = self.__tail
            while current_node:
                print(current_node.data)
                current_node = current_node.prev


if __name__ == '__main__':
    obj = Doubly()
    # l.append(1)
    # l.append(2)
    # l.append(3)
    # l.append(4)
    # print(l.list_size())
    obj.traverse_fw()
    obj.traverse_bw()
