"""
zip 関数
zip 関数は、複数のイテラブルを並行して処理し、タプルのリストを作成します。
"""

# 例: zip 関数の使用
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print('list1', list1)
print('list2', list2)
print('zipの結果', list(zipped))  # 出力: [(1, 'a'), (2, 'b'), (3, 'c')]
