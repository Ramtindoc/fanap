def is_prime(n):
    if n < 2:   # اعداد اول بزرگتر از یک اند
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_prime_number(numbers):
    return[num for num in numbers if is_prime(num)]

try:
    user_input = input("please inter a prime number: ")
    get_number_list = list(map(int, [x.strip() for x in user_input.split(',')]))

    prime_number = get_prime_number(get_number_list)
    if prime_number:
        print("prime number is :",prime_number)
    else:
        print("incorrect prime number or don't used ',' , please inter a correct model ")
except ValueError:
    print("please inter correct prime number")