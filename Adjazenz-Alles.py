import doppelt_verkettete_Liste as dvl


class bNode(dvl.Node):
    def __init__(self, data):
        super().__init__(data)
        self.color = "white"


class bLinkedList(dvl.LinkedList):
    def changeColor(self, node):
        if node.color == "white":
            node.color = "grey"
        elif node.color == "grey":
            node.color = "black"
        elif node.color == "black":
            node.color = "white"


class Adjazenzliste:
    def __init__(self, x):
        self.x = int(x)
        self.ListNode = []

        for i in range(0, self.x):
            linked = bLinkedList()
            linked.insert(bNode("End"))
            self.ListNode.append(linked)

    def ListAppend(self, node, value):
        if self.x >= int(node) >= 0:
            self.ListNode[int(node)].insert(value)

    def ListDelete(self, node, value):
        if self.x >= int(node) >= 0:
            self.ListNode[int(node)].delete(value)

    def GetEdge(self, node):
        if self.x >= int(node.data) >= 0:
            return self.ListNode[int(node.data)]

    def display(self):
        for k in range(0, len(self.ListNode)):
            self.ListNode[k].display()


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
        if self.yList[int(y)][int(x)] != 1:
            self.yList[int(y)][int(x)] = 1

    def AdjDelete(self, x, y):
        if self.yList[int(y)][int(x)] != 0:
            self.yList[int(y)][int(x)] = 0

    def getEdge(self, x, y):
        return self.yList[int(y)][int(x)]

    def display(self):
        for i in range(0, self.y):
            for j in range(0, self.y):
                print(self.yList[i][j], end=", ")
            print()


def importGraph():
    print("Bitte geben Sie einen Graph folgendermaßen an:")
    temp_input = input("NameDesNeuenGraphens,AnzahlDerKnoten:x1,y1;x2,y2;")
    GraphName, Temp_rest = temp_input.split(":")
    GraphNameS = GraphName.split(",")
    Temp_rest_Edge = Temp_rest.split(";")
    Temp_Neuer_Graph = [(GraphNameS[0], GraphNameS[1])]
    for i in Temp_rest_Edge:
        if i != "":
            Temp = i.split(",")
            Temp_Neuer_Graph.append((Temp[0], Temp[1]))
    return Temp_Neuer_Graph


def loadGraph(graph):
    print(graph[0][1])
    ungerichtetLinked = Adjazenzliste(int(graph[0][1]))
    ungerichtetMatrix = Adjazenzmatrix(int(graph[0][1]))
    for i in range(1, len(graph)):
        ungerichtetLinked.ListAppend(graph[i][0], bNode(graph[i][1]))
        ungerichtetMatrix.AdjAppend(graph[i][0], graph[i][1])
    return ungerichtetLinked, ungerichtetMatrix


if __name__ == '__main__':
    Graphen = []
    Linked = None
    Matrix = None
    quit = False
    while not False:
        command = input("Befehle: quit, NewGraph: ng, LoadGraph: lg, Breitensuche: Bs, Tiefensuche: Ts, "
                        "PrintLoadedGraph: plg")
        if command == "quit":
            break
        elif command == "ng":
            Graphen.append(importGraph())
        elif command == "lg":
            if len(Graphen) != 0:
                print(Graphen)
                commandGraph = input("Welcher Graph soll geladen werden? 0-" + str(len(Graphen)-1))
                if 0 <= int(commandGraph) >= len(Graphen)-1:
                    Linked, Matrix = loadGraph(Graphen[int(commandGraph)])
                    print("Done")
                else:
                    print("Graph " + commandGraph + " existiert nicht.")
            else:
                print("Keine Graphen gespiechert.")
        elif command == "plg":
            Linked.display()
            Matrix.display()
        elif command == "Bs":
            pass
        elif command == "Ts":
            pass


"""Test,6:0,1;0,2;0,4;1,0;2,0;2,3;2,5;3,2;3,4;3,5;4,0;4,3;4,5;5,2;5,3;5,4;"""