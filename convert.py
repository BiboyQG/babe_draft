import pandas as pd

# Read the Excel file
# data_market = pd.read_excel("stock_price_market100.xlsx", skiprows=[1, 2])

# # Convert the date column (assuming the date column is the first column)
# # If your date column has a different name, replace 'Date' with your column name
# column_name = 'Trddt'

# data_market[column_name] = pd.to_datetime(data_market[column_name]).dt.strftime('%Y-%m-%d')

# # Save the modified dataframe back to Excel
# data_market.to_excel("stock_price_market100_converted.xlsx", index=False)

data_securities = pd.read_excel("stock_price_securities100.xlsx", skiprows=[1, 2])
column_name = 'TradingDate'

data_securities[column_name] = pd.to_datetime(data_securities[column_name]).dt.strftime('%Y-%m-%d')
data_securities.to_excel("stock_price_securities100_converted.xlsx", index=False)
