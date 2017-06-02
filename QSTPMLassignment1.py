import pandas as pd
import numpy as np
import csv,StringIO
import seaborn
df=pd.read_csv("database.csv",header=None,dtype=str,error_bad_lines=False,sep=',',quotechar='"')
print df[df[10]=="Yes"].iloc[:,10].count()#question 1:448172 were solved
print df[20].value_counts()#question 2:Handgun,knife,Blunt Object,Firearm,Unknown,then shotgun  
statewise=df.groupby(df[5])
print statewise[20].value_counts(normalize=True)#question 3: statewise top weapon used ordered in descending order
count=df[6].value_counts()
time=pd.DataFrame({'Year':count.keys(),'No of Homicides':count}).sort_values(by=['Year'],ascending=True)
seaborn.barplot(time['Year'],time['No of Homicides'])
seaborn.plt.show()#question 4 bar graph of no of homicides every year




