import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

# load csv file

df = pd.read_csv("kidney.csv")
# Looking for null values

print("Null values :: ")
print(df.isnull().sum())
# selection dependant and independant
# Spliting the data
from sklearn.ensemble import RandomForestClassifier
X = df.drop("ChronicKidneyDisease",axis=1)
y = df["ChronicKidneyDisease"]
X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.2)
clf = RandomForestClassifier()

clf.fit(X_train, y_train);
## Evaluating the model
# make pickle file for the model

model = pickle.dump(clf, open("model.pkl", "wb"))

#   Training part is complete


from flask import Flask

# creating app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
print(model.predict([[777,36,15.4,7,5.2,0,1,0,0]]))



