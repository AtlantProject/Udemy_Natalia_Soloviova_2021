"""
Дан список цветов: 'red', 'green', 'white', 'black', 'pink', 'yellow'.
Создайте еще один список и переместите в него 1-ый, 5-ый и 6-ой элементы.
"""

colors = ['red', 'green', 'white', 'black', 'pink', 'yellow']
new_colors = [colors.pop(0), colors.pop(4-1), colors.pop(5-2)]

print(colors, new_colors)
