import pandas as pd

# Load the uploaded Excel file
file_path = '/mnt/data/E1.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display the sheet names to understand the structure of the file
sheet_names = excel_data.sheet_names
sheet_names