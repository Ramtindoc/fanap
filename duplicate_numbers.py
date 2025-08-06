def find_duplicate(numbers):
    seen = set()
    duplicateNum = set()

    for num in numbers:
        if num in seen:
            duplicateNum.add(num)
        else:
            seen.add(num)
        
    return list(duplicateNum)
    
# اعداد رو از کاربر میگیرم
user_input = input("please inter integer numbers from comma-separated(,) :")
# اعداد را به فرم یک لیست از اعداد صحیح تکراری میگیریم
get_number_from_user = list(map(int,user_input.split(',') ))
print('duplicate int numbers:',find_duplicate(get_number_from_user))