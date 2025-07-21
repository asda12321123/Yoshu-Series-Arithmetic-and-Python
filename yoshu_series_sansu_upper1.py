# Program Name: yoshu_series_sansu_upper1.py
# Creation Date: 20250721
# Overview: Solve arithmetic problems from Yoshu Series Grade 5 Upper Volume 1 (Sansu)
# Usage: Run the script to compute answers to modular arithmetic, distribution, and LCM-related questions

# 必要なライブラリのインストール（今回は不要） / No external libraries needed

# 最大公約数・最小公倍数の関数定義 / Define GCD and LCM functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 基本1: 6でも9でも2あまる2けたの整数を3つ / Find three two-digit numbers with remainder 2 for both 6 and 9
mod1 = 6
mod2 = 9
rem = 2
min_val = 10
max_val = 99
results1 = []
for n in range(min_val, max_val + 1):
    if n % mod1 == rem and n % mod2 == rem:
        results1.append(n)
        if len(results1) == 3:
            break

# 基本2 (1): 40枚を6人で配る（割り算の商と余り） / Divide 40 papers among 6 children
total_papers = 40
children = 6
papers_per_child = total_papers // children
remainder_papers = total_papers % children

# 基本2 (2): 5枚余るように配った最小の子ども人数 / Smallest number of children for 5 remainder
min_children = None
for i in range(1, total_papers):
    if total_papers % i == 5:
        min_children = i
        break

# 基本3 (1): Aは6秒、Bは16秒ごとに光る / Light A: every 6 sec, B: every 16 sec
interval_A = 6
interval_B = 16
lcm_AB = lcm(interval_A, interval_B)
second_flash_time = lcm_AB * 2  # 2回目の同時点灯

# 基本3 (2): 5分間での同時点灯回数 / Number of simultaneous flashes within 5 minutes
total_time = 5 * 60  # 5分 = 300秒
simultaneous_flash_count = total_time // lcm_AB

# 基本4 (1): 5で2あまり6で4あまる数の最小値 / Smallest number satisfying both mod conditions
mod_a = 5
rem_a = 2
mod_b = 6
rem_b = 4
n = 1
while True:
    if n % mod_a == rem_a and n % mod_b == rem_b:
        first_match = n
        break
    n += 1

# 基本4 (2): 同じ性質を持つ数を6個列挙 / 6 numbers with same modular conditions
lcm_ab = lcm(mod_a, mod_b)
results4 = [first_match + i * lcm_ab for i in range(6)]

# 基本5: 1〜1000の中で12の倍数でも16の倍数でもない数の個数 / Count integers not multiple of 12 or 16
start = 1
end = 1000
multiple_1 = 12
multiple_2 = 16
count_12 = end // multiple_1
count_16 = end // multiple_2
lcm_12_16 = lcm(multiple_1, multiple_2)
count_both = end // lcm_12_16
count_either = count_12 + count_16 - count_both
not_multiple_count = end - count_either

# 結果の出力 / Print all results
print("基本1:", results1)
print("基本2 (1):", papers_per_child, "枚ずつ", remainder_papers, "枚あまり")
print("基本2 (2):", min_children, "人")
print("基本3 (1):", second_flash_time, "秒後")
print("基本3 (2):", simultaneous_flash_count, "回")
print("基本4 (1):", first_match)
print("基本4 (2):", results4)
print("基本5:", not_multiple_count, "個")
