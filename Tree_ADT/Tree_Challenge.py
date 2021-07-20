import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # child
        self.right = None  # sibling


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert_child(self, parent, item):
        node = Node(item)

        if parent.left is None:
            parent.left = node

        else:
            cur = parent.left
            while cur.right is not None:
                cur = cur.right
            cur.right = node

        self.count += 1

    def print_tree(self, node1, node2):
        cur = node2.left
        if node1 is node2:
            print(node1.data, end='')

        if node1.left is None:
            print()
            return
        print("(", end='')

        while cur is not None:
            print(cur.data, end='')
            if cur.left is not None:
                self.print_tree(node1, cur)
            if cur.right is not None:
                print(",", end='')
            cur = cur.right

        print(")", end='')
        if node1 is node2:
            print()

    def search_node(self, node, item):
        if node is None:
            return
        if node.data == item:
            return node

        cur = self.search_node(node.left, item)
        if cur is not None:
            return cur
        cur = self.search_node(node.right, item)
        if cur is not None:
            return cur

        return None

    def get_parent_bt(self, root, node):
        if root is None:
            return None
        if root.left is node or root.right is node:
            return root
        cur = self.get_parent_bt(root.left, node)
        if cur is not None:
            return cur
        cur = self.get_parent_bt(root.right, node)
        if cur is not None:
            return cur
        return None

    def is_leftchild(self, parent, node):
        if parent.left is node:
            return True
        else:
            return False

    def is_rightchild(self, parent, node):
        if parent.right is node:
            return True
        else:
            return False

    def get_parent(self, root, node):
        if self.get_parent_bt(root, node) is None:
            return None

        cur = node
        while not self.is_leftchild(self.get_parent_bt(root, cur), cur):
            cur = self.get_parent_bt(root, cur)
        return self.get_parent_bt(root, cur)

    def total_cost(self, node):
        total = 0
        if self.root is node:
            total += self.root.data
            return total
        cur = node
        while cur is not self.root:
            total += cur.data
            cur = self.get_parent(self.root, cur)
        total += cur.data
        return total

queue = []
tree = Tree()
root = Node(int(input("ROOT 노드 값 입력: ")))
tree.root = root
queue.append(root.data)
while len(queue) > 0:
    node = tree.search_node(tree.root, queue[0])
    while True:
        cost = int(input("{}의 자식 노드 값 입력(음수 입력시 종료): ".format(node.data)))
        if cost < 0:
            break
        tree.insert_child(node, cost)
        queue.append(cost)
    queue.pop(0)

print("입력한 트리 ↓")
tree.print_tree(tree.root, tree.root)
while True:
    cdata = int(input("TOTAL COST 계산할 노드: "))
    pathnode = tree.search_node(tree.root, cdata)
    if pathnode is None:
        print("입력 오류")
    else:
        break
print("TOTAL COST: {}".format(tree.total_cost(pathnode)))