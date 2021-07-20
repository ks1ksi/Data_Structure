class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class doubly_linked_list:
    def __init__(self):
        newnode = Node(None)
        self.head = newnode
        self.size = 0
        self.cur = self.head

    def is_empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def addtail(self, data):
        newnode = Node(data)
        while self.cur.right != None:
            self.cur = self.cur.right
        self.cur.right = newnode
        newnode.left = self.cur
        self.cur = newnode
        self.size += 1

    def add_node(self, data):
        if self.cur.right == None:
            self.addtail(data)
        else:
            newnode = Node(data)
            newnode.right = self.cur.right
            newnode.left = self.cur
            self.cur.right.left = newnode
            self.cur.right = newnode
            self.cur = newnode
            self.size += 1
    
    def traverse_rear(self):
        if self.is_empty() == 1 or self.cur.left == self.head:
            print("CANT TRAVERSE")
            return
        else:
            self.cur = self.cur.left
    
    def traverse_front(self):
        if self.is_empty() == 1 or self.cur.right == None:
            print("CANT TRAVERSE")
            return
        else:
            self.cur = self.cur.right

    def delete_node(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        if self.cur.right == None:
            self.cur = self.cur.left
            self.cur.right = None
        else:
            self.cur.left.right = self.cur.right
            self.cur.right.left = self.cur.left
            self.cur = self.cur.right
        self.size -= 1
    
    def goto_first(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        else:
            self.cur = self.head.right
    
    def goto_last(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        else:
            while self.cur.right != None:
                self.cur = self.cur.right
        
    def goto_index(self, index):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        elif self.size < index or index <= 0:
            print("WRONG INDEX")
            return
        else:
            self.cur = self.head
            for i in range(index):
                self.cur = self.cur.right

    def replace(self, item):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        self.cur.data = item
    
    def data_count(self):
        return self.size
    
    def is_member(self, item):
        if self.is_empty() == 1:
            return -2
        node = self.head
        for i in range(1, (self.size) + 1):
            node = node.right
            if node.data == item:
                return i
        return -1

    def clear_list(self):
        while self.is_empty() == 0:
            self.delete_node()
    
    def reverse_list(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        temp1 = self.head.right
        temp2 = self.cur
        while temp2.right != None:
            temp2 = temp2.right
        for i in range(int(self.size/ 2)):
            temp1.data, temp2.data = temp2.data, temp1.data
            temp1 = temp1.right
            temp2 = temp2.left

    def print_list(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        temp = self.head.right
        while temp != None:
            print(temp.data, end = ' ')
            temp = temp.right
        print("")
        print("Cur:", self.cur.data)
    
    def data_swap(self, index):
        if self.is_empty() == 1:
            print("EMPTY")
            return
        elif index > self.size or index <= 0:
            print("WRONG INDEX")
            return
        node = self.head
        for i in range(index):
            node = node.right
        if node == self.cur:
            print("SAME INDEX")
            return
        else:
            node.data, self.cur.data = self.cur.data, node.data

    def get_data(self):
        if self.is_empty() == 1:
            print("EMPTY")
            return -1
        return self.cur.data


list = doubly_linked_list()
print("+: insert data \n ex) +a +b")
print("<: go to first data")
print(">: go to last data")
print("-: delete data")
print("N: go to next data")
print("P: go to previous data")
print("G: return data")
print("=: replace data\n ex) =u")
print("R: reverse list")
print("C: clear list")
print("L: print list")
print("#: count data")
print("?: data in list? \n ex) ?a ?b")
print("S: swap data\n ex)S1 S2")
print("T: add data to tail\n ex) Ta Tb")
print("E: is the list empty?")
print("NUMBER: go to index")
print("Q: exit")
while True:
    command = input("COMMAND: ")
    command += ' '
    if command[0] == 'Q':
        break
    i = 0
    while i < len(command):
        if command[i] == '+':
            list.add_node(command[i+1])
            i += 1
        elif command[i] == '<':
            list.goto_first()
        elif command[i] == '>':
            list.goto_last()
        elif command[i] == '-':
            list.delete_node()
        elif command[i] == 'N':
            list.traverse_front()
        elif command[i] == 'P':
            list.traverse_rear()
        elif command[i] == 'G':
            if list.get_data() != -1:
                print(list.get_data(), "RETURNED")
        elif command[i] == '=':
            list.replace(command[i+1])
            i += 1
        elif command[i] == 'R':
            list.reverse_list()
        elif command[i] == 'C':
            list.clear_list()
        elif command[i] == 'L':
            list.print_list()
        elif command[i] == '#':
            if list.data_count() == 0:
                print("EMPTY")
            else:
                print("LENGTH:", list.data_count())    
        elif command[i] == '?':
            if list.is_member(command[i+1]) == -2:
                print("EMPTY")
            elif list.is_member(command[i+1]) == -1:
                print("NOT MEMBER")
            else:
                print("INDEX:", list.is_member(command[i+1]))
            i += 1
        elif command[i] == 'S':
            index = 0
            i += 1
            while '0' <= command[i] <= '9':
                index *= 10
                index += int(command[i])
                i +=1
            i -= 1
        elif command[i] == 'T':
            list.addtail(command[i+1])
            i +=1
        elif command[i] == 'E':
            if list.is_empty() == 1:
                print("TRUE")
            else:
                print("FALSE")
        elif '0' <= command[i] <= '9':
            index = 0
            while '0' <= command[i] <= '9':
                index *= 10
                index += int(command[i])
                i += 1
            list.goto_index(index)
        i += 1