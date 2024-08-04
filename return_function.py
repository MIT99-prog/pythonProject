"""
関数を返す高階関数
"""


def add_n(n):
    def adder(x):
        return x + n

    return adder


add_five = add_n(5)
print(add_five(10))  # 出力: 15
