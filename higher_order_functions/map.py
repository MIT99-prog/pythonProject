"""
map関数
"""
# 二倍サンプル
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print('二倍サンプル')
print('Number = ', numbers)
print('二倍した結果', list(doubled))  # 出力: [2, 4, 6, 8, 10]


# 二乗サンプル
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print('二乗サンプル')
print('Number = ', numbers)
print('二乗した結果', list(squared))  # 出力: [1, 4, 9, 16, 25]


# 複数の引数の足し算サンプル
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = map(lambda x, y: x + y, numbers1, numbers2)
print('複数の引数の足し算サンプル')
print('Number1 = ', numbers1)
print('Number2 = ', numbers2)
print('足し算の結果', list(summed))  # 出力: [5, 7, 9]
