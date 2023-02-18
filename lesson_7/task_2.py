# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

from math import pi


def find_farthest_orbit(nums_list):
    s_dict = {pi * val[0] * val[1]: val for i,
              val in enumerate(nums_list) if val[0] != val[1]}
    return max(s_dict.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))

# --------------------------------------------------------------


def find_farthest_orbit(nums_list):
    return max([(a[0] * a[1], a) for a in nums_list if a[0] != a[1]])[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))

# for  i  in orbits:
#     if i[0] != i[1]:
#         max_orbits = max([i[0] * i[1], i])[1]
#         print(max_orbits)
# print(max_orbits)
