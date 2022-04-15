def even_or_odd(number):
    status = ""
    if number == 0:
        status = "Even"
    elif number % 2 == 0:
        status = "Even"
    else:
        status = "Odd"
    return print(f'even_or_odd({number}), "{status}"')


even_or_odd(2)
even_or_odd(1)
even_or_odd(0)
even_or_odd(152345346)
even_or_odd(10000)
even_or_odd(-123)
even_or_odd(-423)

return "Odd" if number % 2 else "Even"

even_or_odd = lambda number: "Odd" if number % 2 else "Even"

def even_or_odd(number):
    if number % 2:
        return "Odd"
    return "Even"

def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'

def even_or_odd(number):
  return 'Even' if number % 2 == 0 else 'Odd'


def even_or_odd(number):
    status = ""
    if number % 2 == 0:
        status = "Even"
    else:
        status = "Odd"

    return status

