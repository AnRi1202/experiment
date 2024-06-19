import pandas as pd
import numpy as np



# Excelファイルの読み込み
file_path = './電界分布計算結果_202106修正 のコピー.xlsx'
excel_data = pd.ExcelFile(file_path)

# 指定シートのデータを取得
sheet_name = 'gap=0.5mm'
df_gap_0_5mm = pd.read_excel(file_path, sheet_name=sheet_name)

# alphaの定義
def alpha(E, p):
    p *= 133.322
    E *= 1000
    if p == 0:
        return 0
    elif E / p < 31.6:
        return 0
    elif 31.6 <= E / p < 60.0:
        return (p / 10000) * (1.047 * (E / p - 28.5)**2 - 12.6)
    elif 60.0 <= E / p < 100.0:
        return (1.0 - 0.00674755 * (E / p - 60.0)) * (p / 10000) * (1.047 * (E / p - 28.5)**2 - 12.6)
    elif 100.0 <= E / p:
        return 15.0 * p * np.exp(-365 / (E / p))
    return 0

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
        a = alpha(E, p)
        K += a * d
    return K

# E_multiplierとpの固定値を設定
E_multiplier = 5.0
p = 5.0

# 結果を保存するリスト
results = []

# 'No.'列でグループ化し、各グループごとにKを計算
grouped = df_gap_0_5mm.groupby('No.')
for name, group in grouped:
    group = group.reset_index()
    K = calculate_K(E_multiplier, p, group)
    results.append({'No.': name, 'K': K})

# 結果をデータフレームに変換
df_results = pd.DataFrame(results)

# Kの値を出力
print(df_results)
