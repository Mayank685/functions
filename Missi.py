def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
    dict.values()
print(char_frequency("Mppissiissi"))
def print_dict_in_reverse_order(d):
    _list = d.values()
    _list.sort()
    _list.reverse()
    for s in _list:
        print(d)

                                                                                                                                                                                                                                                                                                                                 
