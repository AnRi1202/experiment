import numpy as np
import matplotlib.pyplot as plt
import os


# データの定義
I_side = [2500, 8200, 10000]
I_center = [4000, 14000, 16000]

A_values = {
    'SP13': 4.93e6,
    'SP24': 4.07e6,
    'SP35': 2.40e6
}

E_values = {
    'SP13': 95105.8,
    'SP24': 93231.8,
    'SP35': 91291.3
}

# 各遷移に対応するデータ
I_side_values = {
    'SP13': 10000,
    'SP24': 8200,
    'SP35': 2500
}

I_center_values = {
    'SP13': 16000,
    'SP24': 14000,
    'SP35': 4000
}

# 計算関数
def calculate_temperature_and_plot(I_values, A_values, E_values, label):
    ln_I_A = {key: np.log(I_values[key] / A_values[key]) for key in I_values}
    E_values = {key: E_values[key] for key in I_values}
    
    # y = mx + b の形式で回帰直線を求める
    x = np.array([E_values[key] for key in I_values])
    y = np.array([ln_I_A[key] for key in I_values])
    m, b = np.polyfit(x, y, 1)
    
    # 温度 T の計算
    T = -1.4388 / m
    
    # プロット
    plt.scatter(x, y, label=label + ' Data')
    # plt.plot(x, m * x + b, label=label + f' Fit: T = {T:.2f} K')
    
    return T

# プロットの設定
plt.figure(figsize=(10, 6))
plt.xlabel('$E_{v\'}$ (cm$^{-1}$)')
plt.ylabel('ln($I_{v\'\'}/A_{v\'\'}$)')

# 温度の計算とプロット
T_side = calculate_temperature_and_plot(I_side_values, A_values, E_values, 'Side')
T_center = calculate_temperature_and_plot(I_center_values, A_values, E_values, 'Center')

plt.legend()
# plt.title('Boltzmann Plot for Temperature Calculation')
plt.grid(True)

# プロットの表示
output_folder = 'bunko_graph'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, 'boltzmann_plot.png')
plt.savefig(output_path)
plt.show()

print(f'Sideの温度: {T_side:.2f} K')
print(f'Centerの温度: {T_center:.2f} K')
print(f'プロットが保存されました: {output_path}')
