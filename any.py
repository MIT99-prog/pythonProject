"""
any 関数
any 関数は、イテラブル内のいずれかの要素が True であれば True を返します。
"""


# 例: any 関数の使用
numbers = [0, 1, 2, 3]  # False, True, True, True
print('number', numbers)
print('T/F : False, True, True, True')
print('結果', any(numbers))  # 出力: True
