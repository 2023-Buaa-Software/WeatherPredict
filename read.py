## 数据读入示例代码

import numpy as np

# 训练集 - 自己划分训练集和验证集，并切分历史序列和预测序列训练模型
data_value_train = np.load("train/data_value_train.npy") # 气象数据文件，[12280, 3850, 2]，其中12280是时间序列长度，3850是气象站数量，2是两个气象变量包括风速和温度。
data_time_train = np.load("train/data_time_train.npy") # 时间文件，[12280]，气象数据文件中每个时间步的具体时间，从“2019-01-01 00:00:00”到“2020-05-26 15:00:00”，间隔一个小时。
stations_sorted = np.load("train/stations_sorted.npy") # 站点地理坐标文件，[3850, 3]，按顺序排列的3850个气象站维度、经度及海拔高度。

print(10, data_value_train)
print(11, data_time_train)
print(12, stations_sorted)

# 测试集 - 共包括73条测试数据，只给出3850个站点的48小时历史数据，需要预测未来24小时数据
# data_value_test_x = np.load("test/data_value_test_x.npy") # 气象数据文件，[73, 48, 3850, 2]，73条测试数据，48小时历史数据，3850个气象站，2个气象变量（风速和温度）。
# data_time_test_x = np.load("test/data_time_test_x.npy") # 时间文件，[73, 48]，73条测试数据中，48小时历史序列中每个时间步的具体时间。
# data_time_test_y = np.load("test/data_time_test_y.npy") # 时间文件，[73, 24]，73条测试数据中，需要预测的24小时具体时间。
# stations_sorted = np.load("test/stations_sorted.npy") # 站点地理坐标文件，[3850, 3]，按顺序排列的3850个气象站维度、经度及海拔高度。

# 保存
# data_value_test_y = np.zeros([73, 24, 3850, 2])
# np.save("data_value_test_y.npy", data_value_test_y)

# print("ok.")
