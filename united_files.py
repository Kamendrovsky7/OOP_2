import os

# список файлов для чтения

files = ['1.txt', '2.txt', '3.txt']

# Список для хранения информации о файлах

files_inf = []

# Читаем каждый файл и собираем информацию

for file_ in files:
    with open(file_ , 'r', encoding='utf-8') as f:
        lines = f.readlines()  
        files_inf.append((file_, len(lines), lines))
    
# Сортировка по количеству строк

files_inf.sort(key=lambda x: x[1])

# Запись в объединеный фаил

with open('united.txt', 'w', encoding='utf-8') as united_file:

    for files, line_count, lines in files_inf:
        united_file.write(f"\n\n{files}\n{line_count}\n\n")  
        united_file.writelines(lines)  
