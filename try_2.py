#4-8

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#2個のD6サイコロを作成する
die_1 = Die()
die_2 = Die()

#サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(50_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

#結果を分析する
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#結果を可視化する
x_values = list(range(1,max_result+1))
#print(x_values)
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title":"結果", "dtick":1}
y_axis_config = {"title":"発生した回数"}
my_layout = Layout(title="2個の6面サイコロを50000回転がして掛け算した結果",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename="d6_x_d6.html")
