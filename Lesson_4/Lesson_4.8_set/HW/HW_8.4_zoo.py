# HW_8.4_zoo

predators = set(['tigers', 'leons', 'wolfs', 'bears'])
birds = set(['parrots', 'owls', 'pelicans', 'eagles', 'penguins', 'flamingos'])
herbivores = set(['rabbits', 'elephants', 'giraffes', 'rhinos', 'roe deers'])

all_animals = predators | birds | herbivores
sorted_all_animals = sorted(all_animals)
print(f"All animals in the 'Zoo': {sorted_all_animals}"
      f"\t\nIn the 'Zoo' - {len(sorted_all_animals)} animals.")

mammals = predators | herbivores
count_mammals = len(mammals)
print(f"Количство млекопитающих в 'Zoo' - {count_mammals} animals.")

birds.remove('owls')
birds.remove('eagles')
print(birds)

birds.add('cranes')
birds.add('peacock')
print(birds)

mammals = predators | herbivores
count_mammals = len(mammals)
print(f"All animals in the 'Zoo': {sorted_all_animals}"
      f"\t\nIn the 'Zoo' - {len(sorted_all_animals)} animals.")