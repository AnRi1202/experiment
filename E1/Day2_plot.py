import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVファイルの読み込み
file_path = 'calculation_results.csv'
df_results = pd.read_csv(file_path)

# 初めの5点を抽出
df_results = df_results.head(5)

# p * Total Distanceを計算して新しい列に追加
df_results['p_distance'] = df_results['p'] * df_results['Total Distance']

# 横軸をp * Total Distance、縦軸をE_multiplierとしてプロット
plt.figure(figsize=(10, 6))
plt.scatter(df_results['p_distance'], df_results['E_multiplier'], color='blue', label='Data Points')
plt.xlabel('p * Total Distance')
plt.ylabel('V = E_multiplier')
plt.title('Scatter Plot of V = E_multiplier against p * Total Distance')
plt.legend()
plt.grid(True)
plt.show()