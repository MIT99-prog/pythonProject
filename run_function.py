"""
関数を引数として受け取る高階関数
"""


def run_function(func):
    func()


def greet():
    print("こんにちは！")


run_function(greet)  # 出力: こんにちは！
