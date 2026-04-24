def pivot_market_data(df):
  pivot_df=df.pivot(index='date',columns='coin_id',values='price')
  pivot_df=pivot_df.ffill()
  return pivot_df

pivoted_df=pivot_market_data(historical_df)
print("---Pivoted data (Wide Format)---")
display(pivoted_df.head())

correlation_matrix=pivoted_df.corr()
print("---Correlation Matrix---")
display(correlation_matrix)

def calculate_daily_returns(df):
  returns_df=df.pct_change()
  returns_df=returns_df.dropna()
  returns_df_pct=returns_df*100
  return returns_df_pct

daily_returns=calculate_daily_returns(pivoted_df)
print('---Daily Returns (Percentage Change)---')
display(daily_returns.head())

