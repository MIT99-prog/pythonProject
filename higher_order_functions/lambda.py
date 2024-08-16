"""
<lambdaのサンプルコード>
Pythonのlambda（ラムダ）式は、名前を付けずに小さな無名関数を作成するための方法です。これにより、コードを簡潔に記述することができます。
<基本構文>
lambda式の基本的な構文は以下の通りです：
lambda 引数: 式
<利点>
簡潔さ：短い関数を一行で記述できるため、コードが読みやすくなります。
高階関数との組み合わせ：mapやfilterなどの高階関数と組み合わせて使うことで、より強力な表現が可能です12.
<注意点>
複雑な処理には向いていないため、複数行にわたる処理が必要な場合は通常のdefを使う方が良いです。
"""

# 加減乗除サンプル
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

print('加減乗除サンプル')
print('3+5=', add(3, 5))  # Output: 8
print('3-5=', subtract(3, 5))  # Output: -2
print('3*5=', multiply(3, 5))  # Output: 15
print('3/5=', divide(3, 5))  # Output: 0.6

# Anonymous functions can be used in various places in Python,
# such as list comprehensions, dictionary comprehensions, and function arguments.

# ソートサンプル
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print('ソートサンプル')
print('students : ', students)
print('sorted by test score : ', sorted_students)  # 出力: [('Charlie', 92), ('Alice', 90), ('Bob', 85)]

# Anonymous functions can also be used as default arguments in functions.

# 二乗サンプル
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print('二乗サンプル')
print('Number = ', numbers)
print('squares = ', squares)  # 出力: [1, 4, 9, 16, 25]

# Anonymous functions can also be used as decorators in Python.

# 複数の引数を持つラムダ式サンプル（リストの長さが異なる場合、短い方に合わせられる）
numbers1 = [1, 2, 3, 4, 5, 6]
numbers2 = [6, 7, 8, 9, 10]
merged = list(map(lambda x, y: x + y, numbers1, numbers2))
print('複数の引数を持つラムダ式サンプル')
print('numbers1 = ', numbers1)
print('numbers2 = ', numbers2)
print('merged = ', merged)  # 出力: [7, 9, 11, 13, 15]

# 条件付きサンプル
is_even = lambda x: True if x % 2 == 0 else False
print('条件付きサンプル')
print('4 is even : ', is_even(4))  # 出力: True
print('5 is even : ', is_even(5))  # 出力: False
