def replace_0_with_5(num):
    return int(str(num).replace('0','5'))
num = int(input("Enter the number you want to check: "))
print("The number after replacing all 0 with 5 will be", replace_0_with_5(num))

