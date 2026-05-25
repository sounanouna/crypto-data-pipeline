# Crypto Market Data Pipeline

## Project Overview

This is a beginner data engineering project that pulls cryptocurrency market data from the CoinGecko API, transforms it using pandas, and saves the cleaned result as a CSV file.

## Objective

The goal of this project is to practice the basic building blocks of a data pipeline:

- API extraction
- JSON inspection
- DataFrame creation
- Data cleaning
- CSV export
- Project organization
- GitHub publishing

## Tools Used

- Python
- requests
- pandas
- CoinGecko API
- VS Code
- GitHub

## Pipeline Steps

1. Send request to the CoinGecko API
2. Receive JSON response
3. Convert JSON into a pandas DataFrame
4. Select useful columns
5. Save cleaned data to CSV

## Project Structure

```text
crypto-data-pipeline/
|
|-- data/
|   |-- crypto_market_data.csv
|
|-- src/
|   |-- crypto_pipeline.py
|
|-- README.md
|-- requirements.txt
|-- .gitignore
```

## How to Run

install the required packages:

```bash
pip3 install -r requirements.txt

```
