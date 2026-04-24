import streamlit as st
from modules.fetcher import get_historical_data
from modules.processor import process_market_data
from modules.visualizer import plot_comparison_heatmaps, plot_volatility_boxplot

st.set_page_config(page_title="Market-Watch",layout="wide")

def main():
  st.title("Market Watch Analytics Dashboard")

  st.sidebar.header("Control Panel")
  target_coins=['bitcoin','ethereum','tether','solana','binancecoin']
  days=st.sidebar.slider("Days of history:",7,90,30)

  if(st.sidebar.button("Fetch and analyze")):
     with(st.spinner("Accessing API and Processing Data:"):
        raw_data=get_historical_data(target_coins,days=days)

        if raw_data is not None:
          pivoted,returns,corr=process_market_data(raw_data)

          st.subheader("Price v/s Returns Correlation")
          fig_corr=plot_comparison_heatmaps(pivoted_corr(),corr)
          st.pyplot(fig_corr)

          st.subheader("Volatility Distribution")
          fig_vol = plot_volatility_boxplot(returns)
          st.pyplot(fig_vol)
        else:
          st.error("Failed to retrieve data. Check your API key or connection.")

if __name__=="__main__":
  main()
