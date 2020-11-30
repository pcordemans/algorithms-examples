from sllist import SingleLinkedList

class Stack:
    def __init__(self):
        self.__list = SingleLinkedList()

    def top(self):
        return self.__list.head()

    def push(self, element):
        self.__list.prepend(element)

    def pop(self):
        element = self.top()
        self.__list = self.__list.tail()
        return element

    def isEmpty(self):
        return self.__list.isEmpty()