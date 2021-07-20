class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        if self.head is None:
            return  True
        else:
            return False

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.count += 1

    def pop(self):
        if self.is_empty():
            return -1
        else:
            item = self.head.data
            self.head = self.head.next
            self.count -= 1
            return item

    def peek(self):
        if self.is_empty():
            return -1
        else:
            return self.head.data

    def print_stack(self):
        if self.is_empty():
            print("EMPTY")
            return
        temp = Stack()
        while self.is_empty() is False:
            temp.push(self.pop())
        while temp.is_empty() is False:
            print(temp.head.data, end = ' ')
            self.push(temp.pop())
        print()

    def replace(self, item):
        if self.is_empty():
            return -1
        else:
            self.head.data = item

    def clear_stack(self):
        if self.is_empty():
            return -1
        else:
            while self.is_empty() is False:
                self.pop()

    def is_member(self, item):
        temp = Stack()
        tf = False
        while self.is_empty() is False:
            if self.peek() == item:
                tf = True
                break
            else:
                temp.push(self.pop())
        while temp.is_empty() is False:
            self.push(temp.pop())
        return tf

    def topofstack(self):
        if self.is_empty():
            print("EMPTY")
            return
        print(self.count, self.head.data)

    def howmanypops(self, item):
        if self.is_empty():
            return -1
        temp = Stack()
        tf = False
        while self.is_empty() is False:
            if self.peek() == item:
                tf = True
                num = temp.count + 1
                break
            else:
                temp.push(self.pop())
        while temp.is_empty() is False:
            self.push(temp.pop())
        if tf is True:
            return num
        else:
            return -2

    def minimize(self, num):
        if num > self.count:
            print("WRONG NUM")
            return
        elif self.is_empty():
            print("EMPTY")
            return
        while self.count > num:
            self.pop()

    def replace_by_index(self, item, idx):
        if self.count < idx:
            print("WRONG NUM")
            return
        elif self.is_empty():
            print("EMPTY")
            return
        temp = Stack()
        while self.count > idx:
            temp.push(self.pop())
        self.replace(item)
        while temp.is_empty() is False:
            self.push(temp.pop())


stack = Stack()
print("+: push data to stack\n ex) +a +b")
print("-: pop data from stack")
print("=: replace data of top of stack\n ex) =u")
print("T: print top of stack")
print("E: is empty?")
print("?: is member?\n ex) ?k")
print("#: count data")
print("P: peek data")
print("num: pop data 'num' times")
print("L: print stack")
print("H: how many pops to get data?\n ex) Ha Hb")
print("M: minimize stack\n ex) M2 M3")
print("R: replace data by index\n ex) R3a R4b")
print("C: clear stack")
print("Q: quit")
while True:
    command = input("COMMAND: ")
    if command[0] == 'Q':
        break
    command += ' '
    i = 0
    while i < len(command):
        if command[i] == '+':
            stack.push(command[i+1])
            i += 1
        elif command[i] == '-':
            stack.pop()
        elif command[i] == '=':
            stack.replace(command[i+1])
            i += 1
        elif command[i] == 'T':
            stack.topofstack()
        elif command[i] == 'E':
            print(stack.is_empty())
        elif command[i] == '?':
            print(stack.is_member(command[i+1]))
            i += 1
        elif command[i] == '#':
            print(stack.count)
        elif command[i] == 'P':
            print(stack.peek())
        elif command[i] == 'L':
            stack.print_stack()
        elif command[i] == 'H':
            if stack.howmanypops(command[i+1]) == -1:
                print("EMPTY")
            elif stack.howmanypops(command[i+1]) == -2:
                print("NO DATA")
            else:
                print("YOU NEED %d TIMES OF POP" %stack.howmanypops(command[i+1]))
            i += 1
        elif command[i] == 'M':
            num = int(command[i+1])
            stack.minimize(num)
            i += 1
        elif command[i] == 'R':
            idx = int(command[i+1])
            stack.replace_by_index(command[i+2], idx)
            i += 2
        elif command[i] == 'C':
            stack.clear_stack()
        elif '0' <= command[i] <= '9':
            num = int(command[i])
            while num > 0:
                stack.pop()
                num -= 1
        i += 1