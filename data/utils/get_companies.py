import os
import pandas as pd
import yfinance as yf

def history():
  '''
  Fetches historical stock data for JKSE and a list of Indonesian companies
  (appending '.JK' to their codes) for the past 2 years and concatenates
  them into a single DataFrame.
  '''

  #check file integrity
  company_list = "/content/Portfolio-Tracker/data/tracked_companies/company_names.csv"
  if not os.path.exists(company_list):
    raise ValueError(f"    Error: The file '{company_list}' DOES NOT exist at the specified path.")

  # Load the company list into a DataFrame
  try:
    company_list = pd.read_csv(company_list)
  except Exception as e:
    raise ValueError(f"Error reading CSV file '{company_list}': {e}")

  if "code" not in company_list.columns:
    raise ValueError(f"    Error: 'code' column not found in '{company_list}'.")

  company_list = [company + ".JK" for company in company_list["code"].tolist()]

  #get historical data
  historical_data = yf.Ticker("^JKSE")
  historical_data = pd.DataFrame(historical_data.history(period="2y"))
  historical_data["code"] = 'JKSE'
  
  for company in company_list:
    try:
      temp = yf.Ticker(company)
      temp = pd.DataFrame(temp.history(period='2y'))
      if not temp.empty and isinstance(temp, pd.DataFrame):
        temp["code"] = company
        historical_data = pd.concat([historical_data, temp])
      else:
        print(f"    No data found or error fetching data for {company}. Skipping.")

    except Exception as e:
      print(f"    Error fetching data for {company}: {e}. Skipping this ticker.")

  return historical_data
  
