import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
iris=datasets.load_iris()
X=iris.data
Y=iris.target
plt.scatter(X[50:100,0],X[50:100,1],color='black',marker='x',label='versicolor')
plt.scatter(X[100:150,0],X[100:150,1],color='red',marker='+',label='verginica')
plt.xlabel('sepal length[cm]')
plt.ylabel('petal length[cm]')
plt.legend(loc='upper left')
plt.show()
