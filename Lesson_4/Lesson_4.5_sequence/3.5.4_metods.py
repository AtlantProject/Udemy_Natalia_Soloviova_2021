'''
l = [1, 2, 3, 4, 5, 5, 5, 6, 7]
print(l)
a = l.pop(0)
print(l)
print(a)
b = l.pop()
print(b)

print(l.index(5))
print(l.count(5))
print(l)
c = l.sort(reverse=True)
print(c)

l_2 = [1, 2, 3, 4, 5]
rev = l_2.sort(reverse=True)
print(l_2)
rev_2 = l_2.reverse()
print(rev_2)
'''
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
a = fruits.pop()
print(a)