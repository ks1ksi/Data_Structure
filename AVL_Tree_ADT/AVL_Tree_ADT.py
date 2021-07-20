class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def node_status(self):
        if self.left is None and self.right is None:
            return 0
        elif self.right is None:
            return 1
        elif self.left is None:
            return 2
        else:
            return 3


class AVL:
    def __init__(self, root):
        self.root = root

    def insert_node(self, item):
        if self.root is None:
            self.root.data = item
        else:
            newnode = Node(item)
            cur = self.root
            parent = None
            while cur is not None:
                if cur.data > item:
                    parent = cur
                    cur = cur.left
                elif cur.data < item:
                    parent = cur
                    cur = cur.right
                else:
                    print("SAME DATA")
                    return
            if parent.data > item:
                parent.left = newnode
            else:
                parent.right = newnode

    def search_node(self, item):
        cur = self.root
        while cur is not None:
            if cur.data == item:
                return cur
            elif cur.data > item:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def search_parent_node(self, item):
        cur = self.root
        parent = None
        while cur is not None:
            if cur.data == item:
                return parent
            elif cur.data > item:
                parent = cur
                cur = cur.left
            else:
                parent = cur
                cur = cur.right
        return None

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def RRL(self, node):
        if node is not None:
            self.RRL(node.right)
            print(node.data, end=' ')
            self.RRL(node.left)

    def print_tree(self, node):
        if node is None:
            return
        if node.right is None and node.left is None:
            return
        print("(", end='')
        if node.left is not None:
            print(node.left.data, end='')
        self.print_tree(node.left)
        print(",", end='')
        if node.right is not None:
            print(node.right.data, end='')
        self.print_tree(node.right)
        print(")", end='')

    def get_min(self):
        if self.root is None:
            return
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur

    def get_max(self):
        if self.root is None:
            return
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur

    def count_node(self, node):
        if node is None:
            return 0
        return 1 + self.count_node(node.left) + self.count_node(node.right)

    def height(self, node):
        if node is None:
            return 0
        l = self.height(node.left)
        r = self.height(node.right)
        if l > r:
            return l + 1
        else:
            return r + 1

    def delete_node(self, item):
        cur = self.search_node(item)
        if cur is None:
            print("NO DATA")
            return
        parent = self.search_parent_node(item)
        successor = None
        scparent = None
        if cur.node_status() == 0:
            if cur == self.root:
                self.root = None
                return
            elif parent.left == cur:
                parent.left = None

            else:
                parent.right = None

        elif cur.node_status() == 1:
            if cur == self.root:
                self.root = self.root.left
                return
            successor = cur.left
            if parent.left == cur:
                parent.left = successor
            else:
                parent.right = successor

        elif cur.node_status() == 2:
            if cur == self.root:
                self.root = self.root.right
                return
            successor = cur.right
            if parent.left == cur:
                parent.left = successor
            else:
                parent.right = successor

        else:  # left and right
            successor = cur.right
            while successor.left is not None:
                scparent = successor
                successor = successor.left
            if successor.right is None:
                if scparent is None:
                    cur.data = successor.data
                    cur.right = None
                else:
                    cur.data = successor.data
                    scparent.left = None
            else:
                if scparent is None:
                    cur.data = successor.data
                    cur.right = successor.right
                else:
                    cur.data = successor.data
                    scparent.left = successor.right

    def balancing_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def LLrotate(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        return a

    def RRrotate(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        return a

    def LRrotate(self, node):
        node.left = self.RRrotate(node.left)
        return self.LLrotate(node)

    def RLrotate(self, node):
        node.right = self.LLrotate(node.right)
        return self.RRrotate(node)

    def rebalance(self):
        if self.balancing_factor(self.root) >= 2:
            if self.balancing_factor(self.root.left) >= 1:
                self.root = self.LLrotate(self.root)
            else:
                self.root = self.LRrotate(self.root)
        elif self.balancing_factor(self.root) <= -2:
            if self.balancing_factor(self.root) <= -1:
                self.root = self.RRrotate(self.root)
            else:
                self.root = self.RLrotate(self.root)





def string_to_int(arr, i):
    x = 0
    while '0' <= arr[i] <= '9':
        x *= 10
        x += int(arr[i])
        i += 1
    return x


avl = AVL(None)

print("+: insert node\n ex) +23")
print("-: delete node\n ex) -36")
print("P: print tree")
print("I: inorder traversal")
print("R: right->root->left traversal")
print("B: print balancing factor\n ex) B22")
print("M: get max")
print("m: get min")
print("F: find node\n ex) F23")
print("H: get tree's height")
print("#: count node")
print("r: get right child\n ex) r30")
print("l: get left child\n ex) l20")
print("C: clear tree")
print("Q: quit")

while True:
    command = input("COMMAND: ")
    command += ' '
    if command[0] == 'Q':
        break
    i = 0
    while i < len(command):
        if command[i] == '+':
            i += 1
            if avl.root is None:
                newnode = Node(string_to_int(command, i))
                avl.root = newnode
            else:
                avl.insert_node(string_to_int(command, i))
                avl.rebalance()
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == '-':
            if avl.root is None:
                print("NO DATA")
            else:
                i += 1
                avl.delete_node(string_to_int(command, i))
                avl.rebalance()
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == 'P':
            if avl.root is None:
                print("NO DATA")
            else:
                print(avl.root.data, end='')
                avl.print_tree(avl.root)
                print()

        elif command[i] == 'I':
            if avl.root is None:
                print("NO DATA")
            else:
                avl.inorder(avl.root)
                print()

        elif command[i] == 'R':
            if avl.root is None:
                print("NO DATA")
            else:
                avl.RRL(avl.root)
                print()

        elif command[i] == 'B':
            i += 1
            node = avl.search_node(string_to_int(command, i))
            if node is None:
                print("NO DATA")
            else:
                print(avl.balancing_factor(node))
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == 'M':
            if avl.root is None:
                print("NO DATA")
            else:
                node = avl.get_max()
                print(node.data)

        elif command[i] == 'm':
            if avl.root is None:
                print("NO DATA")
            else:
                node = avl.get_min()
                print(node.data)

        elif command[i] == 'F':
            i += 1
            node = avl.search_node(string_to_int(command, i))
            if node is None:
                print("NO DATA")
            else:
                print("ROOT", end=' ')
                cur = avl.root
                while cur.data != node.data:
                    if cur.data > node.data:
                        cur = cur.left
                        print("LEFT", end=' ')
                    elif cur.data < node.data:
                        cur = cur.right
                        print("RIGHT", end=' ')
                print()
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == 'H':
            if avl.root is None:
                print("NO DATA")
            else:
                print(avl.height(avl.root))

        elif command[i] == '#':
            if avl.root is None:
                print("NO DATA")
            else:
                print(avl.count_node(avl.root))

        elif command[i] == 'r':
            i += 1
            node = avl.search_node(string_to_int(command, i))
            if node is None:
                print("NO DATA")
            elif node.right is None:
                print("NO RIGHT CHILD")
            else:
                print(node.right.data)
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == 'l':
            i += 1
            node = avl.search_node(string_to_int(command, i))
            if node is None:
                print("NO DATA")
            elif node.left is None:
                print("NO LEFT CHILD")
            else:
                print(node.left.data)
            while '0' <= command[i] <= '9':
                i += 1
            i -= 1

        elif command[i] == 'C':
            avl.root = None

        i += 1
