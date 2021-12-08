"""
Написать программу, в которой с помощью функции sorted() и lambda-функции отсортировать слова в списке по их 2-ой букве.
"""
l = ['here', 'will', 'be', 'some', 'lambda', 'sorting', 'function']

print(l)

res = sorted(l, key=lambda i: i[1])
print(res)
