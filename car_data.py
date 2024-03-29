import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.data")
print(data.head())

ie = preprocessing.LabelEncoder()
buying = ie.fit_transform(list(data["buying"]))
maint = ie.fit_transform(list(data["maint"]))
door = ie.fit_transform(list(data["door"]))
persons = ie.fit_transform(list(data["persons"]))
lug_boot = ie.fit_transform(list(data["lug_boot"]))
safety = ie.fit_transform(list(data["safety"]))
cls = ie.fit_transform(list(data["class"]))

predictions = "class"

x = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

print(x_train, y_train)

