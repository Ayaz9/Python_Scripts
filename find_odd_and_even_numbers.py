
'''This scripts helps to find how many odd (1,3..) and even (2,4..) numbers in user input range  
and which they are. Start putting your range'''

min_num = input("from : ")
max_num = input("to : ")


def find_even_odd_numbers(min_dig, max_dig):
    list_of_even = []
    list_of_odd = []
    for a in range(min_dig, max_dig + 1):
        if a % 2 == 0:
            list_of_even.append(a)
        elif a % 2 != 0:
            list_of_odd.append(a)
    print(f'There are {str(len(list_of_even))} even numbers in between {str(min_dig)} and {str(max_dig)}, and they are : {str(list_of_even)}')
    print(f'There are {str(len(list_of_odd))} odd numbers in between {str(min_dig)} and {str(max_dig)}, and they are : {str(list_of_odd)}')


if min_num.isdigit() and max_num.isdigit():
    min_num, max_num = int(min_num), int(max_num)
    if min_num < max_num:
        find_even_odd_numbers(min_num, max_num)
    elif min_num > max_num:
        find_even_odd_numbers(max_num, min_num)
    elif min_num == max_num:
        print('Wrong input! The entered numbers are the same.')
else:
    print('Wrong input, we expected the digits!')

