import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Housing.csv')

evfiyatlari=df['price']
areas=df['area']
bedrooms=df['bedrooms']
stories=df['stories']
numberofbathrooms =df['bathrooms']
furnishingstatus=df['furnishingstatus']

kutular = 547

plt.hist(evfiyatlari, bedrooms, edgecolor='yellow', bins= kutular)
plt.title('evfiyatlarixbedrooms')
plt.ylabel('evfiyatlari') 
plt.xlabel('bedrooms')

plt.show()

plt.hist(evfiyatlari, areas, edgecolor='navyblue', bins= kutular)
plt.title('evfiyatlarixareas')
plt.ylabel('evfiyatlari') 
plt.xlabel('areas')

plt.show()

plt.hist(evfiyatlari, stories, edgecolor='red', bins= kutular)
plt.title('evfiyatlarixstories')
plt.ylabel('evfiyatlari') 
plt.xlabel('stories')

plt.show()

ortevfiyatlari=df.groupby(numberofbathrooms)['price'].mean()
plt.barh(ortevfiyatlari, numberofbathrooms, color='purple')
plt.title('ortevfiyatlarixnumberofbathrooms')
plt.ylabel('ortevfiyatlari') 
plt.xlabel('numberofbathrooms')

plt.show()

ortevfiyatlari=df.groupby(furnishingstatus)['price'].mean()
plt.barh(ortevfiyatlari, furnishingstatus, color='yellow')
plt.title('ortevfiyatlarixstories')
plt.ylabel('ortevfiyatlari') 
plt.xlabel('furnishingstatus')

plt.show()

secilen_veri=df[['price','area','bedrooms','bathrooms','stories','parking']]

kormat = df.corr()
print(kormat)

sns.heatmap(kormat,annot=True)
plt.show()