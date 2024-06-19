import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

file_path = './chiba/1_center.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# bunko_graphフォルダを作成（存在しない場合）
output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# 水素の理論スペクトルの波長（nm）
h2_lines = {
    '656 nm': 656,
    '486 nm': 486
}
he_lines={
  '588 nm': 588,
  '668 nm': 668,
  '502 nm': 502
}
n2_lines={
  '315 nm': 315,
  '337 nm': 337,
  '357 nm': 357
}
ne_lines={
  '584 nm': 584,
  '640 nm': 640,
  '703 nm': 703
}
ar_lines = {
    '750 nm': 750,
    '763 nm': 763
}
xe_lines = {
    '823 nm': 823,
    '828 nm': 828
}


# スペクトルのプロット
plt.figure(figsize=(10, 6))
plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='測定スペクトル', color='blue')
plt.xlabel('波長(nm)')
plt.ylabel('強度')
plt.title('スペクトルプロット')

# 水素の理論スペクトルを点線でプロット
for line_name, wavelength in he_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'He線 ({line_name})')

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

for line_name, wavelength in he_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'He線 ({line_name})')

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

for line_name, wavelength in h2_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'H2線 ({line_name})')
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



for line_name, wavelength in ar_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'Ar線 ({line_name})')
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


for line_name, wavelength in ne_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'Ne線 ({line_name})')
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

for line_name, wavelength in n2_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'N2線 ({line_name})')
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

for line_name, wavelength in n2_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'N2線 ({line_name})')
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

for line_name, wavelength in xe_lines.items():
    plt.axvline(x=wavelength, color='red', linestyle='--', label=f'Xe線 ({line_name})')
plt.legend()
plt.grid(True)

# プロットをファイルに保存
output_path = os.path.join(output_folder, '6_center_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')


################################################################################################################################################################################





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








