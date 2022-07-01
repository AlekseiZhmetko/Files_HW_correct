import os

dir = os.listdir()
txt_list = []

def count_lines(file):
   with open(file, encoding='utf-8') as f:
      res = len([1 for line in f])
      return res

def choose_txt(list):
   for file in list:
      if file.endswith('.txt'):
         with open(file, encoding='utf-8') as f:
            txt_list.append(file)
   return txt_list

def sort_by_str_qty(list):
   for file in list:
      list.sort(key= count_lines(file))

choose_txt(dir)
sorted_txt_list = sorted(txt_list, key= lambda x: x[1])
print(sorted_txt_list)

def dir_reading_txt(list):
   for i in list:
      with open(i, encoding='utf-8') as f:
         count = sum(1 for line in f)
         list.sort(key = count)


# def get_filename(file):
#    return os.path.basename(file)
#
# def reading(file):
#    with open(file, encoding='utf-8') as f:
#       return f.read()
#
# def what_to_write(file):
#    a = get_filename(file)
#    b = str(count_lines(file))
#    c = reading(file)
#    return print(a, b, c, sep='\n')
#
# def what_to_write(file):
#    a = get_filename(file)
#    b = str(count_lines(file))
#    c = reading(file)
#    return [a, b, c]
#
# print(what_to_write('data.txt'))
#
# file_list = [file1, file2, file3]
#
# def sorting_by_line_qty(list):
#    for i in list:
#       sorted(list, key=count_lines(i))
#       return list
#
# sorting_by_line_qty(file_list)
# print(file_list)
#
#
#
