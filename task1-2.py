from pprint import pprint

file1 = 'data.txt'
cook_book = {}

def catalog_reader(file):
    with open(file, encoding='utf-8') as file_obj:

        for line in file_obj:
            line = line.strip()
            cook_book.update({line:[]})
            for item in range(int(file_obj.readline().strip())):
                list = file_obj.readline().strip().split(' | ')
                dict = {'ingredient_name': list[0], 'quantity': list[1], 'measure': list[2]}
                cook_book[line].append(dict)
            file_obj.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for k, v in cook_book.items():
        for dish in dishes:
            if dish in k:
                for i in v:
                    ing_name = i['ingredient_name']
                    measure = i['measure']
                    qty = int(i['quantity']) * int(person_count)
                    dict = {'measure': measure, 'quantity': qty}
                    shop_list.update({ing_name: dict})
                return shop_list


catalog_reader(file1)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 25))