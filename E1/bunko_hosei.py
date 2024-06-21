import os
import japanize_matplotlib
import matplotlib.pyplot as plt 
import pandas as pd
# フォルダを作成（存在しない場合）
output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# Load the necessary data again
file_path = 'E1.xlsx'
csv_file_path = 'chiba/5_center.csv'

# Load the "波長感度" sheet
wavelength_sensitivity_data = pd.read_excel(file_path, sheet_name='波長感度', skiprows=6)

# Load the CSV file
csv_data = pd.read_csv(csv_file_path)

# Rename the columns for clarity
csv_data.columns = ['Wavelength', 'Intensity']

# Convert the relevant columns to numeric, ensuring any errors are coerced
csv_data['Wavelength'] = pd.to_numeric(csv_data['Wavelength'], errors='coerce')
csv_data['Intensity'] = pd.to_numeric(csv_data['Intensity'], errors='coerce')

# Drop any rows with NaN values in these columns
csv_data.dropna(subset=['Wavelength', 'Intensity'], inplace=True)

# Extract the sensitivity data, ensuring proper column names and data types
wavelength_sensitivity_data.columns = ['Wavelength', 'Sensitivity']
wavelength_sensitivity_data['Wavelength'] = pd.to_numeric(wavelength_sensitivity_data['Wavelength'], errors='coerce')
wavelength_sensitivity_data['Sensitivity'] = pd.to_numeric(wavelength_sensitivity_data['Sensitivity'], errors='coerce')

# Drop any rows with NaN values in these columns
wavelength_sensitivity_data.dropna(subset=['Wavelength', 'Sensitivity'], inplace=True)

# Merge the CSV data with the sensitivity data on the 'Wavelength' column
merged_data = pd.merge(csv_data, wavelength_sensitivity_data, on='Wavelength')

# Normalize the intensity values
merged_data['Normalized_Intensity'] = merged_data['Intensity'] / merged_data['Sensitivity']




# Plot the normalized intensities
plt.figure(figsize=(10, 6))
plt.plot(merged_data['Wavelength'], merged_data['Normalized_Intensity'], label='規格化された強度')
plt.xlabel('波長 (nm)')
plt.ylabel('規格化された強度')
plt.title('波長に対する規格化された強度')
plt.legend()
plt.grid(True)



# Plot the original intensity values and normalized intensities on the same graph
plt.figure(figsize=(10, 6))
plt.plot(merged_data['Wavelength'], merged_data['Intensity'], label='元の強度', alpha=0.7)
plt.plot(merged_data['Wavelength'], merged_data['Normalized_Intensity'], label='規格化された強度', alpha=0.7)
plt.xlabel('波長 (nm)')
plt.ylabel('強度')
plt.title('波長に対する強度と規格化された強度')
plt.legend()
plt.grid(True)

# Save the plot to the specified folder
plot_path_combined = os.path.join(output_folder, 'combined_intensity_plot.png')
plt.savefig(plot_path_combined)
plt.close()

plot_path_combined

# Save the plot to the specified folder
plot_path = os.path.join(output_folder, 'normalized_intensity_plot.png')
plt.savefig(plot_path)


plt.close()

plot_path
