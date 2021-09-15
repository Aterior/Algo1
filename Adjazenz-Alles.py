import doppelt_verkettete_Liste as dvl


class Node(dvl.Node):
    def __init__(self):
        self.color = "white"


class LinkedList(dvl.LinkedList):
    def changeColor(self, node):
        if node.color == "white":
            node.color = "grey"
        elif node.color == "grey":
            node.color = "black"
        elif node.color == "black":
            node.color = "white"


class Adjazenzliste:
    def __init__(self, x):
        self.x = x
        self.ListNode = []

        for i in range(0, self.x):
            linked = LinkedList()
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
        if self.yList[y][x] != 1 and self.yList[x][y] != 1:
            self.yList[y][x] = 1
            self.yList[x][y] = 1

    def AdjDelete(self, x, y):
        if self.yList[y][x] != 0 and self.yList[x][y] != 0:
            self.yList[x][y] = 0
            self.yList[y][x] = 0

    def getEdge(self, x, y):
        return self.yList[y][x]


def importGraph():
    print("Bitte geben Sie einen Graph folgendermaßen an:")
    temp_input = input("NameDesNeuenGraphens,AnzahlDerKnoten:x1,y1;x2,y2;")
    GraphName, Anzahl_Knoten, Temp_rest = temp_input.split(":")
    Temp_rest_Edge = Temp_rest.split(";")
    Temp_Neuer_Graph = [(GraphName, Anzahl_Knoten)]
    for i in Temp_rest_Edge:
        Temp = i.split(",")
        Temp_Neuer_Graph.append((Temp[0], Temp[1]))
    return Temp_Neuer_Graph

def loadGraph(graph):
    Linked = Adjazenzliste
    Matrix = Adjazenzmatrix
    for i in range(1, len(graph)):


if __name__=='__main__':
    Graphen = []
    Linked = None
    Matrix = None
    quit = False
    while not False:
        command = input("Befehle: quit, NewGraph: ng, LoadGraph: lg, Breitensuche: Bs, Tiefensuche: Ts")
        if command == "quit":
            quit = True
        elif command == "ng":
            Graphen.append(importGraph())
        elif command == "lg":
            if len(Graphen) != 0:
                for i in Graphen:
                    print(i, end=", ")
                commandGraph = input("Welcher Graph soll geladen werden? 0-" + len(Graphen))
                if 0 <= commandGraph >= len(Graphen):
                    Linked, Matrix = loadGraph(Graphen[commandGraph])
                    print("Done")
                else:
                    print("Graph" + commandGraph + "existiert nicht.")
            else:
                print("Keine Graphen gespiechert.")
        elif command == "Bs":
            pass
        elif command == "Ts":
            pass




