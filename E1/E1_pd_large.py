import pandas as pd
import matplotlib.pyplot as plt
import os
import japanize_matplotlib

# ファイルパス
file_path = 'E1.xlsx'
output_folder = 'graph'


# フォルダを作成（存在しない場合）
os.makedirs(output_folder, exist_ok=True)

# シート '火花電圧(pd大)' の読み込み
df_spark_voltage_large = pd.read_excel(file_path, sheet_name='火花電圧(pd大)')

# ラベルの文字サイズ
label_fontsize = 20
tick_fontsize = 18

# DとF列のデータ抽出とプロット
d_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 3], errors='coerce').dropna()
f_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 5], errors='coerce').dropna()
plt.figure(figsize=(10, 6))
plt.scatter(d_values, f_values)
plt.xlabel('pd[Pa・mm]', fontsize=label_fontsize)
plt.ylabel('V(kV)', fontsize=label_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
# plt.title('d = 1(mm)')
plt.legend(fontsize=label_fontsize)
plt.grid(True)
output_file_df = f'{output_folder}/pd_vs_V_d1.png'
plt.savefig(output_file_df)
plt.show()

# IとK列のデータ抽出とプロット
i_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 8], errors='coerce').dropna()
k_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 10], errors='coerce').dropna()
plt.figure(figsize=(10, 6))
plt.scatter(i_values, k_values)
plt.xlabel('pd[Pa・mm]', fontsize=label_fontsize)
plt.ylabel('V(kV)', fontsize=label_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
# plt.title('d =2(mm)')
plt.legend(fontsize=label_fontsize)
plt.grid(True)
output_file_ik = f'{output_folder}/pd_vs_V_d2.png'
plt.savefig(output_file_ik)
plt.show()

# NとP列のデータ抽出とプロット
n_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 13], errors='coerce').dropna()
p_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 15], errors='coerce').dropna()
plt.figure(figsize=(10, 6))
plt.scatter(n_values, p_values)
plt.xlabel('pd[Pa・mm]', fontsize=label_fontsize)
plt.ylabel('V(kV)', fontsize=label_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
# plt.title('d = 5(mm)')
plt.legend(fontsize=label_fontsize)
plt.grid(True)
output_file_np = f'{output_folder}/pd_vs_V_d5.png'
plt.savefig(output_file_np)
plt.show()

print(f'DとF列のグラフ: {output_file_df}')
print(f'IとK列のグラフ: {output_file_ik}')
print(f'NとP列のグラフ: {output_file_np}')


import pandas as pd
import matplotlib.pyplot as plt
import os
import japanize_matplotlib

# ファイルパス
file_path = 'E1.xlsx'
output_folder = 'graph'

# フォルダを作成（存在しない場合）
os.makedirs(output_folder, exist_ok=True)

# シート '火花電圧(pd大)' の読み込み
df_spark_voltage_large = pd.read_excel(file_path, sheet_name='火花電圧(pd大)')

# ラベルの文字サイズ
label_fontsize = 20
tick_fontsize = 18

# プロット
plt.figure(figsize=(12, 8))

# DとF列のデータ抽出とプロット
d_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 3], errors='coerce').dropna()
f_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 5], errors='coerce').dropna()
plt.scatter(d_values, f_values, label='(d = 1mm)', alpha=0.7)

# IとK列のデータ抽出とプロット
i_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 8], errors='coerce').dropna()
k_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 10], errors='coerce').dropna()
plt.scatter(i_values, k_values, label='(d = 2mm)', alpha=0.7)

# NとP列のデータ抽出とプロット
n_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 13], errors='coerce').dropna()
p_values = pd.to_numeric(df_spark_voltage_large.iloc[:, 15], errors='coerce').dropna()
plt.scatter(n_values, p_values, label='(d = 5mm)', alpha=0.7)

# グラフの設定
plt.xlabel('pd[Pa・mm]', fontsize=label_fontsize)
plt.ylabel('V(kV)', fontsize=label_fontsize)
plt.xticks(fontsize=tick_fontsize)
plt.yticks(fontsize=tick_fontsize)
plt.legend(fontsize=label_fontsize)
plt.grid(True)

# グラフの保存
output_file_combined = f'{output_folder}/pd_vs_V_combined.png'
plt.savefig(output_file_combined)
plt.show()
