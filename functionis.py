def char_frequency(str1):
    dict = {}
    sorted_dict = {}
    str2 = str1 [::-1]
    for n in str2:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    sorted_keys = sorted(dict, key=dict.get, reverse = True)

    for w in sorted_keys:
        sorted_dict[w] = dict[w]

    return sorted_dict


print(char_frequency("Mississippi"))
