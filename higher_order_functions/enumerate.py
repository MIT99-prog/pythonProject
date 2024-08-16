"""
enumerate 関数
enumerate 関数は、イテラブルを処理する際にインデックスと要素を同時に取得できます。
"""

# 例: enumerate 関数の使用
fruits = ['apple', 'banana', 'cherry']
print('fruits', fruits)
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 出力:
# 0 apple
# 1 banana
# 2 cherry
