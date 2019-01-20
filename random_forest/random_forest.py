from numpy import genfromtxt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

dataset = genfromtxt('data.csv', delimiter=",")
x = dataset[1:, 0:4]
y = dataset[1:, 4]
clf = RandomForestClassifier(n_jobs= 2, )
