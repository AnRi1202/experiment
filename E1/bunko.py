import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

output_folder = 'graph'
os.makedirs(output_folder, exist_ok=True)
# 正の直流のデータ
data_dc_positive = {
    'd': [40.0, 20.0, 8.0, 6.0, 10.0, 4.0],
    'v2': [38.25, 26.03, 14.84, 13.48, 18.02, 6.16],
    'v1': [25.83, 16.35, 11.73, 9.31, 12.21, None] 
}

# 負の直流のデータ
data_dc_negative = {
    'd': [20, 10, 8, 6, 4],
    'v1': [12.787, 9.255, 8.17, 7.463, 6.193],
    'v2': [43.333, 22.478, 17.58, 13.34, 8.97]
}

# 交流のデータ
data_ac = {
    'd': [20, 10, 6],
    'v1': [15.767, 11.17, 8.557],
    'v2': [25.1, 16.88, 10.593]
}

# データフレームの作成
df_dc_positive = pd.DataFrame(data_dc_positive)
df_dc_negative = pd.DataFrame(data_dc_negative)
df_ac = pd.DataFrame(data_ac)

# グラフの作成
plt.figure(figsize=(10, 6))

# 正の直流のプロット
plt.scatter(df_dc_positive['d'], df_dc_positive['v1'], marker='o', label='v1 (正 - コロナ)')
plt.scatter(df_dc_positive['d'], df_dc_positive['v2'], marker='x', label='v2 (正 - 火花)')

# 負の直流のプロット
plt.scatter(df_dc_negative['d'], df_dc_negative['v1'], marker='o', linestyle='--', label='v1 (負 - コロナ)')
plt.scatter(df_dc_negative['d'], df_dc_negative['v2'], marker='x', linestyle='--', label='v2 (負 - 火花)')

# 交流のプロット
plt.scatter(df_ac['d'], df_ac['v1'], marker='o', linestyle=':', label='v1 (交流 - コロナ)')
plt.scatter(df_ac['d'], df_ac['v2'], marker='x', linestyle=':', label='v2 (交流 - 火花)')

plt.xlabel('d')
plt.ylabel('Values')
# plt.title('dとv1, v2の関係 (正, 負, 交流)')
plt.legend()
plt.grid(True)

# グラフを表示
output_path = os.path.join(output_folder, 'd_v1_v2_plot.png')
plt.savefig(output_path)
plt.show()
