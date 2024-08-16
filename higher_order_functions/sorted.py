"""
sorted 関数とカスタムキー
sorted 関数は、リストをソートする際にカスタムキーを指定することで、特定の条件に基づいてソートができます。
"""

# グレードでソートするサンプル
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

sorted_students = sorted(students, key=lambda student: student['grade'])
print('グレードでソートするサンプル')
print('student', students)
print('ソート結果', sorted_students)
# 出力: [{'name': 'Charlie', 'grade': 78}, {'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]
