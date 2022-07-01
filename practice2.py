from pprint import pprint

file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
# fl = [file_name_1, file_name_2, file_name_3]

def files_reader(file_name_1, file_name_2, file_name_3):
    fl = [file_name_1, file_name_2, file_name_3]
    g_dick = {}
    file_dict = {}
    for i in fl:
        with open(i) as file:
            text = file.readlines()
            file_dict = {i: [len(text), text]}
            # pprint(file_dict)
            g_dick.update(file_dict)
            # print(big_dick)
    sorted_tuple = sorted(g_dick.items(), key=lambda x: x[1])
    # pprint(sorted_tuple)

    # with open('all_files.txt', 'w') as f:
    #     for file in sorted_tuple:
    #         f.writelines(file)

files_reader(file_name_1, file_name_2, file_name_3)