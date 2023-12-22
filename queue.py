"""
@Author: Divyansh Babu

@Date: 2023-12-22 12:03

@Last Modified by: Divyansh Babu

@Last Modified time: 2023-12-22 12:03

@Title : Queue implementation using linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, data):
        """
        Description: This function for appending the node in to queue.
        Parameter: data,self object as parameter.
        Return:None
        """
        if self.rear is None:
            self.rear = self.front = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next

    def dequeue(self):
        """
        Description: This function for delete the first coming node in the queue.
        Parameter: self object as parameter.
        Return:None
        """
        if self.front is None:
            return "queue is empty"
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return

    def is_empty(self):
        """
        Description: This function for checking is the queue is empty.
        Parameter: self object as parameter.
        Return: bool value
        """
        return self.front is None

    def size(self):
        """
        Description: This function for display length of queue.
        Parameter: self object as parameter.
        Return: length of queue
        """
        count = 0
        itr = self.front
        while itr:
            count += 1
            itr = itr.next
        return count

    def front_node(self):
        """
        Description: This function for display front end data.
        Parameter: self object as parameter.
        Return: front end data
        """
        return self.front.data

    def rear_node(self):
        """
        Description: This function for display rear end data.
        Parameter: self object as parameter.
        Return: rear end data
        """
        return self.rear.data


if __name__ == '__main__':
    q = Queue()
    q.enqueue(55)
    q.enqueue(2200)
    q.enqueue(121)
    q.enqueue(552)

    print(q.is_empty())
    print(q.rear_node())
    print(q.front_node())
    print(q.size())
    print(q.dequeue())
