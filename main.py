#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas
import pandas as pd
#importing seaborn
import seaborn as sns
#reading csv
df=pd.read_csv("Penguins.csv")
print(df.info())
#i do not know which name to put so i will jus keep tt
tt=("Culmen Length (mm)","Body Mass (g)")
plt.scatter(data=df,x="Culmen Length (mm)",y="Body Mass (g)")
plt.show()