class Wahrscheinlichkeit:
    def __init__(self, name, wert):
        self.name = name
        self.wert = wert
        self.gegenwahrscheinlichkeit = 1 - float(wert)

    def toString(self):
        print("P(" + self.name + ") = " + self.wert)
        print("P(" + self.name + "_) = " + str(self.gegenwahrscheinlichkeit))