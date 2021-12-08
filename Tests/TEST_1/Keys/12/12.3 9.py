"""
Дан список гостей, посетивших вечеринку, причем гости в этом списке располагаются в порядке их прибытия:
Adela, Fleda, Owen, May, Mona, Gilbert, Ford (Adela приехала на вечеринку первая, а Ford - последний).
Гость, прибывший после того, как половина гостей уже была на вечеринке, считается в меру опоздавшим,
в то время как гость, прибывший последним, считается опоздавшим неприлично.
Определите, попадают ли в одну из этих категорий (и если да, то в какую) следующие гости:
May, Fleda, Gilbert и Ford.
"""

guests = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

ind_v_meru_op = int(len(guests)/2)
ind_op_nepr = len(guests) - 1

name = 'May'
ind_name = guests.index(name)

print('В меру опоздавший: ', ind_name >= ind_v_meru_op and ind_name != ind_op_nepr)
print('Опоздавший неприлично: ', ind_name == ind_op_nepr)
