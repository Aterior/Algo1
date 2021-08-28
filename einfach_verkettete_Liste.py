class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        else:
            self.head = new_node

    def search(self, search_data):
        temp_node = self.head
        if temp_node.data == search_data:
            return temp_node
        else:
            while temp_node:
                if temp_node.next.data == search_data:
                    return temp_node
                temp_node = temp_node.next
        return None

    def delete(self, del_value):
        temp_node = self.search(del_value)
        if temp_node:
            if temp_node.next:
                del_temp_node = temp_node.next

                if del_temp_node.next:
                    temp_node.next = del_temp_node.next
                else:
                    temp_node.next = None

                del_temp_node.data = None
                del_temp_node.next = None
            else:
                temp_node.data = None
                temp_node.next = None

            print("Der Knoten mit dem Wert ", del_value, " wurde gelöscht.")
        else:
            print("Der Knoten mit dem Wert ", del_value, "existiert nicht!")

    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print("None")


if __name__ =='__main__':
    linked_list = LinkedList()

    while True:
        x = input("Knoten eingeben: (z.B.: ins 10), Knoten löschen: (z.B.: del 10), display, "
                  "Knoten suchen: (z.B.: sea 10), quit")
        if x == "quit":
            break
        elif x == "display":
            linked_list.display()
        elif x[:3] == "ins" or x[:3] == "del" or x[:3] == "sea":
            x = x.split(" ")
            if x[0] == "ins":
                linked_list.insert(Node(x[1]))
            elif x[0] == "del":
                linked_list.delete(x[1])
            elif x[0] == "sea":
                linked_list.search(x[1])
            else:
                print("Unmöglicher Fehler")
        else:
            print("Kein zulässiger Command!")
