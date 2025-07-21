# Program Name: yoshu_series_sansu_upper1.py
# Creation Date: 20250721
# Overview: Solve arithmetic problems from Yoshu Series Grade 5 Upper Volume 1 (Sansu)
# Usage: Run the script to compute answers to modular arithmetic, distribution, and LCM-related questions

# 必要なライブラリのインストール（今回は不要） / No external libraries needed

# 最大公約数・最小公倍数の関数定義 / Define GCD and LCM functions
def gcd(a, b):
    # bが0になるまで繰り返す / Repeat until remainder becomes 0
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # LCM = |a*b| / GCD / Least common multiple from GCD
    return abs(a * b) // gcd(a, b)

# 基本1: 6でも9でも2あまる2けたの整数を3つ求める / Find three two-digit numbers with remainder 2 for both 6 and 9
mod1 = 6  # 6で割る
mod2 = 9  # 9で割る
rem = 2   # あまり2 / remainder is 2
min_val = 10  # 2けたの最小値
max_val = 99  # 2けたの最大値
results1 = []  # 結果を格納するリスト / List to store results

for n in range(min_val, max_val + 1):
    if n % mod1 == rem and n % mod2 == rem:
        results1.append(n)
        if len(results1) == 3:  # 最初の3つが見つかったら終了 / Stop after finding 3
            break

# 基本2 (1): 40枚の折り紙を6人でできるだけ均等に分ける / Divide 40 papers among 6 children
total_papers = 40  # 総枚数 / Total sheets
children = 6       # 子どもの人数 / Number of children
papers_per_child = total_papers // children  # 1人あたりの枚数 / Papers per child
remainder_papers = total_papers % children   # あまり / Remainder

# 基本2 (2): 5枚あまったときの最小の子ども人数を求める / Find minimum number of children with remainder 5
min_children = None
for i in range(1, total_papers):
    if total_papers % i == 5:
        min_children = i
        break

# 基本3 (1): Aは6秒ごと、Bは16秒ごとに光る / A every 6s, B every 16s
interval_A = 6
interval_B = 16
lcm_AB = lcm(interval_A, interval_B)  # 最初に同時に光るのはLCM秒後 / First simultaneous flash
second_flash_time = lcm_AB * 2        # 2回目はその倍の時間 / Second simultaneous flash

# 基本3 (2): 5分間（300秒）での同時点灯回数を求める / How many times they flash together in 5 minutes
total_time = 5 * 60  # 5分 = 300秒
simultaneous_flash_count = total_time // lcm_AB  # LCMの倍数が同時点灯

# 基本4 (1): 5で2あまり6で4あまる数のうち最小のものを探す / Find smallest number with remainders 2 and 4
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

# 基本4 (2): 上記と同じ性質を持つ数を6個求める / Find next 6 numbers with same modular properties
lcm_ab = lcm(mod_a, mod_b)  # 5と6の最小公倍数で数列を構築 / Use LCM to get next values
results4 = [first_match + i * lcm_ab for i in range(6)]

# 基本5: 1〜1000の中で12の倍数でも16の倍数でもない数の個数を求める / Count numbers not multiple of 12 or 16
start = 1
end = 1000
multiple_1 = 12
multiple_2 = 16
count_12 = end // multiple_1  # 12の倍数の数 / Multiples of 12
count_16 = end // multiple_2  # 16の倍数の数 / Multiples of 16
lcm_12_16 = lcm(multiple_1, multiple_2)  # 共通の倍数（重複）/ Common multiples
count_both = end // lcm_12_16  # 両方の倍数
count_either = count_12 + count_16 - count_both  # いずれかの倍数の合計 / Union count
not_multiple_count = end - count_either  # 両方の倍数でない数の個数 / Complement count

# 結果の出力 / Print all results
print("基本1:", results1)
print("基本2 (1):", papers_per_child, "枚ずつ", remainder_papers, "枚あまり")
print("基本2 (2):", min_children, "人")
print("基本3 (1):", second_flash_time, "秒後")
print("基本3 (2):", simultaneous_flash_count, "回")
print("基本4 (1):", first_match)
print("基本4 (2):", results4)
print("基本5:", not_multiple_count, "個")

