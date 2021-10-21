import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #ランダムウォークを作成する
    rw = RandomWalk()
    rw.fill_walk()

    #ランダムウォークの点を描画する
    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    keep_running = input("別のランダムウォークを生成する？(y/n):")
    if keep_running == "n":
        break
