import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Statistik:

    def charakteristika(self, raw_data):
        print("Datensatz: " + str(raw_data))
        print("Anzahl Messwerte: " + str(len(raw_data)))
        print("verschiedene auftretende Messwerte: " + str(np.unique(raw_data)))
        raw_data_unique, raw_data_counts = np.unique(raw_data, return_counts=True)
        print("Absolute Häufigkeiten: " + str(raw_data_unique) + "     " + str(raw_data_counts))
        print("Relative Häufigkeiten: " + str(np.unique(raw_data, return_counts=True)[1] / len(raw_data)))
        plt.hist(raw_data)
        plt.show()
        sns.ecdfplot(raw_data)
        plt.show()
        sns.kdeplot(raw_data)
        plt.show()
        sns.violinplot(data=raw_data)
        plt.show()

    def kennwerte(self, raw_data):
        print("Mittelwert: " + str(np.mean(raw_data)))
        print("Median: " + str(np.median(raw_data)))
        print("Modalwert: " + str(stats.mode(raw_data)))
        print("Quartile: " + str(np.quantile(raw_data, [0.25, 0.5, 0.75])))
        print("Empirische Varianz: " + str(np.var(raw_data, ddof=1)))
        print("Empirische Standarabweichung: " + str(np.std(raw_data, ddof=1)))
        print("Spannweite: " + str(np.max(raw_data) - np.min(raw_data)))
        print("Interquartilabstand: " + str(np.quantile(raw_data, 0.75) - np.quantile(raw_data, 0.25)))
        print("Empirische Schiefe: " + str(stats.skew(raw_data)))
        print("Empirische Wölnbung: " + str(stats.kurtosis(raw_data)))

    def korrelation(self, a, b):
        print("Empirishcer Korrelationskoeffizient: " + str(np.corrcoefa, b))
        print("Empirische Kovarianz: " + str(np.cov(a, b)))
        plt.plot(a, b)
        plt.show()

    def regression(self, a, b):
        reg = stats.linregress(a, b)
        print("Regressionsgerade: " + str(reg))
        plt.plot(a, reg.intercept + reg.slope * np.asarray(a), 'r', label='fitted line')
        plt.show()