from exceptions import EmptyStackException


class Stack:
    # This is the Stack Data Structure

    # TODO: Add Search Method


    # Storing the contents of the stack in a list
    __items = []

    def __init__(self):
        self.__items=[]

    def push(self, *items):

        # Parameters: send any number of items and they will be pushed to the stack in the order they were sent
        # For example: stack.push(15,25,35,0)

        for item in items:
            self.__items.append(item)

    def pop(self):

        # Returns the popped value of the stack
        # Raises EmptyStackException if the stack is empty.

        if len(self.__items) > 0:
            item = self.__items[-1]
            self.__items.remove(self.__items[-1])
            return item

        raise EmptyStackException("Stack is Empty. No Elements to Pop")

    def peek(self):

        # Returns the top element of the stack without popping it.
        # Raises EmptyStackException if the stack is empty.

        if len(self.__items) == 0:
            raise EmptyStackException("Stack is Empty. No Elements to Peek")
        return self.__items[-1]

    def is_empty(self):

        # Returns: True: if the stack is empty
        #          False if the stack is not empty

        return len(self.__items) == 0

    def clear(self):

        # Clears the stack
        if not self.is_empty():
            self.__items.clear()

    def remove(self, item):
        # Removes the item from the stack

        self.__items.remove(item)

    def reverse(self):
        # Returns a new instance of the Stack with its contents reversed

        reversed_stack = Stack()
        reversed_stack.push(*self.__items[::-1])
        return reversed_stack

    def __str__(self):

        print_string = "Stack("
        for item in self.__items:
            print_string += str(item) +", "
        print_string += ")"
        return  print_string
