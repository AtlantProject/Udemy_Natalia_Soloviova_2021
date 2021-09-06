first_2_years = 10.5
other_years = 4

dog_age = int(input("Введите возраст собаки: "))

if dog_age <= 2:
    human_dog_age = dog_age * first_2_years
    print(f"'Человеческий' возраст собаки - {human_dog_age} лет.")
else:
    human_dog_age = dog_age * other_years
    print(f"'Человеческий' возраст собаки - {human_dog_age} лет.")
