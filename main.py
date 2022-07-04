import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Statistik import Statistik
from Wahrscheinlichkeitsrechnung import Wahrscheinlichkeitsrechnung


##Beschreibende Statistik

# a = [25, 17, 25, 29, 20, 15, 11, 17, 16, 16]
# s = Statistik()
# s.kennwerte(a)
# s.charakteristika(a)


##Zufallsvariablen

# X = [1, 1, 1, 1, 2, 3, 3, 3]
# T = np.linspace(1, 3, 3)
# p, _, _ = plt.hist(X, np.linspace(1,4,4), density=True)
# print(np.cumsum(p))
# print(np.sum(T * p))
# print(np.var(X, ddof=0))
# print(np.std(X, ddof=0))
# plt.bar(T, p)
# plt.step(X, np.cumsum(p))


###Diskrete Verteilungen

##Bernoulli
# p = 0.7
# print(stats.bernoulli(p).pmf(0))
# print(stats.bernoulli(p).cdf(-1))
# print(stats.bernoulli(p).expect())
# print(stats.bernoulli(p).var())

##Geometrische Verteilung
# p = 0.7
# print(stats.geom(p).pmf(0))
# print(stats.geom(p).cdf(0))
# print(stats.geom(p).expect())
# print(stats.geom(p).var())

##Binomialverteilung
# x = 3
# n = 4
# p = 0.2
# print(stats.binom(n, p).pmf(x))
# print(stats.binom(n, p).cdf(x))
# print(stats.binom(n, p).expect())
# print(stats.binom(n, p).var())

##Poisson
# x = 5
# l = 2
# print(stats.poisson(l).pmf(x))
# print(stats.poisson(l).cdf(x))
# print(stats.poisson(l).expect())
# print(stats.poisson(l).var())

##Hypergeometrische Verteilung
# x = 5
# n = 8
# N = 50
# M = 45
# print(stats.hypergeom(N, M, n).pmf(x))
# print(stats.hypergeom(N, M, n).cdf(x))
# print(stats.hypergeom(N, M, n).expect())
# print(stats.hypergeom(N, M, n).var())


###Stetige Verteilungen

##Gleichverteilung
# a = 2
# b = 10
# print(stats.uniform(a, b-a).pdf(0))
# print(stats.uniform(a, b-a).cdf(0))
# print(stats.uniform(a, b-a).ppf(0.1))
# print(stats.uniform(a, b-a).expect())
# print(stats.uniform(a, b-a).var())

##Exponentialverteilung
# l = 5
# print(stats.expon(scale=1/l).pdf(0))
# print(stats.expon(scale=1/l).cdf(0))
# print(stats.expon(scale=1/l).ppf(0.1))
# print(stats.expon(scale=1/l).expect())
# print(stats.expon(scale=1/l).var())

##Normalverteilung
# mu = 1
# sigma = 2
# print(stats.norm(mu, sigma).pdf(0))
# print(stats.norm(mu, sigma).cdf(0))
# print(stats.norm(mu, sigma).ppf(0))
# print(stats.norm(mu, sigma).expect())
# print(stats.norm(mu, sigma).var())
