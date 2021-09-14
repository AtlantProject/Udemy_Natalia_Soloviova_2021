names = ['Rose', 'Nina', 'Phillip', 'Alex', 'Jimmy', 'Max']


for name in names:
    if 'x' in name:
        break
    if len(name) <= 4:
        print(f"Hello {name}!")
