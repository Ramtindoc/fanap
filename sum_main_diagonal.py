# logic
def sum_main_diagonal(matrix):
    total = 0   # مقداردهی اولیه
    for i in range(len(matrix)):
        total += matrix[i][i] # عناصر قطراصلی ماتریکس مربعی
    return total
# --------------------------------------------------------------
# #1.sample matrix  like 3*3
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print("main diagonal total is :", sum_main_diagonal(matrix))  
# ----------------------------------------------------------------------
# 2. user input
user_input_lenght = int(input("inter square lenght :?"))
matrix = []
print(f"inter matrix number lenght is ({user_input_lenght}) and used space between every numbers.")
for i in range(user_input_lenght):
    row = list(map(int, input(f"line {i+1}: ").split()))
    if len(row) != user_input_lenght:
        print()
        exit()
    matrix.append(row)
total_main_diagonal = sum_main_diagonal(matrix)
print("total main diagonal result :",total_main_diagonal)


