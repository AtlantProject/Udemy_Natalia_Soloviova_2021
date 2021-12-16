def cat(weight=0, state='hungri',
        action='eat', kind='Persian'):
    return print(weight, state, action, kind)

cat('110', 'very fat', 'burst')
cat(555)
cat(1, state='state')
cat(1, name='state')    # error