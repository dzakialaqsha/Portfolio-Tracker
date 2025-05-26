import os
import pandas as pd
import yfinance as yf
import datetime as dt

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
      if not temp.empty:
        temp["code"] = company
        historical_data = pd.concat([historical_data, temp])
      else:
        print(f"    No data found or error fetching data for {company}. Skipping.")

    except Exception as e:
      print(f"    Error fetching data for {company}: {e}. Skipping this ticker.")

  output_path = "/content/Portfolio-Tracker/data/tracked_companies/historical_data.csv"
  try:
    historical_data.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def quarters_income():
  '''
  Fetches quarterly income statements for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.quarterly_income_stmt).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.quarterly_income_stmt).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/quarters_is_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def quarters_balance():
  '''
  Fetches quarterly balance sheets for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.quarterly_balancesheet).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.quarterly_balancesheet).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/quarters_bs_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def quarters_cf():
  '''
  Fetches quarterly cash flow statements for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.quarterly_cashflow).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.quarterly_cashflow).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year) + "_" + str(col.quarter)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/quarters_cf_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def ann_income():
  '''
  Fetches annual income statements for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.income_stmt).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.income_stmt).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/ann_is_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def ann_balance():
  '''
  Fetches annual balance sheets for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.balancesheet).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.balancesheet).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/ann_bs_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")

def ann_cf():
  '''
  Fetches annual cash flow statements for a list of tracked companies from yfinance,
  processes and standardizes their column names to a 'YYYY_Qn' format (e.g., '2024_1', '2024_4'),
  and concatenates them into a single DataFrame. The resulting combined data
  is then saved to a CSV file.
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

  for i in range(len(company_list)):
    if i == 0:
      first = yf.Ticker(company_list[i])
      first = pd.DataFrame(first.cashflow).reset_index()
      colnames = first.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      first.rename(columns=col_dict, inplace=True)
      first['code']=company_list[i]
    else:
      temp = yf.Ticker(company_list[i])
      temp = pd.DataFrame(temp.cashflow).reset_index()
      colnames = temp.columns[1:]
      colnames = [col for col in colnames]
      col_dict = dict()
      col_dict['index'] = 'accounts'
      for col in colnames:
        col_dict[col] = str(col.year)
      temp.rename(columns=col_dict, inplace=True)
      temp['code']=company_list[i]
      first = pd.concat([first, temp])
  output_path = "/content/Portfolio-Tracker/data/tracked_companies/ann_cf_data.csv"
  try:
    first.to_csv(output_path, index=False)
  except Exception as e:
    print(f"\nError saving historical data to CSV: {e}")
