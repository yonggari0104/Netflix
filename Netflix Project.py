import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nx = pd.read_csv('C:\\Users\\user\\.spyder-py3\\Netflix\\netflix.csv')

#DROPS THE ROWS WITH NaN VALUE
nex = nx.dropna()
#RESETS THE INDEX NUMBER
nex = nex.reset_index(drop=True)

print(nex.head())
print(nex.describe())




#BREAKDOWN OF TYPE
print(nex['type'].value_counts())
labels = 'Movies', 'TV Shows'
sizes = [3678, 96]
explode = (0,0.1)
plt.pie(sizes, labels=labels,shadow = True, startangle=90, explode = explode, autopct='%1.1f%%')
plt.show()




#BREAKDOWN OF DIRECTOR
#NUMBER OF DIRECTORS
print(nex.director.count())
#NUMBER OF DIFFERENT DIRECTORS
print(nex.director.nunique())
#PRINTS DIRECTOR COUNT NUMBERS (EG. HOW MANY MOVIES EACH DIRECTOR HAS)
print(nex['director'].value_counts())




#BREAKDOWN OF COUNTRY
print(nex['country'].value_counts())
n_1_country = 0
n_2_country = 0
#SEPARATES THE SINGULAR COUNTRIES WITH THE MULTIPLE COUNTRIES
column_data = list(nex['country'].values)
for i in range(0, len(column_data)):
	temporary_data = column_data[i]
	count = len(temporary_data.split(','))
	if count == 1:
		n_1_country += 1
	elif count >= 2:
		n_2_country += 1
	else:
		print('Some issues spotted.')
#PRINTS HOW MANY INDIVIDUAL COUNTRIES
print(n_1_country)
#PRINTS HOW MANY MULTIPLE COUNTRIES
print(n_2_country)

labels = 'Single Countries', 'Multiple Countries'
sizes = [3104, 670]
explode = (0,0.1)
plt.pie(sizes, labels=labels,shadow = True, startangle=90, explode = explode, autopct='%1.1f%%')
plt.show()




#DATE ADDED BREAKDOWN
print(nex.date_added.min())
print(nex.date_added.max())
print(nex.date_added.nunique())

unique_date = list( set(nex['date_added'].values))
print(unique_date)

counter = []

for date in unique_date:
	pandas_slice = nex[nex['date_added'] == date]
	counter.append([date, len(pandas_slice)])

counter = pd.DataFrame(counter)
counter.columns = ['date_added', 'Number of Movies']




#RELEASE YEAR
print(nex.release_year.describe())
print(nex['release_year'].value_counts())


print(nex.release_year.sort_values())

ryc = (nex['release_year'].value_counts())
print(ryc.max())
print(ryc.min())




#RATING BREAKDOWN
print(nex.rating.describe())
print(nex['rating'].value_counts())

labels = 'TV-MA', 'TV-14', 'R', 'TV-PG', 'PG-13', 'PG'
sizes = [1189,917,501,358,278,176]
explode = (0.1,0.1,0,0,0,0)
plt.pie(sizes, labels=labels,shadow = True, startangle=90, explode = explode, autopct='%1.1f%%')
plt.show()





#DURATION BREAKDOWN
print(nex.duration.describe())
print(nex['duration'].value_counts())
print(nex.duration.nunique())

#%%












