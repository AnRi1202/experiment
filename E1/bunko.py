import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

file_path = './chiba/1_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '1_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')






file_path = './chiba/1_side.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '1_side_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')






file_path = './chiba/2_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '2_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')








file_path = './chiba/3_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '3_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')







file_path = './chiba/4_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '4_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')






file_path = './chiba/5_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '5_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')






file_path = './chiba/5_side.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '5_side_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')





file_path = './chiba/6_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '6_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')


############################################################################################################################################





file_path = './chiba/black.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, 'black_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')





file_path = './chiba/black.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, 'black_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')


