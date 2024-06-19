import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルの読み込み
file_path = 'calculation_results.csv'
df_results = pd.read_csv(file_path)

# p * Total Distanceを計算して新しい列に追加
df_results['p_distance'] = df_results['p'] * df_results['Total Distance']

# Kが10より大きい値をフィルタリング
filtered_df = df_results[df_results['K'] > 10]

# 各pの値ごとにフィルタリングして、p_distanceごとにE_multiplierが最も小さいものを抽出
results = []
for p_value in filtered_df['p'].unique():
    df_p = filtered_df[filtered_df['p'] == p_value]
    min_E_per_p_distance = df_p.loc[df_p.groupby('p_distance')['E_multiplier'].idxmin()]
    results.append(min_E_per_p_distance)

# 結果を結合
final_results = pd.concat(results)

# プロット
plt.figure(figsize=(10, 6))
plt.scatter(final_results['p_distance'], final_results['E_multiplier'], color='blue', label='Data Points')
plt.xlabel('p * Total Distance')
plt.ylabel('V = E_multiplier')
plt.title('Scatter Plot of V = E_multiplier against p * Total Distance')
plt.legend()
plt.grid(True)
plt.show()