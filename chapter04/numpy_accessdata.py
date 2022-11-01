import numpy as np
# 创建多维数组
myarray = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
print(myarray)
print(myarray.shape)
# 访问数据
print(f'这是第一行：{myarray[0]}')
print(f'这是最后一行：{myarray[-1]}')
print(f'访问整列（3列）数据：{myarray[:, 2]}')
print(f'访问指定行（2行）和列（3列）的数据：{myarray[1, 2]}')