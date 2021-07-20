currentpos = -1
SIZE_OF_ARR = 30
def insert_arr(arr, data):
    global currentpos
    size = len(arr)
    if size == SIZE_OF_ARR:
        print("FULL")
        return
    arr.insert(currentpos + 1, data)
    currentpos += 1

def delete_arr(arr):
    global currentpos
    size = len(arr)
    if currentpos == -1:
        print("EMPTY")
        return
    del arr[currentpos]
    if currentpos + 1 == size and size == 1:
        currentpos = -1
    elif currentpos + 1 == size and size != 1:
        currentpos = 0

def traverse_front(arr):
    global currentpos
    if (currentpos == -1):
        print("EMPTY")
        return
    size = len(arr)
    if currentpos + 1 >= size:
        print("ERROR")
    else:
        currentpos += 1

def traverse_rear(arr):
    global currentpos
    if currentpos == -1:
        print("EMPTY")
        return
    if currentpos - 1 < 0:
        print("ERROR")
    else:
        currentpos -= 1

def goto_first():
    global currentpos
    currentpos = 0

def goto_last(arr):
    global currentpos
    currentpos = len(arr) - 1

def get_data(arr):
    print("%c returned" %arr[currentpos])
    return arr[currentpos]

def replace(arr, data):
    arr[currentpos] = data

def move(arr, newpos):
    global currentpos
    size = len(arr)
    if (currentpos == newpos or newpos >= size or newpos < 0):
        return
    if currentpos > newpos:
        for i in range(currentpos, newpos, -1):
            arr[i], arr[i-1] = arr[i-1], arr[i]
    else:
        for i in range(currentpos, newpos):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    currentpos = newpos

def print_array(arr):
    if currentpos == -1:
        print("EMPTY")
        return
    else:
        size = len(arr)
        for i in range(size):
            print("%c " %arr[i], end='')
        print()
        print("Current Position: %c" %arr[currentpos])


def makehalf(arr):
    size = len(arr)
    for i in range(int(size/2)):
        delete_arr(arr)

def deleteindex(arr, index):
    global currentpos
    temp = currentpos
    currentpos = index
    delete_arr(arr)
    if temp > index:
        currentpos = 0
    else:
        currentpos = temp

arr = []

print("+: insert data \n ex) +a +b")
print("<: go to first data")
print(">: go to last data")
print("-: delete data")
print("N: go to next data")
print("P: go to previous data")
print("@: return data")
print("=: replace data\n ex) =u")
print("R: reverse array")
print("H: make array half")
print("D: delete data by index\n ex) D1")
print("E: clear array")
print("M: move data\n ex) MP MN Mn M3")
print("L: print data")
print("Q: exit")

while True:
    command = input("COMMAND: ")
    if command[0] == 'Q':
        print("EXIT")
        break
    i = 0
    while i < len(command):
        if command[i] == '+':
            insert_arr(arr, command[i+1])
            i+=1
        elif command[i] == '<':
            goto_first()
        elif command[i] == '>':
            goto_last(arr)
        elif command[i] == '-':
            delete_arr(arr)
        elif command[i] == 'N':
            traverse_front(arr)
        elif command[i] == 'P':
            traverse_rear(arr)
        elif command[i] == '@':
            get_data(arr)
        elif command[i] == 'R':
            arr.reverse()
        elif command[i] == 'H':
            makehalf(arr)
        elif command[i] == 'D':
            deleteindex(arr, int(command[i+1]))
            i+=1
        elif command[i] == '=':
            replace(arr, command[i+1])
            i+=1
        elif command[i] == 'E':
            arr.clear()
            currentpos = -1
        elif command[i] == 'M':
            if command[i+1] == 'P':
                move(arr, currentpos - 1)
                i+=1
            elif command[i+1] == 'N':
                move(arr, currentpos + 1)
                i+=1
            elif command[i+1] == 'n':
                move(arr, len(arr) - 1)
                i+=1
            else:
                move(arr, int(command[i+1]))
                i+=1
        elif command[i] == 'L':
            print_array(arr)
        i += 1