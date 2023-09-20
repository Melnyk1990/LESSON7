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

print('\t'*3, '*'*10, 'TASK 2', '*'*10, 3*'\t')
def search_for_minimum(list):
    min_number = min(list)
    return min_number

list = []
for i in range(10):
    list.append(random.randint(-5, 6))
print(f'A list of numbers has been created: {list}')
print(f'Returned min from a list of numbers: {search_for_minimum(list)}')

print('\t'*3, '*'*10, 'TASK 3', '*'*10, 3*'\t')
def search_for_simple(list):
    list_simple = []
    for i in list:
        total = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total += 1
        if total == 2:
            list_simple.append(i)
    return list_simple

lis_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print(f'A list of numbers has been created: {lis_numbers}')
print(f'Returned a list of simple numbers: {search_for_simple(lis_numbers)}')

print('\t'*3, '*'*10, 'TASK 4', '*'*10, 3*'\t')
def numbers_del(list):
    list_del_nambers =[]
    for i in list:
        if i==0:
            continue
        elif i%2==0:
            list.pop()
            list_del_nambers.append(i)
    return list_del_nambers
list3 = []
for i in range(10):
    list3.append(random.randint(-5, 6))
print(f'A list of numbers has been created: {list3}')
print(f'Returned list of deleted numbers: {numbers_del(list3)}')