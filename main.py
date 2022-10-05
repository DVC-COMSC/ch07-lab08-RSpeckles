# ******************************
# Make your Code
# ******************************
userInputs = input("Enter some numbers: ")
numbers = list(userInputs.split())

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

num = int(input("Enter another number: "))

for i in range(5):
    if numbers[i] > num:
        numbers.insert(i, num)
        flag = 1
        break

if flag == 0:
    numbers.append(num)

print(numbers)
