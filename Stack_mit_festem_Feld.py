class Stack:
    def __init__(self, SizeOfField):
        self.SizeOfField = int(SizeOfField)
        self.Top = -1
        self.Field = [self.SizeOfField]

    def pop(self):
        if not self.isEmpty():
            self.Top -= 1
            print(self.Field[self.Top + 1])
            self.Field.pop(self.Top + 1)
        else:
            print("Es sind keine Elemente auf dem Stack abgelegt.")

    def push(self, x):
        if self.Top < self.SizeOfField - 1:
            self.Top += 1
            self.Field.insert(self.Top, x)
        else:
            print("Die maximale Anzahl an Elementen ist erschöpft.\nObjekt wurde nicht hinzugefügt.")

    def isEmpty(self):
        if self.Top == -1:
            return True
        else:
            return False

    def draw(self):
        counter = 0
        print("|", end="")
        for i in range(0, self.SizeOfField):
            if i < self.Top + 1:
                print(self.Field[i], end="")
                counter += 1
            else:
                print(" ", end="")
            print("|", end="")
        print("")


size = input("Bitte geben Sie hier die Größe des Stacks ein.")
st = Stack(size)

while True:
    x = input("Zahl eingeben, pop, isEmpty oder draw eingeben.")
    if x.isdigit():
        st.push(x)
    elif x == "pop":
        st.pop()
    elif x == "isEmpty":
        st.isEmpty()
    elif x == "draw":
        st.draw()
    else:
        break
