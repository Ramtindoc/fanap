# اگر بخواهیم به صورت دستی به تابع ورودی بدیم :
def reversed_text(text): return text[::-1]
result = reversed_text("text")
# print(result)

# اگر بخوایم ورودی از کاربر داشته باشیم :
# حتی اگر از نوع عدد هم باشه به رشته تبدیل میشه و ریورس میشه
user_input = str(input("Enter a string to reverse it:"))
result = reversed_text(user_input)

# print("result: ",result)
