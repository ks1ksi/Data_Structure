class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        newnode = Node(item)
        if self.is_empty():
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("EMPTY")
            return
        item = self.front.data
        self.front = self.front.next
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("EMPTY")
            return
        return self.front.data

    def print_queue(self):
        if self.is_empty():
            print("EMPTY")
            return
        temp = Queue()
        while not self.is_empty():
            print(self.peek(), end = ' ')
            temp.enqueue(self.dequeue())
        while not temp.is_empty():
            self.enqueue(temp.dequeue())
        print()

    def replace(self, item):
        if self.is_empty():
            print("EMPTY")
            return
        self.rear.data = item

    def is_member(self, item):
        tf = False
        temp = Queue()
        while not self.is_empty():
            if self.peek() == item:
                tf = True
            temp.enqueue(self.dequeue())
        while not temp.is_empty():
            self.enqueue(temp.dequeue())
        return tf

    def clear_queue(self):
        self.front = None
        self.rear = None
        self.count = 0


lq = Queue()
print("+: enqueue data\n ex) +a +b")
print("-: dequeue data")
print("P: peek data")
print("L: print data")
print("#: count data")
print("E: is empty?")
print("=: replace data\n ex) =u")
print("?: is member?\n ex) ?m")
print("C: clear queue")
print("Q: quit")
while True:
    command = input("COMMAND: ")
    if command[0] == 'Q':
        break
    i = 0
    while i < len(command):
        if command[i] == '+':
            lq.enqueue(command[i+1])
            i += 1
        elif command[i] == '-':
            lq.dequeue()
        elif command[i] == 'P':
            print("%c Returned" % lq.peek())
        elif command[i] == '#':
            print("LEN: %d" % lq.count)
        elif command[i] == 'E':
            if lq.is_empty():
                print("TRUE")
            else:
                print("FALSE")
        elif command[i] == '=':
            lq.replace(command[i+1])
            i += 1
        elif command[i] == '?':
            if lq.is_empty():
                print("EMPTY")
            elif lq.is_member(command[i+1]):
                print("TRUE")
            else:
                print("FALSE")
            i += 1
        elif command[i] == 'C':
            lq.clear_queue()
        elif command[i] == 'L':
            lq.print_queue()

        i += 1