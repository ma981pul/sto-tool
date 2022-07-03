class BedingteWahrscheinlichkeit:
    def __init__(self, ereignis, bedingung, wert):
        self.bedingung = bedingung
        self.ereignis = ereignis
        self.wert = wert
        self.gegenwahrscheinlichkeit = 1 - wert

    def toString(self):
        print("P(" + self.ereignis + "/" + self.bedingung + ") = " + str(self.wert))
        print("P(" + self.ereignis + "/" + self.bedingung + "_) = " + str(self.gegenwahrscheinlichkeit))