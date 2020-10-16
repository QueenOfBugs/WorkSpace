# stack
# Last In First Out


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('HiThere')

    def peek(self):
        top_index = len(self.items) - 1
        return self.items[top_index]

    def size(self):
        return len(self.items)


# queue
# First In First Out

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())
    # stack.pop()
    for i in range(0, 6):
        stack.push(i)
    print(stack.peek())
    print(stack.size())
    stack = Stack()
    for i in "hello":
        stack.push(i)

    st = ""

    for i in range(0, stack.size()):
        st += stack.pop()

    print(st)

    queue = Queue()

    for i in "hell0":
        queue.enqueue(i)
    for i in range(0, queue.size()):
        print(queue.dequeue())
    print(queue.size())

    # challenge

    stack = Stack()
    for i in "yesterday":
        stack.push(i)

    reverse = ""

    for i in range(0, len(stack.items)):
        reverse += stack.pop()

    print(reverse)

    list1 = [1, 2, 3, 4, 5]
    list2 = []
    stack = Stack()
    for i in list1:
        stack.push(i)
    for i in range(len(stack.items)):
        list2.append(stack.pop())
    print(list1, list2)
