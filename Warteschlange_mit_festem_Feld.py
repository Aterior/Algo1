class Queue:
    def __init__(self, SizeOfField):
        self.SizeOfField = int(SizeOfField)
        self.count = -1
        self.kopf = 0
        self.ende = 0
        self.Field = []

    def Enqueue(self, x):
        if self.count < self.SizeOfField-1:
            self.ende += 1
            self.count += 1
            self.Field.insert(self.ende, x)
        else:
            print("Die maximale Anzahl an Elementen ist erschöpft.\nObjekt wurde nicht hinzugefügt.")

    def Dequeue(self):
        if not self.isEmpty():
            print(self.Field[self.kopf])
            self.count -= 1
            #self.kopf += 1
            self.Field.pop(self.kopf)
        else:
            print("Es sind keine Elemente in der Warteschlange vorhanden.")

    def isEmpty(self):
        if self.count == -1:
            return True
        else:
            return False

    def draw(self):
        print("|", end="")
        temp_count = -1
        for i in range(0, self.SizeOfField):
            temp_count += 1
            if temp_count <= self.count:
                print(self.Field[self.kopf+i], end="")
            elif self.count < temp_count <= self.SizeOfField:
                print(" ", end="")
            print("|", end="")
        print("")


size = input("Bitte geben Sie hier die Größe der Warteschlange ein.")
qu = Queue(size)

while True:
    x = input("Zahl eingeben, pop, isEmpty oder draw eingeben.")
    if x.isdigit():
        qu.Enqueue(x)
    elif x == "pop":
        qu.Dequeue()
    elif x == "isEmpty":
        qu.isEmpty()
    elif x == "draw":
        qu.draw()
    else:
        break
