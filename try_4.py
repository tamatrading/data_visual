#4-10 matlibによる正規分布

import matplotlib.pyplot as plt

from die import Die

#2個のD6サイコロを作成する
die_1 = Die()
die_2 = Die()

#サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#結果を分析する
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#結果を可視化する
x_values = list(range(2,max_result+1))
print(x_values)

plt.style.use("classic")
#fig, ax = plt.subplots()

plt.plot(x_values, frequencies)

#描画
plt.show()