import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import csv
df = pd.read_csv('reduced.csv')
df.head()
ax = sns.countplot(x = 'Year', data = df)
plt.show()
ax = sns.countplot(x = 'Attack Type', data = df)
plt.show()
ax=sns.countplot('Year',data=df,palette='RdYlGn_r',edgecolor=sns.color_palette('dark',7))
plt.xticks(rotation=90)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()
plt.subplots(figsize=(15,6))
sns.countplot('Attack Type',data=df,palette='inferno',order=df['Attack Type'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Attacking Methods by Terrorists')
plt.show()
plt.subplots(figsize=(15,6))
sns.countplot(df['Target Type'],palette='inferno',order=df['Target Type'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Favorite Targets')
plt.show()
plt.subplots(figsize=(15,6))
sns.countplot(df['Month'],palette='inferno',order=df['Month'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Favorite Time Of The Year')
plt.show()
pd.crosstab(df.Region,df.Year).plot.barh(stacked=True,width=1,color=sns.color_palette('RdYlGn',9))
plt.show()
plt.subplots(figsize=(15,6))
sns.countplot('Weapon',data=df,palette='inferno',order=df['Weapon'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Most Used Weapon By Terrorists')
plt.show()
print('Country with Highest Terrorist Attacks:',df['Country'].value_counts().index[0])
print('Most active terrorist group:',df['Gang Name'].value_counts().index[0])
print('Year With Most Attacks:',df['Year'].value_counts().index[0])
print('Month With Most Attacks:',df['Month'].value_counts().index[0])
print('Most Used Weapon:',df['Weapon'].value_counts().index[0])
print('Most vulnerable city:',df['City'].value_counts().index[0])
print('Region With Highest No Of Attacks:',df['Region'].value_counts().index[0])
print('Most Vulnerable Target:',df['Target Type'].value_counts().index[0])







