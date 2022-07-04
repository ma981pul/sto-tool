import sys

import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from BedingteWahrscheinlichkeit import BedingteWahrscheinlichkeit
from Wahrscheinlichkeit import Wahrscheinlichkeit


class Wahrscheinlichkeitsrechnung:

    def __init__(self):
        self.wahrscheinlichkeiten = []
        self.bedingteWahrscheinlichkeiten = []

    def permutation(self, n):
        print(special.factorial(n, exact=True))

    def variation(self, n, k, repetition):
        if(repetition):
            print(pow(n, k))
        else:
            print(special.perm(n, k, exact=True))

    def combination(self, n, k, repetition):
        if(repetition):
            print(str(special.comb(n, k, repetition=True, exact=True)))
        else:
            print(str(special.comb(n, k, repetition=False)))

    def leseWahrscheinlichkeiten(self):
        while(True):
            name = input("Wahrscheinlichkeitsbezeichnung oder 'q' eingeben: ")
            if(name == 'q'):
                break
            wert = input("Wert eingeben: ")
            if(len(name) == 1):
                ebene = input("Ebene im Wahrscheinlichkeitsbaum angeben: ")
                self.wahrscheinlichkeiten.append(Wahrscheinlichkeit(name, wert, ebene))
            else:
                self.bedingteWahrscheinlichkeiten.append((BedingteWahrscheinlichkeit(name[0], name[2], wert)))

            for i in self.wahrscheinlichkeiten:
                print(i.toString())
            for i in self.bedingteWahrscheinlichkeiten:
                print(i.toString())

    def berechneWahrscheinlichkeiten(self, w):


        if(type(w) is BedingteWahrscheinlichkeit):
            e = w.ereignis
            b = w.bedingung
            v = w.wert

            #Formel von Bayes
            w.wert = (next(x for x in self.bedingteWahrscheinlichkeiten if x.ereignis == w.gegenereignis and x.gegenereignis == w.ereignis).wert * next(x for x in self.wahrscheinlichkeiten if x.ereignis == w.ereignis).wert) / next(x for x in self.wahrscheinlichkeiten if x.ereignis == w.bedingung).wert
