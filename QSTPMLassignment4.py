import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_csv("database.csv",header=None,dtype=str,error_bad_lines=False,sep=',',quotechar='"',low_memory=False)
#to remove data where victim age is 998
#X=df.drop(df[df[12]=='998'].index)
#train2=X.drop(X[X[16]=='0'].index)
#train=train2.drop(train2[train2[12]=='0'].index)
victim_age=pd.to_numeric(df[12],errors="coerce",downcast=None)
perpetrator_age=pd.to_numeric(df[16],errors="coerce",downcast=None)
train_victim=[]
train_perpetrator=[]
test_victim=[]
test_perpetrator=[]


lm=LinearRegression()
for i in range (1,len(victim_age)):
    if ((perpetrator_age[i]==0)and (victim_age[i]!=998)):
	test_victim.append(victim_age[i])
    if ((perpetrator_age[i]!=0) and (victim_age[i]!=998)):
	train_victim.append(victim_age[i])
	train_perpetrator.append(perpetrator_age[i])
train_victim=np.reshape(train_victim,(len(train_victim),1))
train_perpetrator=np.reshape(train_perpetrator,(len(train_perpetrator),1))
test_victim=np.reshape(test_victim,(len(test_victim),1))
plt.scatter(train_victim,train_perpetrator)
plt.xlabel("Victim's Age")
plt.ylabel(" Actual Perpetrator's Age")
plt.show()
lm.fit(train_victim,train_perpetrator)
print "The slope of is",lm.coef_
test_perpetrator=lm.predict(test_victim)
test_perpetrator=np.reshape(test_perpetrator,(len(test_perpetrator),1))
plt.scatter(test_victim,test_perpetrator)
plt.xlabel("Victims who's perpetrators age is unknown")
plt.ylabel("preicted perpetrators age")
plt.show()






