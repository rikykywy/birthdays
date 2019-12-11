import csv

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

with open('databirth2.csv', 'w') as f:
    for key in birthdays:
        csv_columns= []
        x = key
        csv_columns.append(x)
        y = birthdays[key]
        csv_columns.append(y)
        w = csv.DictWriter(f, fieldnames= csv_columns)
        w.writeheader()
#All set!
