"""
filter 関数
filter 関数は、イテラブルなオブジェクトの要素のうち、指定された関数が True を返す要素だけを抽出して、新しいイテラブルを作成します。
"""


# 偶数の抽出サンプル
def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print("Number", numbers)
print('偶数の抽出結果', list(even_numbers))  # 出力: [2, 4]
