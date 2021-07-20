import threading
import time
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

clientpos = -1
riderwayclient = None

client_num = 0

INFINITE = 9999999
# UI파일 연결
# UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야함.
form_start_app = uic.loadUiType("startscreen.ui")[0]
form_class_login = uic.loadUiType("login.ui")[0]
form_class_main = uic.loadUiType("mainpage.ui")[0]
form_menu_ui = uic.loadUiType("menu_search.ui")[0]
form_info = uic.loadUiType("my배민.ui")[0]
form_Myorder = uic.loadUiType("myorderscreen.ui")[0]
form_chungzik_menu = uic.loadUiType("chungzik_menu.ui")[0]
form_bhc_menu = uic.loadUiType("bhc_menu.ui")[0]
form_sinjeon_menu = uic.loadUiType("sinjeon_menu.ui")[0]
form_burgerking_menu = uic.loadUiType("burgerking_menu.ui")[0]
form_ddatti_menu = uic.loadUiType("datti_menu.ui")[0]
form_galli_menu = uic.loadUiType("galli_menu.ui")[0]
form_yooksudang_menu = uic.loadUiType("yooksudang_menu.ui")[0]
form_burgerpark_menu = uic.loadUiType("burgerpark_menu.ui")[0]
form_goobne_menu = uic.loadUiType("goobne_menu.ui")[0]
form_rider_app = uic.loadUiType("riderway_screen.ui")[0]
form_hongkongbanjeom_menu = uic.loadUiType("hongkongbanjeom.ui")[0]
form_phongon_menu = uic.loadUiType("pho.ui")[0]
form_jukstory_menu = uic.loadUiType("juk.ui")[0]
form_complete = uic.loadUiType("completelist.ui")[0]


class Menu:
    def __init__(self, name, price, delay):
        self.name = name
        self.price = price
        self.delay = delay


class Client:
    def __init__(self, order, position):
        self.order = order
        self.position = position
        self.rider = None
        self.now = 0
        self.delay = 0
        self.key = client_num


class Clients:
    def __init__(self, restaurants):
        self.client1 = None
        self.client2 = None
        self.client3 = None
        self.client4 = None
        self.client5 = None

        self.cookthread1 = None
        self.cookthread2 = None
        self.cookthread3 = None
        self.cookthread4 = None
        self.cookthread5 = None

        self.riderthread1 = None
        self.riderthread2 = None
        self.riderthread3 = None
        self.riderthread4 = None
        self.riderthread5 = None

        self.timer1 = None
        self.timer2 = None
        self.timer3 = None
        self.timer4 = None
        self.timer5 = None

        self.restaurants = restaurants

    def timer(self, client, complete):
        client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)
        i = 0

        while True:
            if client_res.remain(client) > 0:
                print(client_res.name, client.key, int(client_res.remain(client)))
                time.sleep(1)
            else:
                client.delay = client.rider.restaurant
                complete.insert_first(client)
                cur = complete.head
                while cur is not None:
                    print(cur.data.order.menu_arr[0].name)
                    cur = cur.next
                if client.key == self.client1.key:
                    print("client1 delete")
                    self.client1 = self.client2
                    self.client2 = self.client3
                    self.client3 = self.client4
                    self.client4 = self.client5
                    self.client5 = None

                    self.cookthread1 = self.cookthread2
                    self.cookthread2 = self.cookthread3
                    self.cookthread3 = self.cookthread4
                    self.cookthread4 = self.cookthread5
                    self.cookthread5 = None

                    self.riderthread1 = self.riderthread2
                    self.riderthread2 = self.riderthread3
                    self.riderthread3 = self.riderthread4
                    self.riderthread4 = self.riderthread5
                    self.riderthread5 = None

                    self.timer1 = self.timer2
                    self.timer2 = self.timer3
                    self.timer3 = self.timer4
                    self.timer4 = self.timer5
                    self.timer5 = None

                    mywindow_myorder.remove_tab(1)
                elif client.key == self.client2.key:
                    print("client2 delete")

                    self.client2 = self.client3
                    self.client3 = self.client4
                    self.client4 = self.client5
                    self.client5 = None

                    self.cookthread2 = self.cookthread3
                    self.cookthread3 = self.cookthread4
                    self.cookthread4 = self.cookthread5
                    self.cookthread5 = None

                    self.riderthread2 = self.riderthread3
                    self.riderthread3 = self.riderthread4
                    self.riderthread4 = self.riderthread5
                    self.riderthread5 = None

                    self.timer2 = self.timer3
                    self.timer3 = self.timer4
                    self.timer4 = self.timer5
                    self.timer5 = None

                    mywindow_myorder.remove_tab(2)
                elif client.key == self.client3.key:
                    print("client3 delete")

                    self.client3 = self.client4
                    self.client4 = self.client5
                    self.client5 = None

                    self.cookthread3 = self.cookthread4
                    self.cookthread4 = self.cookthread5
                    self.cookthread5 = None

                    self.riderthread3 = self.riderthread4
                    self.riderthread4 = self.riderthread5
                    self.riderthread5 = None

                    self.timer3 = self.timer4
                    self.timer4 = self.timer5
                    self.timer5 = None

                    mywindow_myorder.remove_tab(3)
                elif client.key == self.client4.key:
                    print("client4 delete")

                    self.client4 = self.client5
                    self.client5 = None

                    self.cookthread4 = self.cookthread5
                    self.cookthread5 = None

                    self.riderthread4 = self.riderthread5
                    self.riderthread5 = None

                    self.timer4 = self.timer5
                    self.timer5 = None

                    mywindow_myorder.remove_tab(4)
                elif client.key == self.client5.key:
                    print("client5 delete")

                    self.client5 = None

                    self.cookthread5 = None

                    self.riderthread5 = None

                    self.timer5 = None

                    mywindow_myorder.remove_tab(5)

                return

    def new_client(self, client, graph):
        if self.client1 is None:
            self.client1 = client
            client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)

            self.cookthread1 = threading.Thread(target=client_res.cook, args=(client,))
            self.cookthread1.daemon = True
            self.cookthread1.start()

            self.riderthread1 = threading.Thread(target=client.rider.update_pos, args=(graph,))
            self.riderthread1.daemon = True
            self.riderthread1.start()

            self.timer1 = threading.Thread(target=self.timer, args=(client, complete,))
            self.timer1.daemon = True
            self.timer1.start()

        elif self.client2 is None:
            self.client2 = client
            client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)

            self.cookthread2 = threading.Thread(target=client_res.cook, args=(client,))
            self.cookthread2.daemon = True
            self.cookthread2.start()

            self.riderthread2 = threading.Thread(target=client.rider.update_pos, args=(graph,))
            self.riderthread2.daemon = True
            self.riderthread2.start()

            self.timer2 = threading.Thread(target=self.timer, args=(client, complete,))
            self.timer2.daemon = True
            self.timer2.start()

        elif self.client3 is None:
            self.client3 = client
            client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)

            self.cookthread3 = threading.Thread(target=client_res.cook, args=(client,))
            self.cookthread3.daemon = True
            self.cookthread3.start()

            self.riderthread3 = threading.Thread(target=client.rider.update_pos, args=(graph,))
            self.riderthread3.daemon = True
            self.riderthread3.start()

            self.timer3 = threading.Thread(target=self.timer, args=(client, complete,))
            self.timer3.daemon = True
            self.timer3.start()

        elif self.client4 is None:
            self.client4 = client
            client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)

            self.cookthread4 = threading.Thread(target=client_res.cook, args=(client,))
            self.cookthread4.daemon = True
            self.cookthread4.start()

            self.riderthread4 = threading.Thread(target=client.rider.update_pos, args=(graph,))
            self.riderthread4.daemon = True
            self.riderthread4.start()

            self.timer4 = threading.Thread(target=self.timer, args=(client, complete,))
            self.timer4.daemon = True
            self.timer4.start()

        elif self.client5 is None:
            self.client5 = client
            client_res = int_to_restaurant(client.rider.restaurant, self.restaurants)

            self.cookthread5 = threading.Thread(target=client_res.cook, args=(client,))
            self.cookthread5.daemon = True
            self.cookthread5.start()

            self.riderthread5 = threading.Thread(target=client.rider.update_pos, args=(graph,))
            self.riderthread5.daemon = True
            self.riderthread5.start()

            self.timer5 = threading.Thread(target=self.timer, args=(client, complete,))
            self.timer5.daemon = True
            self.timer5.start()

        else:
            return


class Order:
    def __init__(self):
        self.menu_arr = []
        self.count_arr = []

    def add_order(self, menu, count):
        self.menu_arr.append(menu)
        self.count_arr.append(count)  # index 맞춰서


class Restaurant:
    def __init__(self, name, position, menu):
        self.name = name
        self.position = position
        self.menu = menu
        self.queue = []

    def make_delivery(self, client, graph, riders):
        global client_num
        client_num += 1
        client.key = client_num
        client.now = time.time()  # 현재시각
        client.rider = find_rider(graph, riders, self.position)
        rider_to_restaurant = dijsktra(graph, client.rider.position, self.position)
        time_rider_to_restaurant = int(rider_to_restaurant.distance / 100)
        time_cook = 0

        for i in range(len(client.order.menu_arr)):
            time_cook += client.order.menu_arr[i].delay  # 수량 관계 x (주문단위로 시간 계산)

        idx = len(self.queue)
        if idx > 0:

            cnt = 0
            for i in range(idx):
                tmp = 0
                for j in range(len(self.queue[i].order.menu_arr)):
                    tmp += self.queue[i].order.menu_arr[j].delay
                if (time.time() - self.queue[i].now) < tmp:  # 조리가 끝나지 않음
                    if i == cnt:  # 조리가 시작됨
                        time_cook += (tmp - (time.time() - self.queue[i].now))
                    else:  # 조리가 시작되지 않음
                        time_cook += tmp
                else:  # 조리가 끝남
                    cnt += 1

        if time_rider_to_restaurant >= time_cook:
            client.delay = time_rider_to_restaurant
        else:
            client.delay = time_cook
            print("time_cook: ", time_cook)
            client.rider.wait = time_cook - time_rider_to_restaurant

        client.delay += int(dijsktra(graph, self.position, client.position).distance / 100)
        client.rider.destination = client.position
        self.queue.append(client)
        client.rider.update_way(graph)

    def remain(self, client):
        rem = client.now - time.time() + client.delay
        return rem

    def cook(self, client):
        time.sleep(client.delay)
        self.queue[0].rider.delivery_OnOff = 0
        self.queue.pop(0)


class Rider:
    def __init__(self):
        self.position = -1
        self.restaurant = -1
        self.destination = -1
        self.delivery_OnOff = 0  # 배달 시작하면 1로
        self.wait = 0
        self.way = None

    def update_way(self, graph):
        rtr = dijsktra(graph, self.position, self.restaurant)
        rtd = dijsktra(graph, self.restaurant, self.destination)
        self.way = total_way(rtr, rtd)

    def update_pos(self, graph):
        tmp = self.way.head
        while tmp.next is not None:
            if self.position == self.restaurant and self.wait != 0:
                time.sleep(self.wait)
                self.wait = 0
            dist = graph.distance_between_node(tmp.data, tmp.next.data)
            time.sleep(int(dist / 100))
            self.position = tmp.next.data
            tmp = tmp.next

    def random_pos(self):
        self.position = random.randint(1, 23)


class Riders:
    def __init__(self):
        new = Rider()
        self.rider1 = new
        self.rider1.random_pos()
        new = Rider()
        self.rider2 = new
        self.rider2.random_pos()
        new = Rider()
        self.rider3 = new
        self.rider3.random_pos()
        new = Rider()
        self.rider4 = new
        self.rider4.random_pos()
        new = Rider()
        self.rider5 = new
        self.rider5.random_pos()


class Point_on_Map:
    def __init__(self, position_number, position_name, distance):
        self.number = position_number
        self.name = position_name
        self.distance = distance
        self.next = None


class Return_Way_Distance:
    def __init__(self, way, distance):
        self.way = way
        self.distance = distance


class Graph:
    def __init__(self):
        _Map = [None] * 24
        self.Map = _Map

        self.Map[1] = Point_on_Map(6, '신전떡볶이', 751)

        self.Map[2] = Point_on_Map(3, '청춘직화', 240)

        self.Map[3] = Point_on_Map(2, '양현관', 240)
        new = Point_on_Map(4, '새마을금고', 219)
        self.Map[3].next = new

        self.Map[4] = Point_on_Map(3, '청춘직화', 219)
        new = Point_on_Map(5, 'bhc종로성대점', 192)
        self.Map[4].next = new
        new = Point_on_Map(7, '명륜아남아파트', 330)
        self.Map[4].next.next = new
        new = Point_on_Map(8, '포응온베트남쌀국수', 487)
        self.Map[4].next.next.next = new

        self.Map[5] = Point_on_Map(4, '새마을금고', 192)
        new = Point_on_Map(6, '신전떡볶이', 271)
        self.Map[5].next = new

        self.Map[6] = Point_on_Map(1, '성균관대학교', 751)
        new = Point_on_Map(5, 'bhc종로성대점', 271)
        self.Map[6].next = new
        new = Point_on_Map(10, '따띠삼겹(성대앞사거리)', 172)
        self.Map[6].next.next = new

        self.Map[7] = Point_on_Map(4, '새마을금고', 330)
        new = Point_on_Map(9, '혜화동로터리', 345)
        self.Map[7].next = new

        self.Map[8] = Point_on_Map(4, '새마을금고', 487)
        new = Point_on_Map(9, '혜화동로터리', 720)
        self.Map[8].next = new

        self.Map[9] = Point_on_Map(7, '명륜아남아파트', 345)
        new = Point_on_Map(8, '포응온베트남쌀국수', 720)
        self.Map[9].next = new
        new = Point_on_Map(10, '따띠삼겹(성대앞사거리)', 507)
        self.Map[9].next.next = new
        new = Point_on_Map(14, '육수당', 240)
        self.Map[9].next.next.next = new
        new = Point_on_Map(23, '굽네치킨한성대점', 640)
        self.Map[9].next.next.next.next = new

        self.Map[10] = Point_on_Map(6, '신전떡볶이', 172)
        new = Point_on_Map(9, '혜화동로터리', 507)
        self.Map[10].next = new
        new = Point_on_Map(11, '한국예술종합학교대학로캠퍼스', 350)
        self.Map[10].next.next = new
        new = Point_on_Map(12, '깔리', 180)
        self.Map[10].next.next.next = new

        self.Map[11] = Point_on_Map(10, '따띠삼겹', 350)

        self.Map[12] = Point_on_Map(10, '따띠삼겹', 180)
        new = Point_on_Map(13, '버거파크', 230)
        self.Map[12].next = new

        self.Map[13] = Point_on_Map(12, '깔리', 230)
        new = Point_on_Map(16, '혜화역1번출구', 140)
        self.Map[13].next = new

        self.Map[14] = Point_on_Map(9, '혜화동로터리', 240)
        new = Point_on_Map(16, '혜화역1번출구', 193)
        self.Map[14].next = new

        self.Map[15] = Point_on_Map(16, '혜화역1번출구', 58)
        new = Point_on_Map(18, '홍콩반점', 305)
        self.Map[15].next = new

        self.Map[16] = Point_on_Map(13, '버거파크', 140)
        new = Point_on_Map(14, '육수당', 193)
        self.Map[16].next = new
        new = Point_on_Map(15, '버거킹', 58)
        self.Map[16].next.next = new
        new = Point_on_Map(17, '혜화역2번출구', 201)
        self.Map[16].next.next.next = new

        self.Map[17] = Point_on_Map(16, '혜화역1번출구', 201)
        new = Point_on_Map(18, '홍콩반점', 142)
        self.Map[17].next = new
        new = Point_on_Map(19, '죽이야기/서울대학교병원', 353)
        self.Map[17].next.next = new

        self.Map[18] = Point_on_Map(15, '버거킹', 305)
        new = Point_on_Map(17, '혜화역2번출구', 142)
        self.Map[18].next = new
        new = Point_on_Map(20, '마로니에공원뒤쪽', 332)
        self.Map[18].next.next = new

        self.Map[19] = Point_on_Map(17, '혜화역2번출구', 353)
        new = Point_on_Map(20, '마로니에공원뒤쪽', 314)
        self.Map[19].next = new
        new = Point_on_Map(21, '서울대학교사범대부설초등학교', 289)
        self.Map[19].next.next = new

        self.Map[20] = Point_on_Map(18, '홍콩반점', 332)
        new = Point_on_Map(19, '죽이야기/서울대학교병원', 314)
        self.Map[20].next = new

        self.Map[21] = Point_on_Map(19, '죽이야기/서울대학교병원', 289)

        self.Map[22] = Point_on_Map(23, '굽네치킨한성대점', 178)

        self.Map[23] = Point_on_Map(9, '혜화동로터리', 640)
        new = Point_on_Map(22, '한성대입구역1번출구', 178)
        self.Map[23].next = new

    def distance_between_node(self, cur, next):
        tmp = self.Map[cur]
        while tmp.number != next:
            tmp = tmp.next

        return tmp.distance


class Node:  # Node class 정의
    def __init__(self, data):  # node를 생성하고 받은 data를 저장하는 스페셜 메서드
        self.data = data
        self.next = None

    def __str__(self):  # node의 data 값을 출력하는 스페셜 메서드
        return str(self.data)


class LinkedList:  # LinkedList class 정의
    def __init__(self):  # 첫번째 node를 추가하면서, linked list를 생성하는 스페셜 메서드 (create(my_list))
        self.head = None
        self.size = 0  # linked list에 있는 원소 수를 나타내는 변수

    def __str__(self):  # linked list의 모든 node의 data들을 출력하는 스페셜 메서드
        display = '  '
        tmp = self.head
        if tmp == None:
            return display
        while True:
            display += str(tmp)  # 각 node의 data 값을 하나씩 추가
            if tmp.next == None:
                break
            tmp = tmp.next
            display += '->'

        return display

    def insert(self, data):  # linked list의 가장 뒷부분에 node를 추가하는 메서드
        new = Node(data)
        tmp = self.head
        if tmp is None:
            self.head = new
        else:
            while True:
                if tmp.next is None:
                    break
                tmp = tmp.next
            tmp.next = new

        self.size += 1

    def insert_first(self, data):  # 첫번째에 삽입
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1

    def delete_first(self):
        if self.size == 0:  # 원소가 하나도 없을 때
            self.size -= 1
            return -1

        else:
            target = self.head
            self.head = target.next
            self.size -= 1
            return target.data


class Stack:  # Stack class 정의
    def __init__(self):  # 첫번째 헤드 node를 생성하면서, stack을 생성하는 스페셜 메서드
        new = Node(None)
        self.top = new.next  # 헤드 node의 다음이 top에 해당하게 된다
        self.size = 0  # stack의 크기를 저장하는 속성

    def push(self, data):  # stack의 top에 데이터를 push하는 메서드
        new = Node(data)

        new.next = self.top
        self.top = new
        self.size += 1

    def pop(self):  # stack의 top에서 데이터를 pop하는 메서드
        pop_data = self.top.data  # 뽑아낼 데이터를 따로 저장

        target = self.top
        self.top = self.top.next

        del target

        self.size += -1

        return pop_data


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass_chungzik(QMainWindow, form_chungzik_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.ggamang.valueChanged.connect(self.ggamang_spinbox)
        self.bbalgang.valueChanged.connect(self.bbalgang_spinbox)
        self.chungzik_order.clicked.connect(self.btn_order)

        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.orderwidget = orderwidget
        self.ggamangnum = 0
        self.bbalgangnum = 0

    def ggamang_spinbox(self):
        self.ggamangnum = self.ggamang.value()

    def bbalgang_spinbox(self):
        self.bbalgangnum = self.bbalgang.value()

    def btn_order(self):  # 주문하기 눌렀을 때
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.ggamangnum == 0 and self.bbalgangnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.ggamangnum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.ggamangnum)
                if self.bbalgangnum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.bbalgangnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_bhc(QMainWindow, form_bhc_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.bhc_goldking.valueChanged.connect(self.bhc_goldking_spinbox)
        self.bhc_redking.valueChanged.connect(self.bhc_redking_spinbox)
        self.bhc_bburing.valueChanged.connect(self.bhc_bburing_spinbox)
        self.bhc_machoking.valueChanged.connect(self.bhc_machoking_spinbox)
        self.bhc_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.goldkingnum = 0
        self.redkingnum = 0
        self.bburingnum = 0
        self.machokingnum = 0

        self.orderwidget = orderwidget

    def bhc_goldking_spinbox(self):
        self.goldkingnum = self.bhc_goldking.value()

    def bhc_redking_spinbox(self):
        self.redkingnum = self.bhc_redking.value()

    def bhc_bburing_spinbox(self):
        self.bburingnum = self.bhc_bburing.value()

    def bhc_machoking_spinbox(self):
        self.machokingnum = self.bhc_machoking.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.goldkingnum == 0 and self.redkingnum == 0 and self.bburingnum == 0 and self.machokingnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.goldkingnum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.goldkingnum)
                if self.redkingnum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.redkingnum)
                if self.bburingnum > 0:
                    my_order.add_order(self.restaurant.menu[2], self.bburingnum)
                if self.machokingnum > 0:
                    my_order.add_order(self.restaurant.menu[3], self.machokingnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_sinjeon(QMainWindow, form_sinjeon_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.tteokbokki.valueChanged.connect(self.tteokbokki_spinbox)
        self.cheese_tteokbokki.valueChanged.connect(self.cheese_tteokbokki_spinbox)
        self.gimbap.valueChanged.connect(self.gimbap_spinbox)
        self.spammayo.valueChanged.connect(self.spammayo_spinbox)
        self.chamchimayo.valueChanged.connect(self.chamchimayo_spinbox)

        self.sinjeon_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders

        self.tteokbokki_num = 0
        self.cheese_tteokbokki_num = 0
        self.gimbap_num = 0
        self.spammayo_num = 0
        self.chamchimayo_num = 0

        self.orderwidget = orderwidget

    def tteokbokki_spinbox(self):
        self.tteokbokki_num = self.tteokbokki.value()

    def cheese_tteokbokki_spinbox(self):
        self.cheese_tteokbokki_num = self.cheese_tteokbokki.value()

    def gimbap_spinbox(self):
        self.gimbap_num = self.gimbap.value()

    def spammayo_spinbox(self):
        self.spammayo_num = self.spammayo.value()

    def chamchimayo_spinbox(self):
        self.chamchimayo_num = self.chamchimayo.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.tteokbokki_num == 0 and self.cheese_tteokbokki_num == 0 and self.gimbap_num == 0 and self.spammayo_num == 0 and self.chamchimayo_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.tteokbokki_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.tteokbokki_num)
                if self.cheese_tteokbokki_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.cheese_tteokbokki_num)
                if self.gimbap_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.gimbap_num)
                if self.spammayo_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.spammayo_num)
                if self.chamchimayo_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.chamchimayo_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_ddatti(QMainWindow, form_ddatti_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.simple_double.valueChanged.connect(self.simple_double_spinbox)
        self.simple_meat.valueChanged.connect(self.simple_meat_spinbox)
        self.simple_original.valueChanged.connect(self.simple_original_spinbox)
        self.bap.valueChanged.connect(self.bap_spinbox)
        self.ddatti_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.doublenum = 0
        self.meatnum = 0
        self.originalnum = 0
        self.bapnum = 0
        self.orderwidget = orderwidget

    def simple_double_spinbox(self):
        self.doublenum = self.simple_double.value()

    def simple_meat_spinbox(self):
        self.meatnum = self.simple_meat.value()

    def simple_original_spinbox(self):
        self.originalnum = self.simple_original.value()

    def bap_spinbox(self):
        self.bapnum = self.bap.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.doublenum == 0 and self.meatnum == 0 and self.originalnum == 0 and self.bapnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.doublenum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.doublenum)
                if self.meatnum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.meatnum)
                if self.originalnum > 0:
                    my_order.add_order(self.restaurant.menu[2], self.originalnum)
                if self.bapnum > 0:
                    my_order.add_order(self.restaurant.menu[3], self.bapnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_galli(QMainWindow, form_galli_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.aset.valueChanged.connect(self.aset_spinbox)
        self.saecurry.valueChanged.connect(self.saecurry_spinbox)
        self.saecorma.valueChanged.connect(self.saecorma_spinbox)
        self.yangma.valueChanged.connect(self.yangma_spinbox)
        self.yangbin.valueChanged.connect(self.yangbin_spinbox)
        self.galli_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.asetnum = 0
        self.saecurrynum = 0
        self.saecormanum = 0
        self.yangmanum = 0
        self.yangbinnum = 0
        self.orderwidget = orderwidget

    def aset_spinbox(self):
        self.asetnum = self.aset.value()

    def saecurry_spinbox(self):
        self.saecurrynum = self.saecurry.value()

    def saecorma_spinbox(self):
        self.saecormanum = self.saecorma.value()

    def yangma_spinbox(self):
        self.yangmanum = self.yangma.value()

    def yangbin_spinbox(self):
        self.yangbinnum = self.yangbin.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.asetnum == 0 and self.saecurrynum == 0 and self.saecormanum == 0 and self.yangmanum == 0 and self.yangbinnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.asetnum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.asetnum)
                if self.saecurrynum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.saecurrynum)
                if self.saecormanum > 0:
                    my_order.add_order(self.restaurant.menu[2], self.saecormanum)
                if self.yangmanum > 0:
                    my_order.add_order(self.restaurant.menu[3], self.yangmanum)
                if self.yangbinnum > 0:
                    my_order.add_order(self.restaurant.menu[4], self.yangbinnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_yooksudang(QMainWindow, form_yooksudang_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.sundae.valueChanged.connect(self.sundae_spinbox)
        self.suyook.valueChanged.connect(self.suyook_spinbox)
        self.ttarou.valueChanged.connect(self.ttarou_spinbox)
        self.kimchi.valueChanged.connect(self.kimchi_spinbox)
        self.gogifry.valueChanged.connect(self.gogifry_spinbox)

        self.yooksudang_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders

        self.sundae_num = 0
        self.suyook_num = 0
        self.ttarou_num = 0
        self.kimchi_num = 0
        self.gogifry_num = 0
        self.orderwidget = orderwidget

    def sundae_spinbox(self):
        self.sundae_num = self.sundae.value()

    def suyook_spinbox(self):
        self.suyook_num = self.suyook.value()

    def ttarou_spinbox(self):
        self.ttarou_num = self.ttarou.value()

    def kimchi_spinbox(self):
        self.kimchi_num = self.kimchi.value()

    def gogifry_spinbox(self):
        self.gogifry_num = self.gogifry.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.sundae_num == 0 and self.suyook_num == 0 and self.ttarou_num == 0 and self.kimchi_num == 0 and self.gogifry_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.sundae_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.sundae_num)
                if self.suyook_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.suyook_num)
                if self.ttarou_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.ttarou_num)
                if self.kimchi_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.kimchi_num)
                if self.gogifry_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.gogifry_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_burgerpark(QMainWindow, form_burgerpark_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.bacon.valueChanged.connect(self.bacon_spinbox)
        self.avocado.valueChanged.connect(self.avocado_spinbox)
        self.cheese.valueChanged.connect(self.cheese_spinbox)
        self.mushroom.valueChanged.connect(self.mushroom_spinbox)
        self.shrimp.valueChanged.connect(self.shrimp_spinbox)

        self.burgerpark_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders

        self.bacon_num = 0
        self.avocado_num = 0
        self.cheese_num = 0
        self.mushroom_num = 0
        self.shrimp_num = 0
        self.orderwidget = orderwidget

    def bacon_spinbox(self):
        self.bacon_num = self.bacon.value()

    def avocado_spinbox(self):
        self.avocado_num = self.avocado.value()

    def cheese_spinbox(self):
        self.cheese_num = self.cheese.value()

    def mushroom_spinbox(self):
        self.mushroom_num = self.mushroom.value()

    def shrimp_spinbox(self):
        self.shrimp_num = self.shrimp.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.bacon_num == 0 and self.avocado_num == 0 and self.cheese_num == 0 and self.mushroom_num == 0 and self.shrimp_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.bacon_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.bacon_num)
                if self.avocado_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.avocado_num)
                if self.cheese_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.cheese_num)
                if self.mushroom_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.mushroom_num)
                if self.shrimp_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.shrimp_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_hongkongbanjeom(QMainWindow, form_hongkongbanjeom_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.jjajangmeon.valueChanged.connect(self.jjajangmeon_spinbox)
        self.jjambbong.valueChanged.connect(self.jjambbong_spinbox)
        self.jjajangbab.valueChanged.connect(self.jjajangbab_spinbox)
        self.jjambbongbab.valueChanged.connect(self.jjambbongbab_spinbox)
        self.tangsuyooksmall.valueChanged.connect(self.tangsuyooksmall_spinbox)
        self.tangsuyookbig.valueChanged.connect(self.tangsuyookbig_spinbox)

        self.hongkongbanjeom_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.orderwidget = orderwidget

        self.jjajangmeon_num = 0
        self.jjambbong_num = 0
        self.jjajangbab_num = 0
        self.jjambbongbab_num = 0
        self.tangsuyooksmall_num = 0
        self.tangsuyookbig_num = 0

    def jjajangmeon_spinbox(self):
        self.jjajangmeon_num = self.jjajangmeon.value()

    def jjambbong_spinbox(self):
        self.jjambbong_num = self.jjambbong.value()

    def jjajangbab_spinbox(self):
        self.jjajangbab_num = self.jjajangbab.value()

    def jjambbongbab_spinbox(self):
        self.jjambbongbab_num = self.jjambbongbab.value()

    def tangsuyooksmall_spinbox(self):
        self.tangsuyooksmall_num = self.tangsuyooksmall.value()

    def tangsuyookbig_spinbox(self):
        self.tangsuyookbig_num = self.tangsuyookbig.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.jjajangmeon_num == 0 and self.jjambbong_num == 0 and self.jjajangbab_num == 0 and self.jjambbongbab_num == 0 and self.tangsuyooksmall_num == 0 and self.tangsuyookbig_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.jjajangmeon_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.jjajangmeon_num)
                if self.jjambbong_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.jjambbong_num)
                if self.jjajangbab_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.jjajangbab_num)
                if self.jjambbongbab_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.jjambbongbab_num)
                if self.tangsuyooksmall_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.tangsuyooksmall_num)
                if self.tangsuyookbig_num > 0:
                    my_order.add_order(self.restaurant.menu[5], self.tangsuyookbig_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_jukstory(QMainWindow, form_jukstory_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.junbok.valueChanged.connect(self.junbok_spinbox)
        self.samsunjjambbong.valueChanged.connect(self.samsunjjambbong_spinbox)
        self.bulnak.valueChanged.connect(self.bulnak_spinbox)
        self.maesaeng.valueChanged.connect(self.maesaeng_spinbox)
        self.jukstory_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.junboknum = 0
        self.samsunjjambbongnum = 0
        self.bulnaknum = 0
        self.maesaengnum = 0
        self.orderwidget = orderwidget

    def junbok_spinbox(self):
        self.junboknum = self.junbok.value()

    def samsunjjambbong_spinbox(self):
        self.samsunjjambbongnum = self.samsunjjambbong.value()

    def bulnak_spinbox(self):
        self.bulnaknum = self.bulnak.value()

    def maesaeng_spinbox(self):
        self.maesaengnum = self.maesaeng.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.junboknum == 0 and self.samsunjjambbongnum == 0 and self.bulnaknum == 0 and self.maesaengnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.junboknum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.junboknum)
                if self.samsunjjambbongnum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.samsunjjambbongnum)
                if self.bulnaknum > 0:
                    my_order.add_order(self.restaurant.menu[2], self.bulnaknum)
                if self.maesaengnum > 0:
                    my_order.add_order(self.restaurant.menu[3], self.maesaengnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_phongon(QMainWindow, form_phongon_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.jikwha.valueChanged.connect(self.jikwha_spinbox)
        self.bunjja.valueChanged.connect(self.bunjja_spinbox)
        self.yangji.valueChanged.connect(self.yangji_spinbox)
        self.chadol.valueChanged.connect(self.chadol_spinbox)
        self.phongon_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders
        self.jikwhanum = 0
        self.bunjjanum = 0
        self.yangjinum = 0
        self.chadolnum = 0
        self.orderwidget = orderwidget

    def jikwha_spinbox(self):
        self.jikwhanum = self.jikwha.value()

    def bunjja_spinbox(self):
        self.bunjjanum = self.bunjja.value()

    def yangji_spinbox(self):
        self.yangjinum = self.yangji.value()

    def chadol_spinbox(self):
        self.chadolnum = self.chadol.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.jikwhanum == 0 and self.bunjjanum == 0 and self.yangjinum == 0 and self.chadolnum == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.jikwhanum > 0:
                    my_order.add_order(self.restaurant.menu[0], self.jikwhanum)
                if self.bunjjanum > 0:
                    my_order.add_order(self.restaurant.menu[1], self.bunjjanum)
                if self.yangjinum > 0:
                    my_order.add_order(self.restaurant.menu[2], self.yangjinum)
                if self.chadolnum > 0:
                    my_order.add_order(self.restaurant.menu[3], self.chadolnum)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_goobne(QMainWindow, form_goobne_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.galbi.valueChanged.connect(self.galbi_spinbox)
        self.maravolcano.valueChanged.connect(self.maravolcano_spinbox)
        self.honeymello.valueChanged.connect(self.honeymello_spinbox)
        self.original.valueChanged.connect(self.original_spinbox)
        self.gochu.valueChanged.connect(self.gochu_spinbox)

        self.goobne_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders

        self.galbi_num = 0
        self.maravolcano_num = 0
        self.honeymello_num = 0
        self.original_num = 0
        self.gochu_num = 0
        self.orderwidget = orderwidget

    def galbi_spinbox(self):
        self.galbi_num = self.galbi.value()

    def maravolcano_spinbox(self):
        self.maravolcano_num = self.maravolcano.value()

    def honeymello_spinbox(self):
        self.honeymello_num = self.honeymello.value()

    def original_spinbox(self):
        self.original_num = self.original.value()

    def gochu_spinbox(self):
        self.gochu_num = self.gochu.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.galbi_num == 0 and self.maravolcano_num == 0 and self.honeymello_num == 0 and self.original_num == 0 and self.gochu_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.galbi_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.galbi_num)
                if self.maravolcano_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.maravolcano_num)
                if self.honeymello_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.honeymello_num)
                if self.original_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.original_num)
                if self.gochu_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.gochu_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


class WindowClass_burgerking(QMainWindow, form_burgerking_menu):
    def __init__(self, restaurant, clients, graph, riders, orderwidget):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.Whopper.valueChanged.connect(self.Whopper_spinbox)
        self.cheezeWhopper.valueChanged.connect(self.cheezeWhopper_spinbox)
        self.quatrocheezeWhopper.valueChanged.connect(self.quatrocheezeWhopper_spinbox)
        self.shrimpsteak.valueChanged.connect(self.shrimpsteak_spinbox)
        self.Whopper_jr.valueChanged.connect(self.Whopper_jr_spinbox)

        self.burgerking_order.clicked.connect(self.btn_order)
        self.restaurant = restaurant
        self.clients = clients
        self.graph = graph
        self.riders = riders

        self.Whopper_num = 0
        self.cheezeWhopper_num = 0
        self.quatrocheezeWhopper_num = 0
        self.shrimpsteak_num = 0
        self.Whopper_jr_num = 0
        self.orderwidget = orderwidget

    def Whopper_spinbox(self):
        self.Whopper_num = self.Whopper.value()

    def cheezeWhopper_spinbox(self):
        self.cheezeWhopper_num = self.cheezeWhopper.value()

    def quatrocheezeWhopper_spinbox(self):
        self.quatrocheezeWhopper_num = self.quatrocheezeWhopper.value()

    def shrimpsteak_spinbox(self):
        self.shrimpsteak_num = self.shrimpsteak.value()

    def Whopper_jr_spinbox(self):
        self.Whopper_jr_num = self.Whopper_jr.value()

    def btn_order(self):
        order_reply = QMessageBox.question(self, "주문", "정말 주문하시겠습니까?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if order_reply == QMessageBox.Yes:
            if self.clients.client1 is not None and self.clients.client2 is not None and self.clients.client3 is not None and self.clients.client4 is not None and self.clients.client5 is not None:
                QMessageBox.about(self, "Warning!", "현재 주문이 몰려서 배달이 어렵습니다.\n잠시 후 다시 시도해주세요!")
            else:
                my_order = Order()
                if self.Whopper_num == 0 and self.cheezeWhopper_num == 0 and self.quatrocheezeWhopper_num == 0 and self.shrimpsteak_num == 0 and self.Whopper_jr_num == 0:
                    QMessageBox.about(self, "Warning", "수량을 선택해주세요.")
                    return
                if self.Whopper_num > 0:
                    my_order.add_order(self.restaurant.menu[0], self.Whopper_num)
                if self.cheezeWhopper_num > 0:
                    my_order.add_order(self.restaurant.menu[1], self.cheezeWhopper_num)
                if self.quatrocheezeWhopper_num > 0:
                    my_order.add_order(self.restaurant.menu[2], self.quatrocheezeWhopper_num)
                if self.shrimpsteak_num > 0:
                    my_order.add_order(self.restaurant.menu[3], self.shrimpsteak_num)
                if self.Whopper_jr_num > 0:
                    my_order.add_order(self.restaurant.menu[4], self.Whopper_jr_num)

                new_client = Client(my_order, clientpos)
                self.restaurant.make_delivery(new_client, self.graph, self.riders)
                self.clients.new_client(new_client, self.graph)
                self.orderwidget.add_new_tap(self.restaurant, new_client)
                self.destroy()


##############

class Windowclass_riderway(QMainWindow, form_rider_app):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.loc_x = 8
        self.loc_y = 8
        self.destination_loc_x = 35
        self.destination_loc_y = 78
        self.pickup_loc_x = 28
        self.pickup_loc_y = 78
        self.start_loc_x = 15
        self.start_loc_y = 63
        self.rider_loc_x = 20
        self.rider_loc_y = 20

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("new_map1.png")
        painter.drawPixmap(self.rect(), pixmap)

        self.pushButton.setIcon(QIcon('button.PNG'))
        self.pushButton.setIconSize(QSize(16, 16))
        self.pushButton_2.setIcon(QIcon('button.PNG'))
        self.pushButton_2.setIconSize(QSize(16, 16))
        self.pushButton_3.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_3.setIconSize(QSize(16, 16))
        self.pushButton_4.setIcon(QIcon('button.PNG'))
        self.pushButton_4.setIconSize(QSize(16, 16))
        self.pushButton_5.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_5.setIconSize(QSize(16, 16))
        self.pushButton_6.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_6.setIconSize(QSize(16, 16))
        self.pushButton_7.setIcon(QIcon('button.PNG'))
        self.pushButton_7.setIconSize(QSize(16, 16))
        self.pushButton_8.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_8.setIconSize(QSize(16, 16))
        self.pushButton_9.setIcon(QIcon('button.PNG'))
        self.pushButton_9.setIconSize(QSize(16, 16))
        self.pushButton_10.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_10.setIconSize(QSize(16, 16))
        self.pushButton_11.setIcon(QIcon('button.PNG'))
        self.pushButton_11.setIconSize(QSize(16, 16))
        self.pushButton_12.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_12.setIconSize(QSize(16, 16))
        self.pushButton_13.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_13.setIconSize(QSize(16, 16))
        self.pushButton_14.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_14.setIconSize(QSize(16, 16))
        self.pushButton_15.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_16.setIcon(QIcon('button.PNG'))
        self.pushButton_16.setIconSize(QSize(16, 16))
        self.pushButton_17.setIcon(QIcon('button.PNG'))
        self.pushButton_17.setIconSize(QSize(16, 16))
        self.pushButton_18.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_18.setIconSize(QSize(16, 16))
        self.pushButton_19.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_19.setIconSize(QSize(16, 16))
        self.pushButton_20.setIcon(QIcon('button.PNG'))
        self.pushButton_20.setIconSize(QSize(16, 16))
        self.pushButton_21.setIcon(QIcon('button.PNG'))
        self.pushButton_21.setIconSize(QSize(16, 16))
        self.pushButton_22.setIcon(QIcon('button.PNG'))
        self.pushButton_22.setIconSize(QSize(16, 16))
        self.pushButton_23.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_23.setIconSize(QSize(16, 16))

        self.draw_line(painter, riderwayclient)

    def label_rider(self):
        self.rider_image = QPixmap()
        self.rider_image.load("라이더.png")
        self.rider.setPixmap(self.rider_image)

    def label_destinaion(self):
        self.destination_image = QPixmap()
        self.destination_image.load("전달.png")
        self.destination.setPixmap(self.destination_image)

    def label_pickup(self):
        self.pickup_image = QPixmap()
        self.pickup_image.load("픽업.png")
        self.pickup_image = self.pickup_image.scaledToWidth(68)
        self.pickup_image = self.pickup_image.scaledToHeight(88)
        self.pickup.setPixmap(self.pickup_image)

    def label_startnode(self):
        self.startnode_image = QPixmap()
        self.startnode_image.load("start.png")
        self.start.setPixmap(self.startnode_image)

    def draw_line(self, qp, client):
        tl = LinkedList()

        thead = client.rider.way.head
        while thead is not None:
            tl.insert(thead.data)
            thead = thead.next
        tl.insert(client.position)

        tmp = tl.head
        xy = self.num_to_xy(tmp.data)
        self.label_startnode()
        self.start.setGeometry(xy.x - self.start_loc_x, xy.y - self.start_loc_y, 80, 80)

        while tmp.next is not None:
            xy = self.num_to_xy(tmp.data)
            xy_next = self.num_to_xy(tmp.next.data)
            if tmp.data == client.rider.position:
                self.label_rider()
                self.rider.setGeometry(xy.x - self.rider_loc_x, xy.y - self.rider_loc_y, 80, 80)
            if tmp.data == client.rider.restaurant:
                self.label_pickup()
                self.pickup.setGeometry(xy.x - self.pickup_loc_x, xy.y - self.pickup_loc_y, 100, 100)
            if tmp.next.data == client.rider.destination:
                self.label_destinaion()
                self.destination.setGeometry(xy_next.x - self.destination_loc_x, xy_next.y - self.destination_loc_y,
                                             100, 100)
            qp.setPen(QPen(Qt.white, 7))
            qp.drawLine(xy.x + self.loc_x, xy.y + self.loc_y, xy_next.x + self.loc_x, xy_next.y + self.loc_y)
            tmp = tmp.next


    def num_to_xy(self, num):
        xy = XY()
        if num == 1:
            xy.x = 130
            xy.y = 200
        elif num == 2:
            xy.x = 160
            xy.y = 100
        elif num == 3:
            xy.x = 220
            xy.y = 160
        elif num == 4:
            xy.x = 330
            xy.y = 230
        elif num == 5:
            xy.x = 330
            xy.y = 280
        elif num == 6:
            xy.x = 370
            xy.y = 450
        elif num == 7:
            xy.x = 450
            xy.y = 310
        elif num == 8:
            xy.x = 410
            xy.y = 150
        elif num == 9:
            xy.x = 590
            xy.y = 390
        elif num == 10:
            xy.x = 450
            xy.y = 560
        elif num == 11:
            xy.x = 390
            xy.y = 630
        elif num == 12:
            xy.x = 470
            xy.y = 610
        elif num == 13:
            xy.x = 580
            xy.y = 620
        elif num == 14:
            xy.x = 590
            xy.y = 500
        elif num == 15:
            xy.x = 670
            xy.y = 530
        elif num == 16:
            xy.x = 630
            xy.y = 570
        elif num == 17:
            xy.x = 640
            xy.y = 660
        elif num == 18:
            xy.x = 730
            xy.y = 650
        elif num == 19:
            xy.x = 650
            xy.y = 810
        elif num == 20:
            xy.x = 740
            xy.y = 780
        elif num == 21:
            xy.x = 660
            xy.y = 940
        elif num == 22:
            xy.x = 970
            xy.y = 140
        elif num == 23:
            xy.x = 900
            xy.y = 200
        return xy


class XY:
    def __init__(self):
        self.x = -1
        self.y = -1


class WindowClass_myOrder(QMainWindow, form_Myorder):
    def __init__(self, clients, restaurants):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.clients = clients
        self.restaurants = restaurants

        self.tabcount = 0

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.tabUsing = []
        self.tabUnusing = [1, 2, 3, 4, 5]

    def add_new_tap(self, restaurant, client):
        self.tabcount += 1

        if self.tabUnusing[0] == 1:
            self.tabs.addTab(self.tab1, "client number: {}".format(client.key))
            self.label2 = QLabel(self.tab1)
            self.label2.setGeometry(30, 40, 211, 31)
            self.label2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2.setObjectName("label2")
            self.label2.setText("배달이 진행중이에요.")

            self.label2_restaurantname = QLabel(self.tab1)
            self.label2_restaurantname.setGeometry(30, 70, 211, 71)
            self.label2_restaurantname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 25pt \"배달의민족 한나체 Pro\";")
            self.label2_restaurantname.setObjectName("label2_restaurantname")
            self.label2_restaurantname.setText("%s" % (restaurant.name))

            self.label2_menufirst = QLabel(self.tab1)
            self.label2_menufirst.setGeometry(30, 140, 211, 31)
            self.label2_menufirst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menufirst.setObjectName("label2_menufirst")
            self.label2_order_date = QLabel(self.tab1)
            self.label2_order_date.setGeometry(30, 210, 211, 31)
            self.label2_order_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_order_date.setObjectName("label2_order_date")

            ## 라벨 1
            self.label2_menu2_cnt = QLabel(self.tab1)
            self.label2_menu2_cnt.setGeometry(30, 290, 301, 31)
            self.label2_menu2_cnt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_cnt.setObjectName("label2_menu1_cnt")

            self.label2_menu2_price = QLabel(self.tab1)
            self.label2_menu2_price.setGeometry(300, 290, 91, 31)
            self.label2_menu2_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_menu2_price.setObjectName("label2_menu1_price")
            ## 라벨 2
            self.label3_menu2_cnt = QLabel(self.tab1)
            self.label3_menu2_cnt.setGeometry(30, 340, 301, 31)
            self.label3_menu2_cnt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_cnt.setObjectName("label3_menu1_cnt")
            self.label3_menu2_price = QLabel(self.tab1)
            self.label3_menu2_price.setGeometry(300, 340, 91, 31)
            self.label3_menu2_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label3_menu2_price.setObjectName("label3_menu1_price")
            ## 라벨 3
            self.label4_menu2_cnt = QLabel(self.tab1)
            self.label4_menu2_cnt.setGeometry(30, 390, 301, 31)
            self.label4_menu2_cnt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_cnt.setObjectName("label4_menu1_cnt")
            self.label4_menu2_price = QLabel(self.tab1)
            self.label4_menu2_price.setGeometry(300, 390, 91, 31)
            self.label4_menu2_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label4_menu2_price.setObjectName("label4_menu1_price")
            ## 라벨 4
            self.label5_menu2_cnt = QLabel(self.tab1)
            self.label5_menu2_cnt.setGeometry(30, 440, 301, 31)
            self.label5_menu2_cnt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_cnt.setObjectName("label5_menu1_cnt")
            self.label5_menu2_price = QLabel(self.tab1)
            self.label5_menu2_price.setGeometry(300, 440, 91, 31)
            self.label5_menu2_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label5_menu2_price.setObjectName("label5_menu1_price")
            ## 라벨 5
            self.label6_menu2_cnt = QLabel(self.tab1)
            self.label6_menu2_cnt.setGeometry(30, 490, 301, 31)
            self.label6_menu2_cnt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_cnt.setObjectName("label6_menu1_cnt")
            self.label6_menu2_price = QLabel(self.tab1)
            self.label6_menu2_price.setGeometry(300, 490, 91, 31)
            self.label6_menu2_price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_price.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label6_menu2_price.setObjectName("label6_menu1_price")

            self.label2_progress = QLabel(self.tab1)
            self.label2_progress.setGeometry(QRect(100, 650, 271, 31))
            self.label2_progress.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "font: 13.5pt \"배달의민족 한나체 Air\";")
            self.label2_progress.setAlignment(Qt.AlignCenter)
            self.label2_progress.setObjectName("label2_progress")
            self.label2_totalprice = QLabel(self.tab1)
            self.label2_totalprice.setGeometry(QRect(30, 560, 161, 71))
            self.label2_totalprice.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "\n"
                                                 "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_totalprice.setObjectName("label2_totalprice")
            self.label2_int_totalprice = QLabel(self.tab1)
            self.label2_int_totalprice.setGeometry(QRect(270, 560, 151, 71))
            self.label2_int_totalprice.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_int_totalprice.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_int_totalprice.setObjectName("label2_int_totalprice")

            self.pushButton2_2 = QPushButton(self.tab1)
            self.pushButton2_2.setGeometry(290, 690, 131, 41)
            self.pushButton2_2.setObjectName("pushButton2_2")
            self.pushButton2_2.setText("라이더님 위치 보기")
            self.pushButton2_2.clicked.connect(lambda: self.show_ridertab(client))

            self.f5_button1 = QPushButton(self.tab1)
            self.f5_button1.setGeometry(70, 650, 31, 31)
            self.f5_button1.setIcon(QIcon('refresh.png'))
            self.f5_button1.setIconSize(QSize(31, 31))
            self.f5_button1.setObjectName("f5_button1")
            self.f5_button1.clicked.connect(lambda: self.label_1_f5(client, restaurant))

            self.label2_menufirst.setText(
                "{} 외 {}개".format(client.order.menu_arr[0].name, len(client.order.menu_arr) - 1))
            t = time.localtime(client.now)
            self.label2_order_date.setText("주문일시 : {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

            cost = 0
            for i in range(len(client.order.menu_arr)):
                cost += ((client.order.menu_arr[i].price) * client.order.count_arr[i])

            length = len(client.order.menu_arr)

            if length == 1:
                self.label2_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
            elif length == 2:
                self.label2_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
            elif length == 3:
                self.label2_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
            elif length == 4:
                self.label2_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
            elif length > 4:  # textbox의 한계로 메뉴 5개까지만 표시하는 것으로 했습니다.
                self.label2_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
                self.label6_menu2_cnt.setText(
                    "{} {} 개".format(client.order.menu_arr[4].name, client.order.count_arr[4]))
                self.label6_menu2_price.setText(
                    "{} 원".format((client.order.menu_arr[4].price) * client.order.count_arr[4]))

            self.label2_progress.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))
            self.label2_totalprice.setText("총 주문금액")
            self.label2_int_totalprice.setText("{} 원".format(cost))

            self.tabUnusing.pop(0)
            self.tabUsing.append(1)

        elif self.tabUnusing[0] == 2:
            self.tabs.addTab(self.tab2, "client number: {}".format(client.key))
            self.label3 = QLabel(self.tab2)
            self.label3.setGeometry(30, 40, 211, 31)
            self.label3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3.setObjectName("label3")
            self.label3.setText("배달이 진행중이에요.")

            self.label3_restaurantname = QLabel(self.tab2)
            self.label3_restaurantname.setGeometry(30, 70, 211, 71)
            self.label3_restaurantname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 25pt \"배달의민족 한나체 Pro\";")
            self.label3_restaurantname.setObjectName("label3_restaurantname")
            self.label3_restaurantname.setText("%s" % (restaurant.name))

            self.label3_menufirst = QLabel(self.tab2)
            self.label3_menufirst.setGeometry(30, 140, 211, 31)
            self.label3_menufirst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menufirst.setObjectName("label3_menufirst")
            self.label3_order_date = QLabel(self.tab2)
            self.label3_order_date.setGeometry(30, 210, 211, 31)
            self.label3_order_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_order_date.setObjectName("label3_order_date")
            ## 라벨 1
            self.label2_menu2_cnt2 = QLabel(self.tab2)
            self.label2_menu2_cnt2.setGeometry(30, 290, 301, 31)
            self.label2_menu2_cnt2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_cnt2.setObjectName("label2_menu1_cnt2")

            self.label2_menu2_price2 = QLabel(self.tab2)
            self.label2_menu2_price2.setGeometry(300, 290, 91, 31)
            self.label2_menu2_price2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_price2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_menu2_price2.setObjectName("label2_menu1_price2")
            ## 라벨 2
            self.label3_menu2_cnt2 = QLabel(self.tab2)
            self.label3_menu2_cnt2.setGeometry(30, 340, 301, 31)
            self.label3_menu2_cnt2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_cnt2.setObjectName("label3_menu1_cnt2")
            self.label3_menu2_price2 = QLabel(self.tab2)
            self.label3_menu2_price2.setGeometry(300, 340, 91, 31)
            self.label3_menu2_price2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_price2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label3_menu2_price2.setObjectName("label3_menu1_price2")
            ## 라벨 3
            self.label4_menu2_cnt2 = QLabel(self.tab2)
            self.label4_menu2_cnt2.setGeometry(30, 390, 301, 31)
            self.label4_menu2_cnt2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_cnt2.setObjectName("label4_menu1_cnt2")
            self.label4_menu2_price2 = QLabel(self.tab2)
            self.label4_menu2_price2.setGeometry(300, 390, 91, 31)
            self.label4_menu2_price2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_price2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label4_menu2_price2.setObjectName("label4_menu1_price2")
            ## 라벨 4
            self.label5_menu2_cnt2 = QLabel(self.tab2)
            self.label5_menu2_cnt2.setGeometry(30, 440, 301, 31)
            self.label5_menu2_cnt2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_cnt2.setObjectName("label5_menu1_cnt2")
            self.label5_menu2_price2 = QLabel(self.tab2)
            self.label5_menu2_price2.setGeometry(300, 440, 91, 31)
            self.label5_menu2_price2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_price2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label5_menu2_price2.setObjectName("label5_menu1_price2")
            ## 라벨 5
            self.label6_menu2_cnt2 = QLabel(self.tab2)
            self.label6_menu2_cnt2.setGeometry(30, 490, 301, 31)
            self.label6_menu2_cnt2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_cnt2.setObjectName("label6_menu1_cnt2")
            self.label6_menu2_price2 = QLabel(self.tab2)
            self.label6_menu2_price2.setGeometry(300, 490, 91, 31)
            self.label6_menu2_price2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_price2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label6_menu2_price2.setObjectName("label6_menu1_price2")

            self.label2_progress2 = QLabel(self.tab2)
            self.label2_progress2.setGeometry(QRect(100, 650, 271, 31))
            self.label2_progress2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 13.5pt \"배달의민족 한나체 Air\";")
            self.label2_progress2.setAlignment(Qt.AlignCenter)
            self.label2_progress2.setObjectName("label2_progress2")
            self.label2_totalprice2 = QLabel(self.tab2)
            self.label2_totalprice2.setGeometry(QRect(30, 560, 161, 71))
            self.label2_totalprice2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_totalprice2.setObjectName("label2_totalprice2")
            self.label2_int_totalprice2 = QLabel(self.tab2)
            self.label2_int_totalprice2.setGeometry(QRect(270, 560, 151, 71))
            self.label2_int_totalprice2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "\n"
                                                      "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_int_totalprice2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_int_totalprice2.setObjectName("label2_int_totalprice2")

            self.pushButton2_2_2 = QPushButton(self.tab2)
            self.pushButton2_2_2.setGeometry(290, 690, 131, 41)
            self.pushButton2_2_2.setObjectName("pushButton2_2_2")
            self.pushButton2_2_2.setText("라이더님 위치 보기")
            self.pushButton2_2_2.clicked.connect(lambda: self.show_ridertab(client))
            self.f5_button2 = QPushButton(self.tab2)
            self.f5_button2.setGeometry(70, 650, 31, 31)
            self.f5_button2.setIcon(QIcon('refresh.png'))
            self.f5_button2.setIconSize(QSize(31, 31))
            self.f5_button2.setObjectName("f5_button2")
            self.f5_button2.clicked.connect(lambda: self.label_2_f5(client, restaurant))

            self.label3_menufirst.setText(
                "{} 외 {}개".format(client.order.menu_arr[0].name, len(client.order.menu_arr) - 1))
            t = time.localtime(client.now)
            self.label3_order_date.setText("주문일시 : {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

            cost = 0
            for i in range(len(client.order.menu_arr)):
                cost += ((client.order.menu_arr[i].price) * client.order.count_arr[i])

            length = len(client.order.menu_arr)

            if length == 1:
                self.label2_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
            elif length == 2:
                self.label2_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
            elif length == 3:
                self.label2_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
            elif length == 4:
                self.label2_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
            elif length > 4:  # textbox의 한계로 메뉴 5개까지만 표시하는 것으로 했습니다.
                self.label2_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
                self.label6_menu2_cnt2.setText(
                    "{} {} 개".format(client.order.menu_arr[4].name, client.order.count_arr[4]))
                self.label6_menu2_price2.setText(
                    "{} 원".format((client.order.menu_arr[4].price) * client.order.count_arr[4]))

            self.label2_progress2.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))
            self.label2_totalprice2.setText("총 주문금액")
            self.label2_int_totalprice2.setText("{} 원".format(cost))

            self.tabUnusing.pop(0)
            self.tabUsing.append(2)

        elif self.tabUnusing[0] == 3:
            self.tabs.addTab(self.tab3, "client number: {}".format(client.key))
            self.label4 = QLabel(self.tab3)
            self.label4.setGeometry(30, 40, 211, 31)
            self.label4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4.setObjectName("label4")
            self.label4.setText("배달이 진행중이에요.")

            self.label4_restaurantname = QLabel(self.tab3)
            self.label4_restaurantname.setGeometry(30, 70, 211, 71)
            self.label4_restaurantname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 25pt \"배달의민족 한나체 Pro\";")
            self.label4_restaurantname.setObjectName("label4_restaurantname")
            self.label4_restaurantname.setText("%s" % (restaurant.name))

            self.label4_menufirst = QLabel(self.tab3)
            self.label4_menufirst.setGeometry(30, 140, 211, 31)
            self.label4_menufirst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menufirst.setObjectName("label4_menufirst")
            self.label4_order_date = QLabel(self.tab3)
            self.label4_order_date.setGeometry(30, 210, 211, 31)
            self.label4_order_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_order_date.setObjectName("label4_order_date")
            ## 라벨 1
            self.label2_menu2_cnt3 = QLabel(self.tab3)
            self.label2_menu2_cnt3.setGeometry(30, 290, 301, 31)
            self.label2_menu2_cnt3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_cnt3.setObjectName("label2_menu1_cnt3")

            self.label2_menu2_price3 = QLabel(self.tab3)
            self.label2_menu2_price3.setGeometry(300, 290, 91, 31)
            self.label2_menu2_price3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_price3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_menu2_price3.setObjectName("label2_menu1_price3")
            ## 라벨 2
            self.label3_menu2_cnt3 = QLabel(self.tab3)
            self.label3_menu2_cnt3.setGeometry(30, 340, 301, 31)
            self.label3_menu2_cnt3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_cnt3.setObjectName("label3_menu1_cnt3")
            self.label3_menu2_price3 = QLabel(self.tab3)
            self.label3_menu2_price3.setGeometry(300, 340, 91, 31)
            self.label3_menu2_price3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_price3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label3_menu2_price3.setObjectName("label3_menu1_price3")
            ## 라벨 3
            self.label4_menu2_cnt3 = QLabel(self.tab3)
            self.label4_menu2_cnt3.setGeometry(30, 390, 301, 31)
            self.label4_menu2_cnt3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_cnt3.setObjectName("label4_menu1_cnt3")
            self.label4_menu2_price3 = QLabel(self.tab3)
            self.label4_menu2_price3.setGeometry(300, 390, 91, 31)
            self.label4_menu2_price3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_price3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label4_menu2_price3.setObjectName("label4_menu1_price3")
            ## 라벨 4
            self.label5_menu2_cnt3 = QLabel(self.tab3)
            self.label5_menu2_cnt3.setGeometry(30, 440, 301, 31)
            self.label5_menu2_cnt3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_cnt3.setObjectName("label5_menu1_cnt")
            self.label5_menu2_price3 = QLabel(self.tab3)
            self.label5_menu2_price3.setGeometry(300, 440, 91, 31)
            self.label5_menu2_price3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_price3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label5_menu2_price3.setObjectName("label5_menu1_price3")
            ## 라벨 5
            self.label6_menu2_cnt3 = QLabel(self.tab3)
            self.label6_menu2_cnt3.setGeometry(30, 490, 301, 31)
            self.label6_menu2_cnt3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_cnt3.setObjectName("label6_menu1_cnt3")
            self.label6_menu2_price3 = QLabel(self.tab3)
            self.label6_menu2_price3.setGeometry(300, 490, 91, 31)
            self.label6_menu2_price3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_price3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label6_menu2_price3.setObjectName("label6_menu1_price3")

            self.label2_progress3 = QLabel(self.tab3)
            self.label2_progress3.setGeometry(QRect(100, 650, 271, 31))
            self.label2_progress3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 13.5pt \"배달의민족 한나체 Air\";")
            self.label2_progress3.setAlignment(Qt.AlignCenter)
            self.label2_progress3.setObjectName("label2_progress3")
            self.label2_totalprice3 = QLabel(self.tab3)
            self.label2_totalprice3.setGeometry(QRect(30, 560, 161, 71))
            self.label2_totalprice3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_totalprice3.setObjectName("label2_totalprice3")
            self.label2_int_totalprice3 = QLabel(self.tab3)
            self.label2_int_totalprice3.setGeometry(QRect(270, 560, 151, 71))
            self.label2_int_totalprice3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "\n"
                                                      "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_int_totalprice3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_int_totalprice3.setObjectName("label2_int_totalprice3")

            self.pushButton2_2_3 = QPushButton(self.tab3)
            self.pushButton2_2_3.setGeometry(290, 690, 131, 41)
            self.pushButton2_2_3.setObjectName("pushButton2_2")
            self.pushButton2_2_3.setText("라이더님 위치 보기")
            self.pushButton2_2_3.clicked.connect(lambda: self.show_ridertab(client))
            self.f5_button3 = QPushButton(self.tab3)
            self.f5_button3.setGeometry(70, 650, 31, 31)
            self.f5_button3.setIcon(QIcon('refresh.png'))
            self.f5_button3.setIconSize(QSize(31, 31))
            self.f5_button3.setObjectName("f5_button3")
            self.f5_button3.clicked.connect(lambda: self.label_3_f5(client, restaurant))
            self.label4_menufirst.setText(
                "{} 외 {}개".format(client.order.menu_arr[0].name, len(client.order.menu_arr) - 1))
            t = time.localtime(client.now)
            self.label4_order_date.setText("주문일시 : {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

            cost = 0
            for i in range(len(client.order.menu_arr)):
                cost += ((client.order.menu_arr[i].price) * client.order.count_arr[i])

            length = len(client.order.menu_arr)

            if length == 1:
                self.label2_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
            elif length == 2:
                self.label2_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
            elif length == 3:
                self.label2_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
            elif length == 4:
                self.label2_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
            elif length > 4:  # textbox의 한계로 메뉴 5개까지만 표시하는 것으로 했습니다.
                self.label2_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
                self.label6_menu2_cnt3.setText(
                    "{} {} 개".format(client.order.menu_arr[4].name, client.order.count_arr[4]))
                self.label6_menu2_price3.setText(
                    "{} 원".format((client.order.menu_arr[4].price) * client.order.count_arr[4]))

            self.label2_progress3.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))
            self.label2_totalprice3.setText("총 주문금액")
            self.label2_int_totalprice3.setText("{} 원".format(cost))

            self.tabUnusing.pop(0)
            self.tabUsing.append(3)

        elif self.tabUnusing[0] == 4:
            self.tabs.addTab(self.tab4, "client number: {}".format(client.key))
            self.label5 = QLabel(self.tab4)
            self.label5.setGeometry(30, 40, 211, 31)
            self.label5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5.setObjectName("label5")
            self.label5.setText("배달이 진행중이에요.")

            self.label5_restaurantname = QLabel(self.tab4)
            self.label5_restaurantname.setGeometry(30, 70, 211, 71)
            self.label5_restaurantname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 25pt \"배달의민족 한나체 Pro\";")
            self.label5_restaurantname.setObjectName("label5_restaurantname")
            self.label5_restaurantname.setText("%s" % (restaurant.name))

            self.label5_menufirst = QLabel(self.tab4)
            self.label5_menufirst.setGeometry(30, 140, 211, 31)
            self.label5_menufirst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menufirst.setObjectName("label5_menufirst")
            self.label5_order_date = QLabel(self.tab4)
            self.label5_order_date.setGeometry(30, 210, 211, 31)
            self.label5_order_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_order_date.setObjectName("label5_order_date")
            ## 라벨 1
            self.label2_menu2_cnt4 = QLabel(self.tab4)
            self.label2_menu2_cnt4.setGeometry(30, 290, 301, 31)
            self.label2_menu2_cnt4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_cnt4.setObjectName("label2_menu1_cnt4")

            self.label2_menu2_price4 = QLabel(self.tab4)
            self.label2_menu2_price4.setGeometry(300, 290, 91, 31)
            self.label2_menu2_price4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_price4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_menu2_price4.setObjectName("label2_menu1_price4")
            ## 라벨 2
            self.label3_menu2_cnt4 = QLabel(self.tab4)
            self.label3_menu2_cnt4.setGeometry(30, 340, 301, 31)
            self.label3_menu2_cnt4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_cnt4.setObjectName("label3_menu1_cnt4")
            self.label3_menu2_price4 = QLabel(self.tab4)
            self.label3_menu2_price4.setGeometry(300, 340, 91, 31)
            self.label3_menu2_price4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_price4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label3_menu2_price4.setObjectName("label3_menu1_price4")
            ## 라벨 3
            self.label4_menu2_cnt4 = QLabel(self.tab4)
            self.label4_menu2_cnt4.setGeometry(30, 390, 301, 31)
            self.label4_menu2_cnt4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_cnt4.setObjectName("label4_menu1_cnt4")
            self.label4_menu2_price4 = QLabel(self.tab4)
            self.label4_menu2_price4.setGeometry(300, 390, 91, 31)
            self.label4_menu2_price4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_price4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label4_menu2_price4.setObjectName("label4_menu1_price4")
            ## 라벨 4
            self.label5_menu2_cnt4 = QLabel(self.tab4)
            self.label5_menu2_cnt4.setGeometry(30, 440, 301, 31)
            self.label5_menu2_cnt4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_cnt4.setObjectName("label5_menu1_cnt4")
            self.label5_menu2_price4 = QLabel(self.tab4)
            self.label5_menu2_price4.setGeometry(300, 440, 91, 31)
            self.label5_menu2_price4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_price4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label5_menu2_price4.setObjectName("label5_menu1_price4")
            ## 라벨 5
            self.label6_menu2_cnt4 = QLabel(self.tab4)
            self.label6_menu2_cnt4.setGeometry(30, 490, 301, 31)
            self.label6_menu2_cnt4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_cnt4.setObjectName("label6_menu1_cnt4")
            self.label6_menu2_price4 = QLabel(self.tab4)
            self.label6_menu2_price4.setGeometry(300, 490, 91, 31)
            self.label6_menu2_price4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_price4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label6_menu2_price4.setObjectName("label6_menu1_price4")

            self.label2_progress4 = QLabel(self.tab4)
            self.label2_progress4.setGeometry(QRect(100, 650, 271, 31))
            self.label2_progress4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 13.5pt \"배달의민족 한나체 Air\";")
            self.label2_progress4.setAlignment(Qt.AlignCenter)
            self.label2_progress4.setObjectName("label2_progress4")
            self.label2_totalprice4 = QLabel(self.tab4)
            self.label2_totalprice4.setGeometry(QRect(30, 560, 161, 71))
            self.label2_totalprice4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_totalprice4.setObjectName("label2_totalprice4")
            self.label2_int_totalprice4 = QLabel(self.tab4)
            self.label2_int_totalprice4.setGeometry(QRect(270, 560, 151, 71))
            self.label2_int_totalprice4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "\n"
                                                      "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_int_totalprice4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_int_totalprice4.setObjectName("label2_int_totalprice4")

            self.pushButton2_2_4 = QPushButton(self.tab4)
            self.pushButton2_2_4.setGeometry(290, 690, 131, 41)
            self.pushButton2_2_4.setObjectName("pushButton2_2_4")
            self.pushButton2_2_4.setText("라이더님 위치 보기")
            self.pushButton2_2_4.clicked.connect(lambda: self.show_ridertab(client))
            self.f5_button4 = QPushButton(self.tab4)
            self.f5_button4.setGeometry(70, 650, 31, 31)
            self.f5_button4.setIcon(QIcon('refresh.png'))
            self.f5_button4.setIconSize(QSize(31, 31))
            self.f5_button4.setObjectName("f5_button4")
            self.f5_button4.clicked.connect(lambda: self.label_4_f5(client, restaurant))
            self.label5_menufirst.setText(
                "{} 외 {}개".format(client.order.menu_arr[0].name, len(client.order.menu_arr) - 1))
            t = time.localtime(client.now)
            self.label5_order_date.setText("주문일시 : {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

            cost = 0
            for i in range(len(client.order.menu_arr)):
                cost += ((client.order.menu_arr[i].price) * client.order.count_arr[i])

            length = len(client.order.menu_arr)

            if length == 1:
                self.label2_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
            elif length == 2:
                self.label2_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
            elif length == 3:
                self.label2_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
            elif length == 4:
                self.label2_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
            elif length > 4:  # textbox의 한계로 메뉴 5개까지만 표시하는 것으로 했습니다.
                self.label2_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
                self.label6_menu2_cnt4.setText(
                    "{} {} 개".format(client.order.menu_arr[4].name, client.order.count_arr[4]))
                self.label6_menu2_price4.setText(
                    "{} 원".format((client.order.menu_arr[4].price) * client.order.count_arr[4]))

            self.label2_progress4.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))
            self.label2_totalprice4.setText("총 주문금액")
            self.label2_int_totalprice4.setText("{} 원".format(cost))

            self.tabUnusing.pop(0)
            self.tabUsing.append(4)

        elif self.tabUnusing[0] == 5:
            self.tabs.addTab(self.tab5, "client number: {}".format(client.key))
            self.label6 = QLabel(self.tab5)
            self.label6.setGeometry(30, 40, 211, 31)
            self.label6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6.setObjectName("label6")
            self.label6.setText("배달이 진행중이에요.")

            self.label6_restaurantname = QLabel(self.tab5)
            self.label6_restaurantname.setGeometry(30, 70, 211, 71)
            self.label6_restaurantname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "\n"
                                                     "font: 25pt \"배달의민족 한나체 Pro\";")
            self.label6_restaurantname.setObjectName("label6_restaurantname")
            self.label6_restaurantname.setText("%s" % (restaurant.name))

            self.label6_menufirst = QLabel(self.tab5)
            self.label6_menufirst.setGeometry(30, 140, 211, 31)
            self.label6_menufirst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menufirst.setObjectName("label6_menufirst")
            self.label6_order_date = QLabel(self.tab5)
            self.label6_order_date.setGeometry(30, 210, 211, 31)
            self.label6_order_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_order_date.setObjectName("label6_order_date")
            ## 라벨 1
            self.label2_menu2_cnt5 = QLabel(self.tab5)
            self.label2_menu2_cnt5.setGeometry(30, 290, 301, 31)
            self.label2_menu2_cnt5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_cnt5.setObjectName("label2_menu1_cnt5")

            self.label2_menu2_price5 = QLabel(self.tab5)
            self.label2_menu2_price5.setGeometry(300, 290, 91, 31)
            self.label2_menu2_price5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label2_menu2_price5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_menu2_price5.setObjectName("label2_menu1_price5")
            ## 라벨 2
            self.label3_menu2_cnt5 = QLabel(self.tab5)
            self.label3_menu2_cnt5.setGeometry(30, 340, 301, 31)
            self.label3_menu2_cnt5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_cnt5.setObjectName("label3_menu1_cnt5")
            self.label3_menu2_price5 = QLabel(self.tab5)
            self.label3_menu2_price5.setGeometry(300, 340, 91, 31)
            self.label3_menu2_price5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label3_menu2_price5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label3_menu2_price5.setObjectName("label3_menu1_price5")
            ## 라벨 3
            self.label4_menu2_cnt5 = QLabel(self.tab5)
            self.label4_menu2_cnt5.setGeometry(30, 390, 301, 31)
            self.label4_menu2_cnt5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_cnt5.setObjectName("label4_menu1_cnt5")
            self.label4_menu2_price5 = QLabel(self.tab5)
            self.label4_menu2_price5.setGeometry(300, 390, 91, 31)
            self.label4_menu2_price5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label4_menu2_price5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label4_menu2_price5.setObjectName("label4_menu1_price5")
            ## 라벨 4
            self.label5_menu2_cnt5 = QLabel(self.tab5)
            self.label5_menu2_cnt5.setGeometry(30, 440, 301, 31)
            self.label5_menu2_cnt5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_cnt5.setObjectName("label5_menu1_cnt5")
            self.label5_menu2_price5 = QLabel(self.tab5)
            self.label5_menu2_price5.setGeometry(300, 440, 91, 31)
            self.label5_menu2_price5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label5_menu2_price5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label5_menu2_price5.setObjectName("label5_menu1_price5")
            ## 라벨 5
            self.label6_menu2_cnt5 = QLabel(self.tab5)
            self.label6_menu2_cnt5.setGeometry(30, 490, 301, 31)
            self.label6_menu2_cnt5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_cnt5.setObjectName("label6_menu1_cnt5")
            self.label6_menu2_price5 = QLabel(self.tab5)
            self.label6_menu2_price5.setGeometry(300, 490, 91, 31)
            self.label6_menu2_price5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "font: 15pt \"배달의민족 한나체 Air\";")
            self.label6_menu2_price5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label6_menu2_price5.setObjectName("label6_menu1_price5")

            self.label2_progress5 = QLabel(self.tab5)
            self.label2_progress5.setGeometry(QRect(100, 650, 271, 31))
            self.label2_progress5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "font: 13.5pt \"배달의민족 한나체 Air\";")
            self.label2_progress5.setAlignment(Qt.AlignCenter)
            self.label2_progress5.setObjectName("label2_progress5")
            self.label2_totalprice5 = QLabel(self.tab5)
            self.label2_totalprice5.setGeometry(QRect(30, 560, 161, 71))
            self.label2_totalprice5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_totalprice5.setObjectName("label2_totalprice5")
            self.label2_int_totalprice5 = QLabel(self.tab5)
            self.label2_int_totalprice5.setGeometry(QRect(270, 560, 151, 71))
            self.label2_int_totalprice5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "\n"
                                                      "font: 20pt \"배달의민족 한나체 Pro\";")
            self.label2_int_totalprice5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            self.label2_int_totalprice5.setObjectName("label2_int_totalprice5")

            self.pushButton2_2_5 = QPushButton(self.tab5)
            self.pushButton2_2_5.setGeometry(290, 690, 131, 41)
            self.pushButton2_2_5.setObjectName("pushButton2_2_5")
            self.pushButton2_2_5.setText("라이더님 위치 보기")
            self.pushButton2_2_5.clicked.connect(lambda: self.show_ridertab(client))
            self.f5_button5 = QPushButton(self.tab5)
            self.f5_button5.setGeometry(70, 650, 31, 31)
            self.f5_button5.setIcon(QIcon('refresh.png'))
            self.f5_button5.setIconSize(QSize(31, 31))
            self.f5_button5.setObjectName("f5_button5")
            self.f5_button5.clicked.connect(lambda: self.label_5_f5(client, restaurant))
            self.label6_menufirst.setText(
                "{} 외 {}개".format(client.order.menu_arr[0].name, len(client.order.menu_arr) - 1))
            t = time.localtime(client.now)
            self.label6_order_date.setText("주문일시 : {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))

            cost = 0
            for i in range(len(client.order.menu_arr)):
                cost += ((client.order.menu_arr[i].price) * client.order.count_arr[i])

            length = len(client.order.menu_arr)

            if length == 1:
                self.label2_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
            elif length == 2:
                self.label2_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
            elif length == 3:
                self.label2_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
            elif length == 4:
                self.label2_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
            elif length > 4:  # textbox의 한계로 메뉴 5개까지만 표시하는 것으로 했습니다.
                self.label2_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[0].name, client.order.count_arr[0]))
                self.label2_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[0].price) * client.order.count_arr[0]))
                self.label3_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[1].name, client.order.count_arr[1]))
                self.label3_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[1].price) * client.order.count_arr[1]))
                self.label4_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[2].name, client.order.count_arr[2]))
                self.label4_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[2].price) * client.order.count_arr[2]))
                self.label5_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[3].name, client.order.count_arr[3]))
                self.label5_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[3].price) * client.order.count_arr[3]))
                self.label6_menu2_cnt5.setText(
                    "{} {} 개".format(client.order.menu_arr[4].name, client.order.count_arr[4]))
                self.label6_menu2_price5.setText(
                    "{} 원".format((client.order.menu_arr[4].price) * client.order.count_arr[4]))

            self.label2_progress5.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))
            self.label2_totalprice5.setText("총 주문금액")
            self.label2_int_totalprice5.setText("{} 원".format(cost))

            self.tabUnusing.pop(0)
            self.tabUsing.append(5)

    def remove_tab(self, index):

        self.tabUnusing.append(self.tabUsing.pop(index - 1))
        self.tabs.removeTab(index - 1)
        self.tabcount -= 1
        print(self.tabUsing, self.tabUnusing)

    def show_ridertab(self, client):
        global riderwayclient
        riderwayclient = client
        print(client.rider.way)
        mywindow_riderway.show()

    def label_1_f5(self, client, restaurant):
        self.label2_progress.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))

    def label_2_f5(self, client, restaurant):
        self.label2_progress2.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))

    def label_3_f5(self, client, restaurant):
        self.label2_progress3.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))

    def label_4_f5(self, client, restaurant):
        self.label2_progress4.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))

    def label_5_f5(self, client, restaurant):
        self.label2_progress5.setText("기사님 도착까지 남은 시간 : {} 분".format(int(restaurant.remain(client))))


class WindowClass_complete(QMainWindow, form_complete):
    def __init__(self, complete):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.complete = complete

        self.btn_f5.setIcon(QIcon('refresh.png'))
        self.btn_f5.setIconSize(QSize(31, 31))
        self.btn_f5.clicked.connect(self.f5_clicked)

    def f5_clicked(self):
        tmp = self.complete.head
        if self.complete.size == 1:
            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum1.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime1.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace1.setText("음식점: {}".format(place))
            self.ordermenu1.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))
        elif self.complete.size == 2:
            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum1.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime1.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace1.setText("음식점: {}".format(place))
            self.ordermenu1.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum2.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime2.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace2.setText("음식점: {}".format(place))
            self.ordermenu2.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

        elif self.complete.size == 3:
            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum1.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime1.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace1.setText("음식점: {}".format(place))
            self.ordermenu1.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum2.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime2.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace2.setText("음식점: {}".format(place))
            self.ordermenu2.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum3.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime3.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace3.setText("음식점: {}".format(place))
            self.ordermenu3.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

        elif self.complete.size == 4:
            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum1.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime1.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace1.setText("음식점: {}".format(place))
            self.ordermenu1.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum2.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime2.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace2.setText("음식점: {}".format(place))
            self.ordermenu2.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum3.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime3.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace3.setText("음식점: {}".format(place))
            self.ordermenu3.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum4.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime4.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace4.setText("음식점: {}".format(place))
            self.ordermenu4.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

        elif self.complete.size >= 5:
            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum1.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime1.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace1.setText("음식점: {}".format(place))
            self.ordermenu1.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum2.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime2.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace2.setText("음식점: {}".format(place))
            self.ordermenu2.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum3.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime3.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace3.setText("음식점: {}".format(place))
            self.ordermenu3.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum4.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime4.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace4.setText("음식점: {}".format(place))
            self.ordermenu4.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))

            tmp = tmp.next

            t = time.localtime(tmp.data.now)
            place = point_int_to_name(tmp.data.delay)
            self.ordernum5.setText("주문번호: {}".format(tmp.data.key))
            self.ordertime5.setText("주문일시: {}/{} {}시 {}분".format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
            self.orderplace5.setText("음식점: {}".format(place))
            self.ordermenu5.setText(
                "{} 외 {}개".format(tmp.data.order.menu_arr[0].name, len(tmp.data.order.menu_arr) - 1))



class WindowClass_menu(QMainWindow, form_menu_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.chungzik.clicked.connect(self.chunggik_click)
        self.bhc.clicked.connect(self.bhc_click)
        self.sinjeon.clicked.connect(self.sinjeon_click)
        self.datti.clicked.connect(self.datti_clicK)
        self.galli.clicked.connect(self.galli_click)
        self.yooksudang.clicked.connect(self.yooksudang_click)
        self.burgerpark.clicked.connect(self.burgerpark_click)
        self.goobne.clicked.connect(self.goobne_click)
        self.burgerking.clicked.connect(self.burgerking_click)
        self.hongkong.clicked.connect(self.hongkong_click)
        self.juk.clicked.connect(self.juk_click)
        self.phongon.clicked.connect(self.phongon_click)

    def chunggik_click(self):
        mywindow_chungzik.show()

    def bhc_click(self):
        mywindow_bhc.show()

    def sinjeon_click(self):
        mywindow_singeon.show()

    def datti_clicK(self):
        mywindow_ddatti.show()

    def galli_click(self):
        mywindow_galli.show()

    def yooksudang_click(self):
        mywindow_yooksudang.show()

    def burgerpark_click(self):
        mywindow_burgerpark.show()

    def goobne_click(self):
        mywindow_goobne.show()

    def burgerking_click(self):
        mywindow_burgerking.show()

    def hongkong_click(self):
        mywindow_hongkongbanjeom.show()

    def juk_click(self):
        mywindow_jukstory.show()

    def phongon_click(self):
        mywindow_phongon.show()


class WindowClass_main(QMainWindow, form_class_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btn_location.clicked.connect(self.location_check)
        self.btn_order.clicked.connect(self.my_order)
        self.btn_res.clicked.connect(self.go_restaurant)
        self.btn_complete.clicked.connect(self.complete)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))

        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)

        self.pushButton.setIcon(QIcon('button.PNG'))
        self.pushButton.setIconSize(QSize(22, 22))
        self.pushButton_2.setIcon(QIcon('button.PNG'))
        self.pushButton_2.setIconSize(QSize(22, 22))
        self.pushButton_3.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_3.setIconSize(QSize(22, 22))
        self.pushButton_4.setIcon(QIcon('button.PNG'))
        self.pushButton_4.setIconSize(QSize(22, 22))
        self.pushButton_5.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_5.setIconSize(QSize(22, 22))
        self.pushButton_6.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_6.setIconSize(QSize(22, 22))
        self.pushButton_7.setIcon(QIcon('button.PNG'))
        self.pushButton_7.setIconSize(QSize(22, 22))
        self.pushButton_8.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_8.setIconSize(QSize(22, 22))
        self.pushButton_9.setIcon(QIcon('button.PNG'))
        self.pushButton_9.setIconSize(QSize(22, 22))
        self.pushButton_10.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_10.setIconSize(QSize(22, 22))
        self.pushButton_11.setIcon(QIcon('button.PNG'))
        self.pushButton_11.setIconSize(QSize(22, 22))
        self.pushButton_12.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_12.setIconSize(QSize(22, 22))
        self.pushButton_13.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_13.setIconSize(QSize(22, 22))
        self.pushButton_14.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_14.setIconSize(QSize(22, 22))
        self.pushButton_15.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_15.setIconSize(QSize(22, 22))
        self.pushButton_16.setIcon(QIcon('button.PNG'))
        self.pushButton_16.setIconSize(QSize(22, 22))
        self.pushButton_17.setIcon(QIcon('button.PNG'))
        self.pushButton_17.setIconSize(QSize(22, 22))
        self.pushButton_18.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_18.setIconSize(QSize(22, 22))
        self.pushButton_19.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_19.setIconSize(QSize(22, 22))
        self.pushButton_20.setIcon(QIcon('button.PNG'))
        self.pushButton_20.setIconSize(QSize(22, 22))
        self.pushButton_21.setIcon(QIcon('button.PNG'))
        self.pushButton_21.setIconSize(QSize(22, 22))
        self.pushButton_22.setIcon(QIcon('button.PNG'))
        self.pushButton_22.setIconSize(QSize(22, 22))
        self.pushButton_23.setIcon(QIcon('Rbutton.PNG'))
        self.pushButton_23.setIconSize(QSize(22, 22))

        self.pushButton.clicked.connect(self.func_btn1_clicked)
        self.pushButton_2.clicked.connect(self.func_btn2_clicked)
        self.pushButton_3.clicked.connect(self.func_btn3_clicked)
        self.pushButton_4.clicked.connect(self.func_btn4_clicked)
        self.pushButton_5.clicked.connect(self.func_btn5_clicked)
        self.pushButton_6.clicked.connect(self.func_btn6_clicked)
        self.pushButton_7.clicked.connect(self.func_btn7_clicked)
        self.pushButton_8.clicked.connect(self.func_btn8_clicked)
        self.pushButton_9.clicked.connect(self.func_btn9_clicked)
        self.pushButton_10.clicked.connect(self.func_btn10_clicked)
        self.pushButton_11.clicked.connect(self.func_btn11_clicked)
        self.pushButton_12.clicked.connect(self.func_btn12_clicked)
        self.pushButton_13.clicked.connect(self.func_btn13_clicked)
        self.pushButton_14.clicked.connect(self.func_btn14_clicked)
        self.pushButton_15.clicked.connect(self.func_btn15_clicked)
        self.pushButton_16.clicked.connect(self.func_btn17_clicked)
        self.pushButton_17.clicked.connect(self.func_btn13_clicked)
        self.pushButton_18.clicked.connect(self.func_btn18_clicked)
        self.pushButton_19.clicked.connect(self.func_btn19_clicked)
        self.pushButton_20.clicked.connect(self.func_btn20_clicked)
        self.pushButton_21.clicked.connect(self.func_btn21_clicked)
        self.pushButton_22.clicked.connect(self.func_btn22_clicked)
        self.pushButton_23.clicked.connect(self.func_btn23_clicked)

        # 프로그램 종료

    def func_btn1_clicked(self):
        global clientpos
        clientpos = 1
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn2_clicked(self):
        global clientpos
        clientpos = 2
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn3_clicked(self):
        global clientpos
        clientpos = 3
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn4_clicked(self):
        global clientpos
        clientpos = 4
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn5_clicked(self):
        global clientpos
        clientpos = 5
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn6_clicked(self):
        global clientpos
        clientpos = 6
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn7_clicked(self):
        global clientpos
        clientpos = 7
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn8_clicked(self):
        global clientpos
        clientpos = 8
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn9_clicked(self):
        global clientpos
        clientpos = 9
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn10_clicked(self):
        global clientpos
        clientpos = 10
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn11_clicked(self):
        global clientpos
        clientpos = 11
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn12_clicked(self):
        global clientpos
        clientpos = 12
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn13_clicked(self):
        global clientpos
        clientpos = 13
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn14_clicked(self):
        global clientpos
        clientpos = 14
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn15_clicked(self):
        global clientpos
        clientpos = 15
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn16_clicked(self):
        global clientpos
        clientpos = 16
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn17_clicked(self):
        global clientpos
        clientpos = 17
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn18_clicked(self):
        global clientpos
        clientpos = 18
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn19_clicked(self):
        global clientpos
        clientpos = 19
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn20_clicked(self):
        global clientpos
        clientpos = 20
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn21_clicked(self):
        global clientpos
        clientpos = 21
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn22_clicked(self):
        global clientpos
        clientpos = 22
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def func_btn23_clicked(self):
        global clientpos
        clientpos = 23
        QMessageBox.about(self, "위치", "위치가 {}(으)로 선택되었습니다.".format(point_int_to_name(clientpos)))

    def closeEvent(self, event):
        close_btn = QMessageBox.question(self, "Close", "정말 종료하시겠습니까?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Yes)
        if close_btn == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def location_check(self):
        if clientpos == -1:
            QMessageBox.about(self, "Warning!", "위치를 선택해주세요.")
        else:
            ml = point_int_to_name(clientpos)
            QMessageBox.about(self, "My location", "현재 위치는 {}입니다.".format(ml))

    def go_restaurant(self):
        if clientpos == -1:
            QMessageBox.about(self, "Warning!", "위치를 선택해주세요.")
        else:
            mywindow_menu.show()

    def my_order(self):
        if clientpos == -1:
            QMessageBox.about(self, "Warning!", "위치를 선택해주세요.")
        else:
            mywindow_myorder.show()

    def complete(self):
        if clientpos == -1:
            QMessageBox.about(self, "Warning!", "위치를 선택해주세요.")
        else:
            mywindow_complete.f5_clicked()
            mywindow_complete.show()

    def exit_program(self):
        QCoreApplication.instance().quit()


class WindowClass_login(QMainWindow, form_class_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btn_login.clicked.connect(self.login_Func)
        self.btn_easter.clicked.connect(self.eater_egg_func)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))
        self.ID_text = ''
        self.pw_text = ''

    def login_Func(self):
        QMessageBox.about(self, "로그인", "로그인되었습니다!!")
        QMessageBox.about(self, "위치", "위치를 선택해주세요!")
        self.destroy()
        mywindow_main.show()

    def eater_egg_func(self):
        QMessageBox.about(self, "김승일", "이랬는데 A+ 못받는다? 아 ㅋㅋ")
        QMessageBox.about(self, "이동섭", "2020 6/1~6/8 이동섭의 영혼 여기에 잠들다..")
        QMessageBox.about(self, "정유찬", "정유찬님 버튼싸개로 전직하셨습니다.")



class WindowClass_start(QMainWindow, form_start_app):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btn_1.clicked.connect(self.startbtn_Func)
        self.setWindowTitle("명륜당에 짜장하나요")
        self.setWindowIcon(QIcon("라이더.png"))

    def startbtn_Func(self):
        self.destroy()
        mywindow_login.show()


def dijsktra(graph, start, end):
    if start == end:
        way = LinkedList()
        way.insert(start)
        info = Return_Way_Distance(way, 0)
        return info

    distance = [None] * 24
    check = [None] * 24
    back_of_distance = [None] * 24

    for i in range(0, 24, 1):
        distance[i] = INFINITE
        check[i] = 0

    distance[start] = 0
    cycle = 0
    now = -1

    while (cycle < 23 - 1):
        min = INFINITE
        for i in range(0, 24, 1):
            if distance[i] < min and check[i] == 0:
                min = distance[i]
                now = i
        check[now] = 1
        tmp = graph.Map[now]

        while tmp != None:
            if check[tmp.number] == 0 and (min + tmp.distance) < distance[tmp.number]:
                distance[tmp.number] = min + tmp.distance
                back_of_distance[tmp.number] = now

            tmp = tmp.next

        cycle += 1
        if now == end:
            break

    tmp = Stack()

    k = end
    while True:
        j = back_of_distance[k]
        if j == start:
            break
        tmp.push(j)
        k = j

    way = LinkedList()

    way.insert(start)

    while tmp.size != 0:
        way.insert(tmp.pop())

    way.insert(end)

    info = Return_Way_Distance(way, distance[end])

    # print("{} 부터 {} 까지의 최단거리 = {}\n".format(start, end, distance[end]))

    return info


def find_rider(graph, riders, restaurant_position):
    if riders.rider1.delivery_OnOff == 1 and riders.rider2.delivery_OnOff == 1 and riders.rider3.delivery_OnOff == 1 and riders.rider4.delivery_OnOff == 1 and riders.rider5.delivery_OnOff == 1:
        # 배달이 불가능합니다
        return

    availabe_riders = []
    availabe_riders_info = []

    rider1info = dijsktra(graph, riders.rider1.position, restaurant_position)
    rider2info = dijsktra(graph, riders.rider2.position, restaurant_position)
    rider3info = dijsktra(graph, riders.rider3.position, restaurant_position)
    rider4info = dijsktra(graph, riders.rider4.position, restaurant_position)
    rider5info = dijsktra(graph, riders.rider5.position, restaurant_position)

    if riders.rider1.delivery_OnOff == 0:
        availabe_riders.append(riders.rider1)
        availabe_riders_info.append(rider1info)
    if riders.rider2.delivery_OnOff == 0:
        availabe_riders.append(riders.rider2)
        availabe_riders_info.append(rider2info)
    if riders.rider3.delivery_OnOff == 0:
        availabe_riders.append(riders.rider3)
        availabe_riders_info.append(rider3info)
    if riders.rider4.delivery_OnOff == 0:
        availabe_riders.append(riders.rider4)
        availabe_riders_info.append(rider4info)
    if riders.rider5.delivery_OnOff == 0:
        availabe_riders.append(riders.rider5)
        availabe_riders_info.append(rider5info)

    shortest_rider = availabe_riders[0]
    j = 0

    i = 1
    while i < len(availabe_riders):
        if availabe_riders_info[i].distance < availabe_riders_info[j].distance:
            shortest_rider = availabe_riders[i]
            j = i
        i += 1

    shortest_rider.restaurant = restaurant_position
    shortest_rider.delivery_OnOff = 1
    return shortest_rider


def total_way(rtr, rtd):
    totalway = rtr.way

    rtd.way.delete_first()

    while True:
        dd = rtd.way.delete_first()
        if dd == -1:
            break
        totalway.insert(dd)

    return totalway


def point_int_to_name(num):
    if num == 1:
        return "성균관대학교"
    elif num == 2:
        return "양현관"
    elif num == 3:
        return "청춘직화"
    elif num == 4:
        return "새마을금고"
    elif num == 5:
        return "bhc 종로성대점"
    elif num == 6:
        return "신전떡볶이"
    elif num == 7:
        return "명륜 아남아파트"
    elif num == 8:
        return "포응온 (서울과학고등학교)"
    elif num == 9:
        return "혜화동 로터리"
    elif num == 10:
        return "따띠삼겹 (성대 앞 사거리)"
    elif num == 11:
        return "한국예술종합학교 대학로 캠퍼스"
    elif num == 12:
        return "깔리"
    elif num == 13:
        return "버거파크"
    elif num == 14:
        return "육수당"
    elif num == 15:
        return "버거킹"
    elif num == 16:
        return "혜화역 1번출구"
    elif num == 17:
        return "혜화역 2번출구"
    elif num == 18:
        return "홍콩반점"
    elif num == 19:
        return "죽 이야기 (서울대학교 병원)"
    elif num == 20:
        return "마로니에 공원"
    elif num == 21:
        return "서울대학교사범대 부설 초등학교"
    elif num == 22:
        return "한성대입구역 1번출구"
    elif num == 23:
        return "굽네치킨 한성대점"
    else:
        return "미확인 지역"


def int_to_restaurant(restaurant_position, restaurants):
    return restaurants[restaurant_position]


chungzik_ggamang = Menu("까망직화불백정식", 7500, 5)  # delay는 음식 제작 시간으로, 분단위로 작성합니다. 대충 추정해서 5분~20분 내에서 골라주세요
chungzik_bbalgang = Menu("빨강직화불백정식", 7500, 6)

chungzik_menu = []
chungzik_menu.append(chungzik_ggamang)
chungzik_menu.append(chungzik_bbalgang)

chungzik = Restaurant("청춘직화", 3, chungzik_menu)

bhc_goldking = Menu("골드킹콤보", 18000, 13)
bhc_redking = Menu("레드킹콤보", 18000, 13)
bhc_bburing = Menu("뿌링클콤보", 18000, 14)
bhc_machoking = Menu("마초킹콤보", 18000, 12)

bhc_menu = []
bhc_menu.append(bhc_goldking)
bhc_menu.append(bhc_redking)
bhc_menu.append(bhc_bburing)
bhc_menu.append(bhc_machoking)

bhc = Restaurant("bhc", 5, bhc_menu)

sinjeon_tteokbokki = Menu("떡볶이", 3000, 6)
sinjeon_cheese_ttekbokki = Menu("치즈떡볶이", 4000, 7)
sinjeon_gimbap = Menu("신전김밥", 2000, 4)
sinjeon_spammayo = Menu("스팸마요컵밥", 3500, 7)
sinjeon_chamchimayo = Menu("참치마요컴밥", 3500, 7)

sinjeon_menu = []
sinjeon_menu.append(sinjeon_tteokbokki)
sinjeon_menu.append(sinjeon_cheese_ttekbokki)
sinjeon_menu.append(sinjeon_gimbap)
sinjeon_menu.append(sinjeon_spammayo)
sinjeon_menu.append(sinjeon_chamchimayo)

sinjeon = Restaurant("신전떡볶이", 6, sinjeon_menu)

ddatti_simple_double = Menu("간단삼겹곱배기", 4800, 10)
ddatti_simple_meat = Menu("간단삼겹고기만", 6500, 12)
ddatti_simple_original = Menu("간단삼겹기본", 2900, 8)
ddatti_bap = Menu("공기밥", 1000, 1)

ddatti_menu = []
ddatti_menu.append(ddatti_simple_double)
ddatti_menu.append(ddatti_simple_meat)
ddatti_menu.append(ddatti_simple_original)
ddatti_menu.append(ddatti_bap)

datti = Restaurant("따띠삼겹", 10, ddatti_menu)

galli_aset = Menu("깔리 A세트", 26000, 17)
galli_saecurry = Menu("새우 커리", 12000, 15)
galli_saecorma = Menu("새우 코르마", 12000, 15)
galli_yangma = Menu("양고기 마살라", 12000, 16)
galli_yangbin = Menu("양고기 빈달루", 12000, 16)

galli_menu = []
galli_menu.append(galli_aset)
galli_menu.append(galli_saecurry)
galli_menu.append(galli_saecorma)
galli_menu.append(galli_yangma)
galli_menu.append(galli_yangbin)

galli = Restaurant("깔리", 12, galli_menu)

yooksudang_sundae = Menu("서울촌놈 순대국밥", 6500, 5)
yooksudang_suyook = Menu("든든한끼 수육국밥", 6500, 5)
yooksudang_ttarou = Menu("얼큰시원 따로국밥", 6500, 6)
yooksudang_kimchi = Menu("김치짜글전골", 18000, 8)
yooksudang_gogifry = Menu("파듬뿍 고기튀김", 12000, 10)

yooksudang_menu = []
yooksudang_menu.append(yooksudang_sundae)
yooksudang_menu.append(yooksudang_suyook)
yooksudang_menu.append(yooksudang_ttarou)
yooksudang_menu.append(yooksudang_kimchi)
yooksudang_menu.append(yooksudang_gogifry)

yooksudang = Restaurant("육수당", 14, yooksudang_menu)

burgerpark_bacon = Menu("베이컨치즈버거", 6900, 9)
burgerpark_avocado = Menu("아보카도치즈버거", 7900, 11)
burgerpark_cheese = Menu("치즈버거", 5900, 8)
burgerpark_mushroom = Menu("머쉬룸치즈버거", 6900, 10)
burgerpark_shrimp = Menu("쉬림프치즈버거", 7900, 12)

burgerpark_menu = []
burgerpark_menu.append(burgerpark_bacon)
burgerpark_menu.append(burgerpark_avocado)
burgerpark_menu.append(burgerpark_cheese)
burgerpark_menu.append(burgerpark_mushroom)
burgerpark_menu.append(burgerpark_shrimp)

burgerpark = Restaurant("버거파크", 13, burgerpark_menu)

hongkongbanjeom_jjajangmeon = Menu("짜장면", 4500, 7)
hongkongbanjeom_jjambbong = Menu("짬뽕", 5500, 6)
hongkongbanjeom_jjajangbab = Menu("짜장밥", 6500, 6)
hongkongbanjeom_jjambbongbab = Menu("짬뽕밥", 6000, 5)
hongkongbanjeom_tangsuyooksmall = Menu("탕수육 소", 9500, 9)
hongkongbanjeom_tangsuyookbig = Menu("탕수육 대", 15000, 11)

hongkongbanjeom_menu = []
hongkongbanjeom_menu.append(hongkongbanjeom_jjajangmeon)
hongkongbanjeom_menu.append(hongkongbanjeom_jjambbong)
hongkongbanjeom_menu.append(hongkongbanjeom_jjajangbab)
hongkongbanjeom_menu.append(hongkongbanjeom_jjambbongbab)
hongkongbanjeom_menu.append(hongkongbanjeom_tangsuyooksmall)
hongkongbanjeom_menu.append(hongkongbanjeom_tangsuyookbig)

hongkongbanjeom = Restaurant("홍콩반점", 18, hongkongbanjeom_menu)
jukstory_junbok = Menu("전복죽", 12000, 10)
jukstory_samsunjjambbong = Menu("삼선짬뽕죽", 9500, 13)
jukstory_bulnak = Menu("불낙죽(순한맛)", 9500, 12)
jukstory_maesaeng = Menu("매생이굴죽", 9000, 11)

goobne_galbi = Menu("굽네 갈비천왕", 17000, 15)
goobne_maravolcano = Menu("굽네마라볼케이노", 18000, 15)
goobne_honeymello = Menu("굽네 허니멜로", 18000, 15)
goobne_original = Menu("굽네 오리지널", 15000, 12)
goobne_gochu = Menu("굽네 고추바사삭", 16000, 14)

phoNgon_jikhwa = Menu("직화 쌀국수", 10000, 6)
phoNgon_bunjja = Menu("분보샤오(소고기 분짜)", 13000, 8)
phoNgon_yangji = Menu("양지 쌀국수", 9000, 7)
phoNgon_chadol = Menu("차돌박이 쌀국수", 11000, 8)

burgerking_Whopper = Menu("와퍼세트", 7900, 6)
burgerking_cheezeWhopper = Menu("치즈와퍼세트", 8500, 7)
burgerking_quatrocheezeWhopper = Menu("콰트로치즈와퍼세트", 8800, 7)
burgerking_shrimpstake = Menu("통새우스테이크버거세트", 9900, 7)
burgerking_Whopper_jr = Menu("와퍼주니어세트", 6300, 5)

jukstory_menu = []
jukstory_menu.append(jukstory_junbok)
jukstory_menu.append(jukstory_samsunjjambbong)
jukstory_menu.append(jukstory_bulnak)
jukstory_menu.append(jukstory_maesaeng)

goobne_menu = []
goobne_menu.append(goobne_galbi)
goobne_menu.append(goobne_maravolcano)
goobne_menu.append(goobne_honeymello)
goobne_menu.append(goobne_original)
goobne_menu.append(goobne_gochu)

phoNgon_menu = []
phoNgon_menu.append(phoNgon_jikhwa)
phoNgon_menu.append(phoNgon_bunjja)
phoNgon_menu.append(phoNgon_yangji)
phoNgon_menu.append(phoNgon_chadol)

burgerking_menu = []
burgerking_menu.append(burgerking_Whopper)
burgerking_menu.append(burgerking_cheezeWhopper)
burgerking_menu.append(burgerking_quatrocheezeWhopper)
burgerking_menu.append(burgerking_shrimpstake)
burgerking_menu.append(burgerking_Whopper_jr)

jukstory = Restaurant("죽이야기", 19, jukstory_menu)
goobne = Restaurant("굽네치킨", 23, goobne_menu)
phoNgon = Restaurant("포응온", 8, phoNgon_menu)
burgerking = Restaurant("버거킹", 15, burgerking_menu)

RestaurantS = [None] * 24
RestaurantS[3] = chungzik
RestaurantS[5] = bhc
RestaurantS[6] = sinjeon
RestaurantS[8] = phoNgon
RestaurantS[10] = datti
RestaurantS[12] = galli
RestaurantS[13] = burgerpark
RestaurantS[14] = yooksudang
RestaurantS[15] = burgerking
RestaurantS[18] = hongkongbanjeom
RestaurantS[19] = jukstory
RestaurantS[23] = goobne

riders = Riders()
graph = Graph()
my_order = Order()
clients = Clients(RestaurantS)
complete = LinkedList()

'''
print(riders.rider1.position)
print(riders.rider2.position)
print(riders.rider3.position)
graph = Graph()
my_order = Order()
my_order.add_order(chungzik.menu[0], 2)
client = Client(my_order, 23)
chungzik.make_delivery(client, graph, riders)

th1 = threading.Thread(target=chungzik.cook, args=())
th1.start()

th2 = threading.Thread(target=client.rider.update_pos, args=(graph,))
th2.start()

print(chungzik.queue[0].order.menu_arr[0].name)
print(client.rider.way)

print(int(chungzik.remain(client)))
time.sleep(5)
print(client.rider.position)
'''

app = QApplication(sys.argv)
mywindow_start = WindowClass_start()
mywindow_login = WindowClass_login()
mywindow_main = WindowClass_main()
mywindow_menu = WindowClass_menu()
mywindow_complete = WindowClass_complete(complete)
mywindow_myorder = WindowClass_myOrder(clients, RestaurantS)
mywindow_riderway = Windowclass_riderway()

mywindow_chungzik = WindowClass_chungzik(chungzik, clients, graph, riders, mywindow_myorder)
mywindow_bhc = WindowClass_bhc(bhc, clients, graph, riders, mywindow_myorder)
mywindow_singeon = WindowClass_sinjeon(sinjeon, clients, graph, riders, mywindow_myorder)
mywindow_ddatti = WindowClass_ddatti(datti, clients, graph, riders, mywindow_myorder)
mywindow_galli = WindowClass_galli(galli, clients, graph, riders, mywindow_myorder)
mywindow_yooksudang = WindowClass_yooksudang(yooksudang, clients, graph, riders, mywindow_myorder)
mywindow_burgerpark = WindowClass_burgerpark(burgerpark, clients, graph, riders, mywindow_myorder)
mywindow_hongkongbanjeom = WindowClass_hongkongbanjeom(hongkongbanjeom, clients, graph, riders, mywindow_myorder)
mywindow_jukstory = WindowClass_jukstory(jukstory, clients, graph, riders, mywindow_myorder)
mywindow_phongon = WindowClass_phongon(phoNgon, clients, graph, riders, mywindow_myorder)
mywindow_goobne = WindowClass_goobne(goobne, clients, graph, riders, mywindow_myorder)
mywindow_burgerking = WindowClass_burgerking(burgerking, clients, graph, riders, mywindow_myorder)

# 첫화면

mywindow_start.show()
app.exec_()
