with open ('task6.txt',encoding='utf-8') as file:
    lines = file.readlines()
    result = dict()
    for line in lines:
        l = line.split()
        s = l[0]
        summ = sum([int(x[:x.find('(')]) for x in l[1:] if '(' in x])
        result[s[:-1]] = summ
print(result)