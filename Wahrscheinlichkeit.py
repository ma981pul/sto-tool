class Wahrscheinlichkeit:
    def __init__(self, name, wert, ebene):
        self.name = name
        self.wert = wert
        self.gegenwahrscheinlichkeit = 1 - float(wert)
        self.ebene = 1

    def toString(self):
        print("P(" + self.name + ") = " + self.wert)
        print("P(" + self.name + "_) = " + str(self.gegenwahrscheinlichkeit))