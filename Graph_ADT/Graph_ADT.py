class Vertex:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.e_head = None
        self.visited = False


class Edge:
    def __init__(self, weight):
        self.weight = weight
        self.linked_vertex = None
        self.next = None


class Graph:
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_vertex(self, item):
        v = Vertex(item)
        v.next = self.head
        self.head = v
        self.count += 1

    def insert_edge(self, v1, v2 ,weight):
        e1 = Edge(weight)
        e2 = Edge(weight)

        e1.linked_vertex = v1
        e1.next = v2.e_head
        v2.e_head = e1

        e2.linked_vertex = v2
        e2.next = v1.e_head
        v1.e_head = e2

    def print_graph(self):
        vcur = self.head
        while vcur is not None:
            print(vcur.data, end = '')
            if vcur.e_head is not None:
                ecur = vcur.e_head
                print("(", end = '')
                while ecur is not None:
                    print(ecur.linked_vertex.data, ecur.weight, end = '')
                    ecur = ecur.next
                    if ecur is not None:
                        print(",", end = '')
                print(")", end = '')
            vcur = vcur.next
            print(" ", end = '')


    def delete_edge(self, v1, v2):
        ecur = v1.e_head
        tmp = None
        while ecur is not None:
            if ecur.linked_vertex is v2:
                if ecur is v1.e_head:
                    v1.e_head = v1.e_head.next
                    break
                else:
                    tmp.next = ecur.next
                    break
            else:
                tmp = ecur
                ecur = ecur.next

        ecur = v2.e_head
        while ecur is not None:
            if ecur.linked_vertex is v1:
                if ecur is v2.e_head:
                    v2.e_head = v2.e_head.next
                    break
                else:
                    tmp.next = ecur.next
                    break

            else:
                tmp = ecur
                ecur = ecur.next

    def delete_vertex(self, item):
        vcur = self.head
        tmp = None
        while vcur is not None and vcur.data != item:
            tmp = vcur
            vcur = vcur.next
        if vcur is None:
            print("NO DATA")
            return

        ecur = vcur.e_head

        while ecur is not None:
            ncur = ecur.next
            self.delete_edge(ecur.linked_vertex, vcur)
            ecur = ncur

        if vcur is self.head:
            self.head = self.head.next

        else:
            tmp.next = vcur.next

        self.count -= 1

    def degree_of_v(self, v):
        degree = 0
        ecur = v.e_head
        while ecur is not None:
            ecur = ecur.next
            degree += 1
        return degree

    def is_conncted(self):
        vcur = self.head
        while vcur is not None:
            vc2 = vcur.next
            while vc2 is not None:
                self.reset_visited()
                if not self.path_exist(vcur, vc2):
                    return False
                vc2 = vc2.next
            vcur = vcur.next
        return True

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def adjacent(self, v):
        if v.e_head is None:
            print("NO ADJACENT VERTEX")
            return
        ecur = v.e_head
        while ecur is not None:
            print(ecur.linked_vertex.data ,end = ' ')
            ecur = ecur.next
        print()

    def path_exist(self, v1, v2):
        if v1 is v2:
            return True
        if v1.visited is True:
            return False
        ecur = v1.e_head
        v1.visited = True
        while ecur is not None:
            if self.path_exist(ecur.linked_vertex, v2):
                return True
            ecur = ecur.next
        return False

    def num_of_e(self):
        num = 0
        if self.head is None:
            return 0
        vcur = self.head
        while vcur is not None:
            ecur = vcur.e_head
            while ecur is not None:
                num += 1
                ecur = ecur.next
            vcur = vcur.next
        return int(num / 2)

    def rename_v(self, v, item):
        if v is None:
            return
        v.data = item

    def clear(self):
        vcur = self.head
        temp = None
        while vcur is not None:
            temp = vcur
            vcur = vcur.next
            self.delete_vertex(temp.data)

    def search_v(self, item):
        vcur = self.head
        while vcur is not None:
            if vcur.data == item:
                return vcur
            else:
                vcur = vcur.next

        return None

    def reset_visited(self):
        vcur = self.head
        while vcur is not None:
            vcur.visited = 0
            vcur = vcur.next

g = Graph()

print("+: insert vertex\n ex) +A +B")
print("E: insert edge\n ex) E(AB)")
print("-: delete vertex\n ex) -A -B")
print("D: delete edge\n ex) D(BC)")
print("L: print graph")
print("C: is connected?")
print("N: is empty?")
print("V: print degree of vertex\n ex) V(A)")
print("A: print adjacent vertex\n ex) A(B)")
print("P: path exist?\n ex) P(BC)")
print("X: count vertex")
print("H: count edge")
print("R: rename vertex\n ex) R(AF)")
print("K: clear")
print("Q: quit")

while True:
    command = input("COMMAND: ")
    if command[0] == 'Q':
        break
    i = 0
    while i < len(command):
        if command[i] == '+':
            g.insert_vertex(command[i+1])
            i += 1
        
        elif command[i] == 'E':
            v1_e = g.search_v(command[i+2])
            v2_e = g.search_v(command[i+3])
            if v1_e is None or v2_e is None:
                print("NO DATA")
            else:
                weight = int(input("WEIGHT: "))
                g.insert_edge(v1_e, v2_e, weight)
            i += 4
        
        elif command[i] == '-':
            g.delete_vertex(command[i+1])
            i += 1
        
        elif command[i] == 'D':
            v1_d = g.search_v(command[i+2])
            v2_d = g.search_v(command[i+3])
            if v1_d is None or v2_d is None:
                print("NO DATA")
            else:
                tf = False
                ecur = v1_d.e_head
                while ecur is not None:
                    if ecur.linked_vertex is v2_d:
                        tf = True
                        break
                    ecur = ecur.next
                if not tf:
                    print("NOT CONNECTED")
                else:
                    g.delete_edge(v1_d, v2_d)
            i += 4

        elif command[i] == 'L':
            g.print_graph()
            print()            

        elif command[i] == 'C':
            print(g.is_conncted())
        
        elif command[i] == 'N':
            print(g.is_empty())
        
        elif command[i] == 'V':
            v_d = g.search_v(command[i+2])
            if v_d is None:
                print("NO DATA")
            else:
                print(g.degree_of_v(v_d))
            i += 3
        
        elif command[i] == 'A':
            v_a = g.search_v(command[i+2])
            if v_a is None:
                print("NO DATA")
            else:
                g.adjacent(v_a)
            i += 3
        
        elif command[i] == 'P':
            v1 = g.search_v(command[i+2])
            v2 = g.search_v(command[i+3])
            if v1 is None or v2 is None:
                print("NO DATA")
            else:
                print(g.path_exist(v1, v2))
            i += 4
            g.reset_visited()

        elif command[i] == 'X':
            print(g.count)

        elif command[i] == 'H':
            print(g.num_of_e())
        
        elif command[i] == 'R':
            v = g.search_v(command[i+2])
            if v is None:
                print("NO DATA")
            else:
                g.rename_v(v, command[i+3])
            i += 4
        
        elif command[i] == 'K':
            g.clear()
        
        i += 1