def get_count_char(str_):
    dict_ = dict()
    str_ = "".join(str_.split())
    str_ = str_.lower()
    list_ = list(set(str_))
    list_.sort()
    for i in list_:
        if i.isalpha():
            b = 0
            for k in range(len(str_)):
                if str_[k] == i:
                    b += 1
            dict_[i] = b
    return dict_


def to_percent(dict_):
    n = sum(dict_.values())
    for i in dict_:
        dict_[i] = round(dict_[i]/n*100, 3)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(to_percent(get_count_char(main_str)))
