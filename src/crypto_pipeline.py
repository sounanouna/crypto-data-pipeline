import requests
import pandas as pd

# Step 1: Fetching data from CoinGecko API

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    params = {
        "vs_currency" : "usd",
        "order" : "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Step 2: Processing the data

def process_crypto_data(data):
    df = pd.DataFrame(data)
    selected_columns = ['id', 
                        'symbol', 
                        'name', 
                        'current_price', 
                        'market_cap', 
                        'market_cap_rank', 
                        'total_volume' , 
                        'price_change_percentage_24h', 
                        'last_updated']
    df_clean = df[selected_columns]
    return df_clean

# Step 3: Saving the data to a CSV file

def save_to_csv(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
        crypto_data = fetch_crypto_data()
        cleaned_data = process_crypto_data(crypto_data)
        save_to_csv(cleaned_data, 'data/crypto_market_data.csv')
        print("Crypto market data pipeline completed successfully.")

print(cleaned_data.head())
print(cleaned_data.columns)
print(cleaned_data.shape)


    