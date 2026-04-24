import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("CG_API_KEY")
if not API_KEY:
    print("Warning: API Key not found! Make sure .env is set up.")
BASE_URL="https://api.coingecko.com/api/v3"

def check_connection():
  endpoint=f"{BASE_URL}/ping"
  headers={
      "accept": "application/json",
      "x-cg-demo-api-key": API_KEY
  }

  try:
    response=requests.get(endpoint,headers=headers)
    if response.status_code==200:
      print("Success! Your API Key is active and connected")
      print(f"Server response: {response.json()}")
    else:
      print(f"Connection failed: Error Code {response.status_code}")
      print(response.text)
  except Exception as e:
    print(f"An error occured {e}")

check_connection()

def top_10_market_data():
  endpoint=f"{BASE_URL}/coins/markets"

  parameters={
      'vs_currency': 'inr',
      'order': 'market_cap_desc',
      'per_page': 10,
      'page': 1,
      'sparkline': 'false',
      'price_change_percentage': '24h'
  }

  headers={
        "accept": "application/json",
        "x-cg-demo-api-key": API_KEY
  }

  response=requests.get(endpoint,headers=headers,params=parameters)

  if response.status_code==200:
    data=response.json()
    df=pd.DataFrame(data)

    cols_to_keep=['market_cap_rank','name','symbol','current_price','market_cap','price_change_percentage_24h']
    return df[cols_to_keep]
  else:
    print(f"Error: {response.status_code}")
    return None

top_10_df=top_10_market_data()
if top_10_df is not None:
  print("---Top 10 coins by market cap---")
  display(top_10_df)

def get_historical_data(coin_list,days=30):
  all_history=[]
  headers={
      "accept": "application/json",
      "x-cg-demo-api-key": API_KEY
  }
  for coin in coin_list:
    print(f"Fetching 30-day history for {coin}")
    endpoint=f"{BASE_URL}/coins/{coin}/market_chart"
    params={
        'vs_currency':'inr',
        'days':days,
        'interval':'daily'
    }
    response=requests.get(endpoint,headers=headers,params=params)
    if response.status_code==200:
      data=response.json()
      prices=data['prices']

      temp_df=pd.DataFrame(prices,columns=['timestamp','price'])
      temp_df['coin_id']=coin

      temp_df['date']=pd.to_datetime(temp_df['timestamp'],unit='ms')

      all_history.append(temp_df[['date','coin_id','price']])
    else:
      print(f"Failed to fetch {coin}:{response.status_code}")

    time.sleep(2)

  if all_history:
    return pd.concat(all_history,ignore_index=True)
  return None

target_coins=['bitcoin','etherium','tether','solana','binancecoin']
historical_df=get_historical_data(target_coins)

if historical_df is not None:
    display(historical_df.head(10))
