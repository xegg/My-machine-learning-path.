import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Print you can execute arbitrary python code
train = pd.read_csv("input/train.csv", dtype={"Age": np.float64}, )
test = pd.read_csv("input/test.csv", dtype={"Age": np.float64}, )

train["Age"][np.isnan(train["Age"])] = np.median(train["Age"])

train['Age'] = train['Age'].fillna(train['Age'].mean())
train['Fare'] = train['Fare'].fillna(train['Fare'].mean())

train["Male"] = train['Sex'].apply(lambda x:1 if x=='male' else 0)
train["Female"] = train['Sex'].apply(lambda x:1 if x!='male' else 0)

train["S"] = train['Embarked'].apply(lambda x:1 if x=='S' else 0)
train["C"] = train['Embarked'].apply(lambda x:1 if x=='C' else 0)
train["Q"] = train['Embarked'].apply(lambda x:1 if x=='Q' else 0)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for n,point in train.iterrows():
    gender = (1 if point['Male'] else 0 ) + np.random.rand()/10
    pclass = point['Pclass'] + np.random.rand()/10
    surv = point['Survived']
    third_feature = point['SibSp'] + np.random.rand()/10
    color = 'red' if surv else 'blue'

    ax.scatter(gender, pclass, third_feature, c=color)

ax.set_xlabel('gender')
ax.set_ylabel('Pclass')
ax.set_zlabel('Sibsp')

plt.show()

plt.savefig('viz.png')
