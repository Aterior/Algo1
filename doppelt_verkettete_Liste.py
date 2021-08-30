class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def search(self, search_data):
        temp_node = self.head
        while temp_node:
            if temp_node.data == search_data:
                return temp_node
            temp_node = temp_node.next
        return None

    def delete(self, del_data):
        temp_node = self.search(del_data)
        if temp_node:
            if not temp_node.prev:
                temp_node.next.prev = None
                self.head = temp_node.next
                temp_node.next = None
                temp_node.data = None
            elif not temp_node.next:
                temp_node.prev.next = None
                temp_node.prev = None
                temp_node.data = None
            else:
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev
                temp_node.next = None
                temp_node.prev = None
                temp_node.data = None

            print("Der Knoten mit dem Wert", del_data, "wurde gelöscht.")
        else:
            print("Der Knoten mit dem Wert", del_data, "existiert nicht!")

    def display(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print("None")


if __name__ == '__main__':
    linked_list = LinkedList()

    while True:
        x = input("Knoten eingeben: (z.B.: ins 10), Knoten löschen: (z.B.: del 10), display, "
                  "Knoten suchen: (z.B.: sea 10), quit, seehead")
        if x == "quit":
            break
        elif x == "display":
            linked_list.display()
        elif x == "seehead":
            if linked_list.head.data:
                print("self.head.data:", linked_list.head.data)
            else:
                print("self.head.data: None")

            if linked_list.head.next:
                print("self.head.next.data:", linked_list.head.next.data)
            else:
                print("self.head.next.data: None")

        elif x[:3] == "ins" or x[:3] == "del" or x[:3] == "sea":
            x = x.split(" ")
            if x[0] == "ins":
                linked_list.insert(Node(x[1]))
            elif x[0] == "del":
                linked_list.delete(x[1])
            elif x[0] == "sea":
                print(linked_list.search(x[1]))
            else:
                print("Unmöglicher Fehler")
        else:
            print("Kein zulässiger Command!")