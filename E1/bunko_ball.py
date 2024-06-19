import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
from scipy.signal import find_peaks

file_path = './chiba/plasma_ball.csv'  # 実際のファイルパスに置き換えてください

# CSVファイルの読み込み
df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

# データの表示
print(df_spectrum.head())

# 極大値（ピーク）の検出
peaks, _ = find_peaks(df_spectrum['intensity'])

# 検出されたピークの強度を取得
peak_intensities = df_spectrum['intensity'][peaks]

# 上位15個のピークのインデックスを取得
top_15_peak_indices = peak_intensities.nlargest(15).index

# 上位15個のピークの波長を取得
top_15_wavelengths = df_spectrum['wavelength'].iloc[top_15_peak_indices].values
print("上位15個の極大値の波長:", top_15_wavelengths)

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

# 上位15個の極大値に縦線を描画
for wavelength in top_15_wavelengths:
    plt.axvline(x=wavelength, color='red', linestyle='--')

# プロットをファイルに保存
output_path = os.path.join(output_folder, 'plasma_ball_plot.png')
plt.savefig(output_path)
plt.show()

print(f'グラフが保存されました: {output_path}')
print(f'上位15個の極大値の波長: {top_15_wavelengths}')


#700.57  582.478 820.758 637.488 635.605 611.566 584.979
