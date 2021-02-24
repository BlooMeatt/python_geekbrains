# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('task2.txt', 'r') as file:
    line_sum = 0
    for line in file:
        line_sum += 1
        word_sum = len(line.split())
        print('Количество слов в строке {} - {}'.format(line_sum, word_sum))

print('Количество строк в файле: ', line_sum)
