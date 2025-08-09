import csv 

sales = []

# readable
with open('sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)   # access easly 
    for row in reader:  
        sales.append(int(row['sales']))

# مجموع فروش
total_sales = sum(sales)
# میانگین فروش 
average_sales = total_sales / len(sales)
# بیشترین میزان فروش
max_sales = max(sales)

print(f" total sales: {total_sales}")
print(f" average sales : {average_sales:.2f}")
print(f"maxiam sales : {max_sales}")