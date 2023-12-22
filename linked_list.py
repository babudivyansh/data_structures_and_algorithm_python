"""
@Author: Divyansh Babu

@Date: 2023-12-22 10:33

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-22 10:33

@Title : Linked list curd operation.
"""


class Node:
    def __init__(self, data=None, next_re=None):
        self.data = data
        self.next = next_re


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        """
        Description: This function printing all the element of the linked list
        Parameter: self object as parameter.
        Return:None
        """
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        """
        Description: This function return the length of the linked list.
        Parameter: self object as parameter.
        Return: length of linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        """
        Description: This function add the node at the begining of the linked list.
        Parameter: data, self object as parameter.
        Return:None
        """
        node = Node(data, self.head)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        """
        Description: This function add the node at the end of the linked list.
        Parameter: data, self object as parameter.
        Return:None
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        """
        Description: This function add the node at given position of the linked list.
        Parameter: index number, data, self object as parameter.
        Return:None
        """
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        """
        Description: This function remove the node from the linked list at given position.
        Parameter: index number, self object as parameter.
        Return:None
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        """
        Description: This function add multiple node at the linked list.
        Parameter: data_list,self object as parameter.
        Return:None
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(1, "blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45, 7, 12, 567, 99])
    ll.insert_at_end(67)
    ll.print()
    ll.insert_at_begining("data")
    ll.print()
