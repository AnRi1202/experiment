import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os

energy_levels_c3piu = {
    "v": [4, 3, 2, 1, 0],
    "energy": [96900.5, 95105.8, 93231.8, 91291.3, 89297.4]
}

energy_levels_b3pig = {
    "v": [6, 5, 4, 3, 2, 1, 0],
    "energy": [69422.9, 67862.6, 66273.3, 64654.9, 63007.7, 61331.5, 59626.3]
}
energy_v_prime_0 = energy_levels_c3piu['energy'][4]

# v'' = 4 のエネルギーを取得 (インデックス 2)
energy_v_double_prime_2 = energy_levels_b3pig['energy'][4]

# エネルギー差の計算
energy_difference = energy_v_prime_0 - energy_v_double_prime_2

print(1/energy_difference*1e7) ##02




energy_v_prime_1 = energy_levels_c3piu['energy'][3]

# v'' = 4 のエネルギーを取得 (インデックス 2)
energy_v_double_prime_3 = energy_levels_b3pig['energy'][3]

# エネルギー差の計算
energy_difference = energy_v_prime_1 - energy_v_double_prime_3

print(1/energy_difference*1e7) ##13




energy_v_prime_2 = energy_levels_c3piu['energy'][2]

# v'' = 4 のエネルギーを取得 (インデックス 2)
energy_v_double_prime_4 = energy_levels_b3pig['energy'][2]

# エネルギー差の計算
energy_difference = energy_v_prime_2 - energy_v_double_prime_4

print(1/energy_difference*1e7) ##24




energy_v_prime_3 = energy_levels_c3piu['energy'][1]

# v'' = 4 のエネルギーを取得 (インデックス 2)
energy_v_double_prime_5 = energy_levels_b3pig['energy'][1]

# エネルギー差の計算
energy_difference = energy_v_prime_3 - energy_v_double_prime_5

print(1/energy_difference*1e7) ##35


# 波長データ
lambda02 = 380.37710586275233
lambda13 = 375.4261086332988
lambda24 = 370.9405196876681
lambda35 = 367.0640747048805

# 実際のファイルパスに置き換えてください
file_path_center = './chiba/5_center.csv'
file_path_side = './chiba/5_side.csv'

output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)

# CSVファイルの読み込みとプロット作成関数
def plot_spectrum(file_path, output_file_name, lambdas):
    # CSVファイルの読み込み
    df_spectrum = pd.read_csv(file_path, header=None, names=['wavelength', 'intensity'])

    # スペクトルのプロット
    plt.figure(figsize=(10, 6))
    plt.plot(df_spectrum['wavelength'], df_spectrum['intensity'], label='スペクトル')
    plt.xlabel('波長(nm)')
    plt.ylabel('強度')
    plt.title('スペクトルプロット')
    plt.xlim(300, 400)  # x軸の範囲を設定

    # 各lambdaに対して垂直線を引く
    for lambda_value in lambdas:
        plt.axvline(x=lambda_value, color='r', linestyle='--', label=f'{lambda_value:.1f} nm')

    plt.legend()
    plt.grid(True)

    # プロットをファイルに保存
    output_path = os.path.join(output_folder, output_file_name)
    plt.savefig(output_path)
    plt.show()

    print(f'グラフが保存されました: {output_path}')

# 中心部のスペクトル
plot_spectrum(file_path_center, 'N2_center.png', [lambda02, lambda13, lambda24, lambda35])

# 端部のスペクトル
plot_spectrum(file_path_side, 'N2_side.png', [lambda02, lambda13, lambda24, lambda35])
