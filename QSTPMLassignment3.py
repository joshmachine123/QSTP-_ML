import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_excel("sat.xls")
X=df.drop("univ_GPA",axis=1)
lm=LinearRegression()
lm.fit(X,df.univ_GPA)
EC=pd.DataFrame(zip(X.columns,lm.coef_), columns =['features','estimatedCoefficents'])
print EC
target_values=lm.predict(X)
plt.scatter(df.univ_GPA,lm.predict(X))
plt.xlabel("Actual University GPA")
plt.ylabel("Predicted University GPA")
plt.plot([0,1,2,3,4])
plt.show()
print "The Meaan Square Error is ", np.mean((lm.predict(X)-df.univ_GPA)**2)
plt.scatter(df.univ_GPA,abs(lm.predict(X)-df.univ_GPA))
plt.xlabel("Actual University GPA")
plt.ylabel("Absolute error between predicted and actual GPAs")
plt.hlines(y=0,xmin=0,xmax=4)
plt.show()



