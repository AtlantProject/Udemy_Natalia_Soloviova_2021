"""
решение предыдущей задачи с использованием нелокальной переменной
"""

points = 0

def game(card, max_sum=21):
    cur_points = 0

    def get_cur_points():
        nonlocal cur_points
        points = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'V': 2, 'D': 3, 'K':4, 'T': 11}
        if card in points.keys():
            cur_points = points[card]

    get_cur_points()
    global points
    points += cur_points

    if points < max_sum:
        print('Try another card..')
    elif points > max_sum:
        print('You lose!')
    else:
        print('You win!')


game('T')
game('10')
game('D')