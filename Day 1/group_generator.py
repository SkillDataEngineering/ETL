# Inspired by the Python module exercise.
# Can use student submission instead if available.

import random

GROUP_SIZE = 2

students = [

]

# students = ['Adam Andersson', 'Birgitta Bolund', 'Charlotte Ceres',
#             'David Demi', 'Elin Eliasson', 'Fredrik Filament',
#             'Gustav Gonewrong', 'Helena den Helige', 'Ivar Ivrig']

random.shuffle(students)

groups = []

# Slice up into groups
for i in range(0, len(students), GROUP_SIZE):
    groups.append(students[i:min(i+GROUP_SIZE, len(students))])

# Print
for number, grouping in enumerate(groups, 1):
    group_string = "\n - " + "\n - ".join(grouping)
    print(f"Group {number}: {group_string}")
