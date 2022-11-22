def dict_value_sort(dic):
    return dict(sorted(dic.items(), key=lambda item:item[1]))

def dict_key_sort(dic):
    return dict(sorted(dic.items(), key=lambda item:item[0]))