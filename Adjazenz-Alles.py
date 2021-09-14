import doppelt_verkettete_Liste as dvl


class Node(dvl.Node):
    def __init__(self):
        self.color = "white"

class LinkedList(dvl.LinkedList):
    def changeColor(self):



class Adjazenzliste:
    def __init__(self, x):
        self.x = x
        self.ListNode = []

        for i in range(0, self.x):
            linked = dvl.LinkedList()
            linked.insert(i+1)
            self.ListNode.append(linked)

    def ListAppend(self, node, value):
        if self.x >= node - 1 >= 0:
            self.ListNode[node - 1].insert(value)

    def ListDelete(self, node, value):
        if self.x >= node - 1 >= 0:
            self.ListNode[node - 1].delete(value)

    def GetEdge(self, node):
        if self.x >= node - 1 >= 0:
            return self.ListNode[node - 1]


class Adjazenzmatrix:
    def __init__(self, y):
        self.y = y
        self.yList = []

        for i in range(0, self.y):
            tempList = []
            for j in range(0, self.y):
                tempList.append(int(0))
            self.yList.append(tempList)

    def AdjAppend(self, x, y):
        if self.yList[y][x] != 1:
            self.yList[y][x] = 1
        else:
            print("Knoten bereits vorhanden.")

    def AdjDelete(self, x, y):
        if self.yList[y][x] != 0:
            self.yList[y][x] = 0
        else:
            print("Kein Knoten zum löschen vorhanden.")

    def getEdge(self, x, y):
        return self.yList[y][x]


def importGraph(x):
    pass
