"""
reduce 関数
reduce 関数は、イテラブルなオブジェクトの要素を順番に指定された関数に適用し、要素を1つにまとめます。
Pythonでは、functools モジュールからインポートして使用します。
"""

from functools import reduce


# 2つの数を足し合わせる関数を定義する
def add(x, y):
    return x + y


# listの内容を合計するサンプル
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print('合計サンプル')
print('numbers', numbers)
print('足し算の結果', sum_of_numbers)  # 出力: 15
