# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# x = np.linspace(0,100,5)
# x = np.linspace(0,100,10)
# y = np.linspace(50,100,1000)
# print(x,y)
# print(y)
# plt.plot(x,y,'b_')
# plt.plot(x,'b_')
# plt.plot(y,'b_')
# plt.show()

# %%
# x = [1,2,3]
# y = [4,5,6]
# # plt.plot(x,y)
# plt.plot([1,4,6,8],[3,8,3,5])
# plt.ylabel("price")
# plt.xlabel("time")
# plt.title("Budget")
# plt.xlim([4,7]) # for limiting range of x axis
# plt.ylim([3,7]) # for limiting range of y axis
# plt.show()

#%%
# x = np.linspace(0,5)
# y = np.linspace(3,6)
# # plt.plot(x,y,'r.',x,y**2,'b.',x,y**3,'b.')
# # plt.plot(x,y,'r_',x,y**2,'b.',x,y**3,'g^')
# # plt.ylim([0,100])
# # plt.xlim([0,1000])
# plt.plot(x,y)
# # plt.plot(x,y,'b+')
# # plt.plot(x,y,'b_')
# # plt.plot(x,y,'b^')
# plt.show()

#%%
###### Subplotting
# x = np.linspace(1,10,100)
# y = np.log(x)
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.title("y = logx")
# plt.plot(x,y)
# # plt.show()
# plt.subplot(1,2,2)
# plt.title("y = logx**2")
# plt.plot(x,y**2)
# plt.show()


#%%
# y = np.linspace(0,5,100) # line starts from (0,0) to (5,100) with 100 divisions
# plt.plot(y)
# plt.show()

#%%
###### Subplotting 4 figures together
# x = np.linspace(0,5)
# # plt.figure()
# plt.subplot(2,2,1)
# plt.plot(x)
# plt.title("Linear")
# plt.subplot(2,2,2)
# plt.plot(x,x**2)
# plt.title("Exponential")
# plt.subplot(2,2,3)
# plt.plot(x,x**3)
# plt.title("Cubic")
# plt.subplot(2,2,4)
# plt.plot(x,np.log(x))
# plt.title("Logarithm")
# plt.show()


#%%
###### Types of plotting (Reading CSV files)
### Boxplot
# df = pd.read_csv('/Users/amankumarsaw/Documents/Prakash/ML/csv/industry_sic.csv')
# # print(df)
# # print(df.head())
# plt.boxplot(df['SIC Code'])
# plt.show()



# %%
###### Subplotting boxplots
# df = pd.read_csv('/Users/amankumarsaw/Documents/Prakash/ML/csv/industry_sic.csv')
# # print(df)
# plt.subplot(1,2,1)
# plt.boxplot(df['SIC Code'])
# plt.subplot(1,2,2)
# plt.boxplot(df['SIC Code'])

####### plt.yscale('log') converts data to lagarithmic data annd makes data analysis more convenient
# plt.yscale('log')
# plt.show()
# df['SIC Code'].describe()


# %%
###### Histograms
# df = pd.read_csv('/Users/amankumarsaw/Documents/Prakash/ML/csv/industry_sic.csv')
# plt.yscale('log')
# # plt.xscale('log')
# plt.hist(df['SIC Code'])
# %%
###### Reading images
image = plt.imread('img/img1.png')
plt.imshow(image)
print(image)
plt.show()
# %%
image
# %%
print(type(image))
print(image.shape)
print(image.dtype)



# %%
###### Using seaborn library
### Seaborn is also a python library built on top of matplotlib. It creates much more attractive plots than matplot lib and often concise than matplotlib when we want to customize our plots, colors,grids,etc
import seaborn as sns
# %%
###### distplot (density plot)
sns.set_style('whitegrid')
df = pd.read_csv('csv/industry_sic.csv')
# sns.distplot(df['SIC Code']) ## distplot has been depricated
# sns.distplot(df['SIC Code'][:200],rug = True) # rug created small histograms
sns.distplot(df['SIC Code'],hist=False) # Density plot without histograms 
plt.show()

# %%
sns.displot(df['SIC Code'])
sns.histplot(df['SIC Code'])

# %%
print(df['SIC Code'])
# %%
# sns.boxplot(df['SIC Code'])
sns.boxplot(x=df['SIC Code'])


# %%
df = pd.read_csv('csv/shopping_trends.csv')
# plt.yscale('log')
# plt.hist(df['Customer ID'])
sns.jointplot(x='Customer ID',y='Age',data=df,kind="scatter")
sns.jointplot(x='Customer ID',y='Age',data=df,kind="hex")
sns.jointplot(x='Customer ID',y='Age',data=df,kind="kde")
# sns.jointplot(x='Customer ID',y='Age',data=df,kind="reg",dropna=True)
plt.show()

# %%
df = pd.read_csv('csv/shopping_trends.csv')
df = df[(df.Age>20)]
# plt.yscale('log')
# plt.hist(df['Customer ID'])
# sns.jointplot(x='Customer ID',y='Age',data=df,kind="scatter",color="brown")
sns.jointplot(x='Customer ID',y='Age',data=df,kind="hex",color="brown")




# %%
btc = pd.read_csv('csv/coin_Bitcoin.csv')
eth = pd.read_csv('csv/coin_Ethereum.csv')
aave = pd.read_csv('csv/coin_Aave.csv')
cardano = pd.read_csv('csv/coin_Cardano.csv')
chainlink = pd.read_csv('csv/coin_ChainLink.csv')
litecoin = pd.read_csv('csv/coin_Litecoin.csv')

btc.columns = btc.columns.map(lambda x:(x)+'btc')
eth.columns = eth.columns.map(lambda x:(x)+'eth')
aave.columns = aave.columns.map(lambda x:(x)+'aave')
cardano.columns = cardano.columns.map(lambda x:(x)+'cardano')
chainlink.columns = chainlink.columns.map(lambda x:(x)+'chainlink')
litecoin.columns = litecoin.columns.map(lambda x:(x)+'litecoin')
btc.head()
# eth.head()
# aave.head()
# cardano.head()
# chainlink.head()
# litecoin.head()

# %%
###### merging all the files by date
m1 = pd.merge(btc,eth,how='inner',left_on='Datebtc',right_on='Dateeth')
m2 = pd.merge(m1,aave,how='inner',left_on='Datebtc',right_on='Dateaave')
m3 = pd.merge(m2,cardano,how='inner',left_on='Datebtc',right_on='Datecardano')
m4 = pd.merge(m3,chainlink,how='inner',left_on='Datebtc',right_on='Datechainlink')
m5 = pd.merge(m4,litecoin,how='inner',left_on='Datebtc',right_on='Datelitecoin')
# m5 = pd.merge(m2,,how='inner',left_on='Datebtc',right_on='Datelitecoin')
m5.head()



# %%
###### Subsetting only the closing prices column for plotting
curr = m5[["Closebtc","Closeeth","Closeaave","Closecardano","Closechainlink","Closelitecoin"]]
curr.head()
# %%
sns.pairplot(curr)
# %%
###### Correlation among currencies
cor = curr.corr()
# round(cor,3) // For roundof upto 3 decimal places
cor
# %%
###### Heatmap
#### Heatmap shows the correlation between two data. Denser the color higher the correlation
sns.heatmap(cor,cmap="YlGnBu",annot = True) ## Here Yl(yellow will show lower correlation, Gn (green) will show moderate correlation) and Bu (Blue) will show higher correlation
# %%
