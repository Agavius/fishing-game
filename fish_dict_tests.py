import random, json, time
from dict_data import fish_dict

fish_dict_weight = []
for i in range(len(fish_dict)):
    fish_dict_weight.append(list(fish_dict.values())[i][0])
print(fish_dict_weight)

fish_dict_xp = []
for i in range(len(fish_dict)):
    fish_dict_xp.append(list(fish_dict.values())[i][0])
print(fish_dict_xp)

fish_dict_worth = []
for i in range(len(fish_dict)):
    fish_dict_worth.append(list(fish_dict.values())[i][0])
print(fish_dict_worth)