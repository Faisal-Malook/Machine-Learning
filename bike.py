#Importing libraries

import pandas
import scipy
import sklearn
import numpy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns


#Reading csv file

Bike = pandas.read_csv(r"C:\Users\k21190224\Desktop\python first project\bikedatasethour.csv")

print(Bike)

#Bike.workingday.replace(('Yes', 'No'), (1, 0), inplace=True)

#Bike.head(workingday)

#Converting datatype from string/object to boolean/integer

Bike['workingday'] = Bike['workingday'].map({'Yes': 1, 'No': 0})

Bike.info()

# Finding null values in data frame

print(Bike.isnull().values.any())
print(Bike.isnull().sum())

# Filling missing values with mean

Bike.temp.fillna(Bike.temp.mean(), inplace=True)
Bike.atemp.fillna(Bike.atemp.mean(), inplace=True)

# Identifying peak hour frequency of bike usage and plot

Bike['hr'].value_counts().plot.bar()

#plt.show()



conditions = [
    (Bike['hr'] >= 7) & (Bike['hr'] <= 9) & (Bike['workingday']==1) ,
    (Bike['hr'] >= 16) & (Bike['hr'] <= 19) & (Bike['workingday']==1),
    (Bike['hr'] >= 10) & (Bike['hr'] <= 16) & (Bike['workingday']==0)]
values =[1,1,1]
Bike['pt'] = numpy.select(conditions, values)

#conditions = [
#    (Bike['hr']>= 22) & (Bike['hr']<=4)]
#values= []
Bike['nighttime']= numpy.where((Bike['hr']>= 22) & (Bike['hr']<=4), 1, 0)








