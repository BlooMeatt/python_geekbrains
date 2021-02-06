item_template = {
    'Название': 'Введите название товара:\n>>>',
    'Цена': 'Цена:\n>>>',
    'Количество': 'Количество:\n>>>',
    'Ед.измерения': 'Ед. измерения:\n>>>',
}
item_dict = {}
item_warehouse = ()
warehouse = []
i = int(input("Введите количество товаров: "))
for i in range(i):
    item_dict = {}
    for key, value in item_template.items():
        item_dict[key] = input(value)
    item_warehouse = (i+1, item_dict)
    warehouse.append(item_warehouse)
print("Список товаров:\n", warehouse)
warehouse_summary = {}
warehouse_summary_value = []
for key in item_template.keys():
    for i in range(len(warehouse)):
        warehouse_summary_value.append(warehouse[i][1].get(key))
    warehouse_summary[key] = warehouse_summary_value
    warehouse_summary_value = []
print("Конечная матрица: ", warehouse_summary)
