
'''
#1 - Verify if the range input is digit
#2 - Create empty dictionary, iterate every digit from input range and set them as keys, 
     multiply the keys as per the request and set them as values respectively
#3 - Return set of keys
#4 - Return set of values
#5 - Return entire dictionary
'''

def verify_digit(note):
    usr_input = input(f'{note}: \n')
    if usr_input.isdigit():
        return int(usr_input)

def multipled_value(range_value, mutiply_by):
    if range_value == 1: return 1
    else: 
        a = 1
        for i in range(mutiply_by): 
            # print(i)
            a = a * range_value
        return  a

verify = verify_digit('Enter range')
if verify:
    new_dict = {}
    multiply = verify_digit('Multiply of each digit by')
    if multiply:
        # Create dictionary
        for i in range(1, verify + 1):
            new_dict[i] = multipled_value(i,multiply)
        print(f'Dictionary keys: \n{new_dict.keys()} \n')
        print(f'Dictionary values: \n{new_dict.values()} \n')
        print(f'The range is from 0 to {verify}, and each of the values in the range multiplied by {multiply}. \
            \nFull dictionary is: \n{new_dict}')
    else: 
        print('Expected digit!')
else:
    print('Expected digit!')

