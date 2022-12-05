import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_, d=",", k="\n") -> list[dict]:
    with open(input_) as f:

        # блок чтения чтения из файла и удаления пустых элементов
        src = f.read().split(k)
        src_m = [src[i] for i in range(len(src)) if src[i]]

        # блок разделения информации на названия колонок и сами колонки
        headers = src_m[0].split(d)
        data = src_m[1:]
        data_m = []
        result = []

        # блок разделения строк на элементы
        for i in range(len(data)):
            data_m.append(data[i].split(d))

        # блок компоновки одного словаря и его добавление в список
        for i in range(len(data_m)):
            list_ = data_m[i]
            dict_ = {headers[j]: list_[j] for j in range(len(list_))}
            result.append(dict_)

    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
