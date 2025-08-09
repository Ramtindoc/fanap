import csv

sales_data = [
    ['names', 'sales'],
    ['ali', 12000000],
    ['behzad', 95000000],
    ['hosein', 134000000],
    ['reza', 88000000],
    ['ramtin', 1000000]
]

with open('csv/sales.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

print("sales.csv created")