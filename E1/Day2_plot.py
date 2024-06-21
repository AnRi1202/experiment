import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import japanize_matplotlib

# Excelファイルの読み込み
file_path = './電界分布計算結果_202106修正 のコピー.xlsx'
excel_data = pd.ExcelFile(file_path)

sheet_name = 'gap=1.5mm'
df_gap_0_5mm = pd.read_excel(file_path, sheet_name=sheet_name)

# alphaの定義
def alpha(E, p):
    p *= 133.322
    E *= 1000
    if E / p < 31.6:
        return 0
    elif 31.6 <= E / p < 60.0:
        return (p / 10000) * (1.047 * (E / p - 28.5)**2 - 12.6)
    elif 60.0 <= E / p < 100.0:
        return (1.0 - 0.00674755 * (E / p - 60.0)) * (p / 10000) * (1.047 * (E / p - 28.5)**2 - 12.6)
    elif 100.0 <= E / p:
        return 15.0 * p * np.exp(-365 / (E / p))

# 距離の計算とNo.ごとの距離の和を求める
distances_sum = []

# 'No.'列でグループ化し、距離の和を計算
grouped = df_gap_0_5mm.groupby('No.')
for name, group in grouped:
    group = group.reset_index()
    total_distance = 0
    for i in range(len(group) - 1):
        r1, r2 = group.loc[i, 'r[cm]'], group.loc[i+1, 'r[cm]']
        z1, z2 = group.loc[i, 'z[cm]'], group.loc[i+1, 'z[cm]']
        d = np.sqrt((r2 - r1)**2 + (z2 - z1)**2)
        total_distance += d
    distances_sum.append({'No.': name, 'Total Distance': total_distance})

# 結果をデータフレームに変換
df_distances_sum = pd.DataFrame(distances_sum)
df_distances_sum.to_csv('distances_sum_data.csv', index=False)

# Kの計算関数
def calculate_K(E_multiplier, p, group):
    K = 0
    for i in range(len(group) - 1):
        r1, r2 = group.loc[i, 'r[cm]'], group.loc[i+1, 'r[cm]']
        z1, z2 = group.loc[i, 'z[cm]'], group.loc[i+1, 'z[cm]']
        Er = group.loc[i, 'Er[kV/cm]']
        Ez = group.loc[i, 'Ez[kV/cm]']
        E = np.sqrt(Er**2 + Ez**2) * E_multiplier
        d = np.sqrt((r2 - r1)**2 + (z2 - z1)**2)
        K += alpha(E, p) * d
    return K

# Eとpの範囲を設定
E_multipliers = np.linspace(0.05, 5, 30)  # 100 -> 20
p_values = np.linspace(0.01, 20, 10)      # 100 -> 20

# 結果を保存するリスト
results = []

# 各No.ごとにEとpの範囲でKを計算し、最初にKが10を超える点を収集
for name, group in grouped:
    group = group.reset_index()
    total_distance = df_distances_sum.loc[df_distances_sum['No.'] == name, 'Total Distance'].values[0]
    for p in p_values:
        for E_multiplier in E_multipliers:
            K = calculate_K(E_multiplier, p, group)
            if K > 10:
                results.append({'No.': name, 'E_multiplier': E_multiplier, 'p': p * 133.322, 'K': K, 'Total Distance': total_distance*10})
                break  # 最初の点を見つけたら次のpへ
        else:
            continue
        break

# 結果をデータフレームに変換
df_results = pd.DataFrame(results)

# 結果をCSVファイルに保存
df_results.to_csv('calculation_results.csv', index=False)

# p * Total Distanceを計算して新しい列に追加
df_results['p_distance'] = df_results['p'] * df_results['Total Distance']

# フォルダを作成（存在しない場合）
output_folder = 'graph'
os.makedirs(output_folder, exist_ok=True)

# プロット
plt.figure(figsize=(10, 6))
plt.scatter(df_results['p_distance'], df_results['E_multiplier'], color='blue', label='Data Points')
plt.xlabel('pd[Pa*mm]')
plt.ylabel('V(kV)')
# plt.title('Scatter Plot of V against pd[Pa*mm]')
plt.legend()
plt.grid(True)

# 画像を保存
output_file_path = os.path.join(output_folder, 'scatter_plot2.png')
plt.savefig(output_file_path)

# プロットを表示
plt.show()

print(f'プロットが保存されました: {output_file_path}')
