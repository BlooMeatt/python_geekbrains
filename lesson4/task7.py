import json
with open('task7.txt', encoding='utf-8') as file:
    lines = file.readlines()
    result = dict()
    summ = 0
    i = 0
    for line in lines:
        s = (line.split())
        name = s[0]
        profit = int(s[2]) - int(s[3])
        if profit < 0:
            continue
        else:
            result[name] = profit
        summ = summ + profit
        i += 1
avg = summ / i
info = [result, {'avg_profit': avg}]
print(info)

with open('task7.json', 'w') as f_json:
    json.dump(info, f_json)
