from exceptions import EmptyQueueException


class Queue:
    # This is the Queue Data Structure

    # TODO: Add Search Method

    # Storing the contents of the queue in a list
    __items = []

    def __init__(self):
        self.__items =[]

    def put(self, *items):
        # This function puts an element at the end of the queue
        # Parameters: items: Send any number of items and they will be put in the queue in any order they are sent
        # For Example: queue.put(15,35,65,15,45)

        for item in items:
            self.__items.append(item)

    def get(self):
        # Returns the element at the front of the queue and removes it from the queue
        # Raises EmptyQueueException if the Queue is empty

        if len(self.__items) > 0:
            item = self.__items[0]
            self.__items.remove(item)
            return item
        raise EmptyQueueException("Queue is Empty")

    def peek(self):
        # Returns the first element of the queue
        # Raises EmptyQueueException if the Queue is empty


        if len(self.__items) > 0:
            item = self.__items[0]
            return item
        raise EmptyQueueException("Queue is Empty")

    def is_empty(self):
        # Returns True if the queue is empty otherwise False

        return len(self.__items) == 0

    def clear(self):
        # Clears the queue if its not empty

        if not self.is_empty():
            self.__items.clear()

    def remove(self, item):
        # Removes the item from the stack

        self.__items.remove(item)

    def reverse(self):
        # Returns a new instance of the Queue with its contents reversed

        reversed_queue = Queue()
        reversed_queue.put(*self.__items[::-1])
        return reversed_queue

    def __str__(self):

        print_string = "Queue("
        for item in self.__items:
            print_string += str(item) +", "
        print_string += ")"
        return  print_string
