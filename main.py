import matplotlib.pyplot as plt

categories = ['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015']
values1 = [19, 19, 19, 21, 23, 25, 25, 25, 25, 25]
values2 = [4.5, 5.5, 6.5, 10, 13.5, 17, 19, 21, 23, 25]
values3 = [27, 25.5, 24, 31, 38, 45, 40, 35, 30, 25]
values4 = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
plt.barh(categories, values1, label='\u6211\u4eec\u7684\u751f\u5b58\u6210\u672c')
plt.barh(categories, values2, label='\u6211\u4eec\u7684\u7ed3\u4f59', left=values1)
plt.barh(categories, values3, label='\u4ed6\u4eec\u7684\u7ed3\u4f59', left=[v1+v2 for v1, v2 in zip(values1, values2)])
plt.barh(categories, values4, label='\u4ed6\u4eec\u7684\u751f\u5b58\u6210\u672c', left=[v1+v2+v3 for v1, v2, v3 in zip(values1, values2, values3)])
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.title('\u8fd9\u5341\u5e74')
plt.legend(loc='lower right', bbox_to_anchor=(1, 0))
plt.show()
