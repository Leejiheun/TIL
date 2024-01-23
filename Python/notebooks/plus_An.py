blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'A', 'B', 'O', 'A', 'B', 'AB']


# case 1
def count_blood(blood_types):
    blood_dict = {}
    for blood in blood_types:
        if blood_dict.get(blood):
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1
    return blood_dict


print(count_blood(blood_types))


# case 2
def count_blood(blood_types):
    blood_dict = {}

    for blood in blood_types:
        blood_dict[blood] = blood_dict.get(blood, 0) + 1

    return blood_dict


print(count_blood(blood_types))