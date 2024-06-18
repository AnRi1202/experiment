import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
# Load the uploaded Excel file
file_path = './E1.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display the sheet names to understand the structure of the file
sheet_names = excel_data.sheet_names


df_spark_voltage_small = pd.read_excel(file_path, sheet_name='火花電圧(pd小)')

# Display the first few rows of the DataFrame to understand its structure
print(df_spark_voltage_small.head())



# Extract the relevant columns for plotting, handling invalid values
pd_values = pd.to_numeric(df_spark_voltage_small.iloc[2, 1:], errors='coerce')
vs_values = pd.to_numeric(df_spark_voltage_small.iloc[3, 1:], errors='coerce')

# Drop NaN values caused by invalid entries
valid_indices = pd_values.notna() & vs_values.notna()
pd_values = pd_values[valid_indices]
vs_values = vs_values[valid_indices]

# Plotting pd vs Vs
output_folder = './graph'
output_file = f'{output_folder}/pd_vs_vs.png'

# Create the folder if it doesn't exist
import os
os.makedirs(output_folder, exist_ok=True)

# Plotting pd vs Vs with Japanese labels and legend
plt.figure(figsize=(10, 6))
plt.scatter(pd_values, vs_values, marker='o', label='火花電圧')
plt.xlabel('pd[Pa・mm]')
plt.ylabel('Vs(平均)[kV]')
plt.title('pdとVsの関係')
plt.legend()
plt.grid(True)
plt.savefig(output_file)
plt.show()

output_file

