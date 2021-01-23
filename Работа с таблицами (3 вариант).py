import pandas as pd

persons = pd.read_csv(r"C:\Users\Олег\Desktop\persons.csv")
items = pd.read_csv(r"C:\Users\Олег\Desktop\items.csv")


def prepare_dict(csv_text):
    dict = {}
    count = 0
    for i in str(csv_text.keys()[0]).split(';'):
        lst = []
        for value in csv_text.values:
            item = str(value)[2:-2:].split(';')[count]
            if i == 'id':
                while item.startswith('0'):
                    item = item[1:]
            lst.append(item)
        dict[i] = lst
        count += 1
    return dict


writer_persons = pd.ExcelWriter('persons.xlsx')
writer_items = pd.ExcelWriter('items.xlsx')
sheet_persons = pd.DataFrame(prepare_dict(persons))
sheet_items = pd.DataFrame(prepare_dict(items))
persons_and_items = {'persons': sheet_persons, 'items': sheet_items}
writer = pd.ExcelWriter('persons_and_items.xlsx', engine='xlsxwriter')
for sheet_name in persons_and_items.keys():
    persons_and_items[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
writer.save()
