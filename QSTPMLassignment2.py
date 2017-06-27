import pandas as pd
import numpy as np
import csv,StringIO
import seaborn
import matplotlib.pyplot as plt
df=pd.read_csv("database.csv",header=None,dtype=str,error_bad_lines=False,sep=',',quotechar='"')
yearcount=df[6].value_counts()
weaponcount=df[6].groupby(df[20]).value_counts()
hguncount=weaponcount["Handgun"]
hgunpercentage=hguncount/yearcount
knifecount=weaponcount["Knife"]
strangulcount=weaponcount["Strangulation"]
riflecount=weaponcount["Rifle"]
#question 1 plot weapon vs year. just thought that the percentage would be a good indicator too
hguncount.plot(kind='line',legend='True',label='HandGun')
hgunpercentage.plot(kind='line',legend='True',label='HandGun Percentage')
knifecount.plot(kind='line',legend='True',label='Knife')
strangulcount.plot(kind='line',legend='True',label='Strangulation')
riflecount.plot(kind='line',legend='True',label='Rifle')
plt.show()
# question 2
relationshipcount=df[6].groupby(df[19]).value_counts()
strangecount=relationshipcount["Stranger"]
acquaintancecount=relationshipcount["Acquaintance"]

strangecount.plot(kind='line',legend='True',label='stranger Count')
acquaintancecount.plot(kind='line',legend='True',label='Acquaintance Count')
#question 3
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(6,6), sharey=True)

axes[0,0].boxplot(weaponcount["Handgun"])
axes[0,0].set_title('Handgun')
axes[0,1].boxplot(weaponcount["Knife"])
axes[0,1].set_title('Knife')
axes[1,0].boxplot(weaponcount["Shotgun"])
axes[1,0].set_title('Shotgun')
axes[1,1].boxplot(weaponcount["Drowning"])
axes[1,1].set_title('Drowning')
axes[2,0].boxplot(weaponcount["Rifle"])
axes[2,0].set_title('Rifle')
axes[2,1].boxplot(weaponcount["Strangulation"])
axes[2,1].set_title('Strangulation')

plt.show()


