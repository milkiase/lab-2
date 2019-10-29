class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, node):
        temp = self.head
        node.next=temp
        self.head=node
        del temp

    def insertEnd(self,node):
        if self.head is None:
            self.head=node
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next=node
            del lastNode
    def insert(self, node):
        size = self.return_size()
        if self.head is None:
            self.insertHead(node)
        elif self.head.data > node.data:
            self.insertHead(node)
        else:
            temp=self.head
            while temp.data < node.data:
                if temp.next is None:
                    self.insertEnd(node)
                    return
                previous_node = temp
                temp=temp.next
            node.next=temp
            previous_node.next=node
            del temp,previous_node,node

    def del_end(self):
        temp=self.head
        previous_node=""
        while temp.next is not None:
            previous_node=temp
            temp=temp.next
        previous_node.next=None
        del temp
    def del_head(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        del temp
    def delete(self, node):
        if self.head.data is node.data:
            self.del_head()
        else:
            temp = self.head
            while temp.data is not node.data :
                previous_node = temp
                temp = temp.next
                if temp is None:
                    print("The node doesn't exist")
                    return
            previous_node.next=temp.next
            temp.next = None
            del temp
    def return_size(self):
        i=0
        current_node=self.head
        while current_node is not None:
            current_node=current_node.next
            i+=1
        return i
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
def concat(list1,list2):
    temp1=list1.head
    temp2=list2.head
    if temp1 is None:
        list1.head=list2.head
    else:
        while temp1.next is not None:
            temp1=temp1.next
        else:
            temp1.next=temp2
    return list1
FIT_list = LinkedList()
#Hagos is the first comer student for the registration. He is registered on October 30, 2018 at 8:40.
# Thus, create a linked list that contains Hagos’s system assigned ID number = 825

hagos=Node(825)
FIT_list.insertHead(hagos)

# Birhan was with Hagos, of course, she registered the same day at 8:55. The system assigned her
# an ID number = 297

Birhan=Node(297)
FIT_list.insertHead(Birhan)

# Tsige has arrived at 9:00 of the same day and registered at 9:10 with system generated ID = 406
Tsige = Node(406)
FIT_list.insert(Tsige)

# Bahta is registered after two days on November 1, 2018 at 10:00 with system generated ID
# number = 331
Bahta = Node(331)
FIT_list.insert(Bahta)
# E. Birhan, whose ID number is FID/19900621-T297/11 got a scholarship opportunity to MIT Mekelle
# Institute of Technology. As a result, she left FID on November 1, 2018 at 12:00, thus, the institute
# (FID) removed her from the list of students of this academic year.
FIT_list.delete(Birhan)
# F. Tsedal arrived on November 1, 2018 at 14:30 (after noon) and registered with the system
# generated new ID number = 527
Tsedal = Node(527)
FIT_list.insert(Tsedal)
# G. Kiros, Girmay, and Selam with IDs 544, 983, and 201 respectively transferred from Humera
# campus of the same university to Mekelle campus. As a result, their short list is added to the
# students list in Mekelle campus.
humera_campus = LinkedList()
Kiros = Node(544)
Girmay = Node(983)
Selam=Node(201)
humera_campus.insert(Kiros)
humera_campus.insert(Girmay)
humera_campus.insert(Selam)
mu=LinkedList()
mu=concat(mu,humera_campus)
humera_campus.delete(Kiros)
humera_campus.delete(Girmay)
humera_campus.delete(Selam)
# H. Meanwhile, after classes started, Selam returned to her home city, Humera to peruse her study
# at Humera campus of FID.
mu.delete(Selam)
humera_campus.insert(Selam)
# I. A late registered student, Hadgay with system generated ID number = 390 joined the class after
# two weeks.  
Hadgay = Node(390)
FIT_list.insert(Hadgay)
FIT_list.print_list()
# humera_campus.print_list()
