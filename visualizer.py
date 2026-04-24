import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(correlation_matrix):
  plt.figure(figsize=(10,8))
  sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)

  plt.title('Crypto Correlation Matrix (Last 30 days)',fontsize=15)
  plt.show()

plot_correlation_heatmap(correlation_matrix)

plt.figure(figsize=(10,6))
sns.boxplot(data=daily_returns)
plt.title('Distribution of Daily Returns (Volatility Check)')
plt.ylabel('Percentage Change (%)')
plt.show()

price_corr=pivoted_df.corr()

returns_df=pivoted_df.pct_change().dropna()
returns_corr=returns_df.corr()

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(20,8))

sns.heatmap(price_corr, annot=True, cmap='Reds', fmt=".2f", ax=ax1)
ax1.set_title('Price Correlation')

sns.heatmap(returns_corr, annot=True, cmap='Blues', fmt=".2f", ax=ax2)
ax2.set_title('Returns Correlation')

plt.show()
