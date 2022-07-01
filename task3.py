import os

dir = os.listdir()

def merge_txt_files(list):
    txt_list = []
    for file in dir:
        if file.endswith('.txt') and file != 'merged_txt_files.txt':
            with open(file, encoding='utf-8') as f:
                a = sum(1 for line in f)
            with open(file, encoding='utf-8') as f:
                text = f.readlines()
                text = [line.strip() for line in text]
                text = "\n".join(text)
                txt_item = [file, a, text]
                txt_item = "\n".join(map(str, txt_item)) # понимаю, что из-за этого действия раньше времени убираю словарь
                txt_list.append(txt_item)
                for i in txt_list:
                    sorted_txt_list = sorted(txt_list, key= lambda x: x[1])
                    # и поэтому здесь не происходит сортировка, т.к. словаря уже нет
                    # но у меня никак не получилось привести форматирование к необходимому,
                    # если убрать 16 строку
                    sorted_txt_list = "\n".join(map(str, sorted_txt_list))
                    with open('merged_txt_files.txt', 'w', encoding='utf-8') as merged_file:
                        merged_file.write(sorted_txt_list)
    return sorted_txt_list

print(merge_txt_files(dir))


