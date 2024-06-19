import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

def plot_spectrum(file_path, color_name):
    # CSVファイルの読み込み
    df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])
    
    output_folder = 'bunko_graph'
    os.makedirs(output_folder, exist_ok=True)
    
    # スペクトルのプロット
    plt.figure(figsize=(10, 6))
    plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
    plt.xlabel('波長(nm)')
    plt.ylabel('強度')
    plt.title(f'{color_name}のスペクトルプロット')
    plt.legend()
    plt.grid(True)
    
    # プロットをファイルに保存
    output_path = os.path.join(output_folder, f'{color_name}_plot.png')
    plt.savefig(output_path)
    plt.show()
    
    print(f'グラフが保存されました: {output_path}')

# ファイルパスと色の名前のリスト
file_color_pairs = [
    ('./chiba/black.csv', 'black'),
    ('./chiba/blue.csv', 'blue'),
    ('./chiba/cyan.csv', 'cyan'),
    ('./chiba/green.csv', 'green'),
    ('./chiba/magenta.csv', 'magenta'),
    ('./chiba/red.csv', 'red'),
    ('./chiba/white.csv', 'white'),
    ('./chiba/yellow.csv', 'yellow')
]

# 各ファイルについてプロット
for file_path, color_name in file_color_pairs:
    plot_spectrum(file_path, color_name)



