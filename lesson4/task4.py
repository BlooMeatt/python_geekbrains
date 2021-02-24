with open('task4_in.txt', encoding='utf-8') as ifile:
    in_list = ifile.readlines()

with open('task4_out.txt', 'w', encoding='utf-8') as ofile:
    for line in in_list:
        if 'One' in line:
            line = line.replace('One', 'Один')
        elif 'Two' in line:
            line = line.replace('Two', 'Два')
        elif 'Three' in line:
            line = line.replace('Three', 'Три')
        elif 'Four' in line:
            line = line.replace('Four', 'Четыре')
        ofile.write(line)
