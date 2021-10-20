import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values,s=10,c=y_values,cmap=plt.cm.Blues)

# グラフのタイトルと軸ラベルを設定する
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# 目盛りラベルのサイズを設定する
ax.tick_params(axis="both", which="major", labelsize=14)

#各軸の範囲を設定する
ax.axis([0,5000,0,126_000_000_000])

#グラフの保存
#plt.savefig("test.png", bbox_inches="tight")

#描画
plt.show()

