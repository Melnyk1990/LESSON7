import random
print('\t'*3, '*'*10, 'TASK 1', '*'*10, 3*'\t')
def get_list_multiplication(numbers):
    numbers_multiplication = 1
    for num in numbers:
        numbers_multiplication *= num
    return numbers_multiplication


my_numbers = [n for n in range(1, 8)]
print(f'A list of numbers has been created: {my_numbers}')
print(f'The product of the list elements is returned: {get_list_multiplication(my_numbers)}')