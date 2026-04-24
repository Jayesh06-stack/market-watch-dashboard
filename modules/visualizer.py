import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(correlation_matrix,title='Correlation Matrix'):
  fig,ax=plt.subplots(figsize=(10,8))
  sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5,ax=ax)
  ax.set_title(title,fontsize=15)
  return fig

def plot_volatility_boxplot(daily_returns):
  fig,ax=plt.subplots(figsize=(10,8))
  sns.boxplot(data=daily_returns,ax=ax)
  ax.set_title('Distribution of Daily Returns (Volatility Check)')
  ax.set_ylabel('Percentage Change (%)')
  return fig

price_corr=pivoted_df.corr()

returns_df=pivoted_df.pct_change().dropna()
returns_corr=returns_df.corr()

def plot_comparison_heatmaps(price_corr,returns_corr):
  fig,(ax1,ax2)=plt.subplots(1,2,figsize=(20,8))

  sns.heatmap(price_corr, annot=True, cmap='Reds', fmt=".2f", ax=ax1)
  ax1.set_title('Price Correlation')

  sns.heatmap(returns_corr, annot=True, cmap='Blues', fmt=".2f", ax=ax2)
  ax2.set_title('Returns Correlation')

  return fig
