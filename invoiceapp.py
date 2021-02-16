import re

# menu and price list
menu = {
    'rice': 50,
    'yam': 100,
    'garri': 200
}

n = int(input('enter number of items purchased: '))

user_name = input('Enter your name: ').capitalize()

# phone number verification
while True:
    try:
        user_phone = int(input('Please enter a valid phone-number: +234-'))
    except ValueError:
        print('invalid number')
        continue

    if len(str(user_phone)) == 10:
        break
    else:
        continue

# email address verification
user_email = ' '
while True:
    # a regular expression for validating an Email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    user_email = input('Enter a valid email address: ')

    try:
        if re.search(regex, user_email):
            break
    except ValueError:
        print("Invalid Email")

print('Please see below our menu and their prices: ')
print('-' * 50)
print(menu)

# user input calculations and print statements
item = {}
for i in range(n):

    x = input("enter item. \n")

    while x not in menu.keys():
        print('item not in stock, please enter an item in the menu list!')
        x = input("enter item(s) purchased. \n")

    y = int(input('enter quantity: \n'))
    item[x] = y
    i += 1



print('\nINVOICE')
print('Dear,',
      user_name + '\n' + '0' + str(
          user_phone) + '\n' + user_email + '\n' + 'Kindly find below your invoice: ')
print('\n')

print('Item' + ' ' * 10 + 'Qty' + ' ' * 10 + 'Total')
print('-' * 40)

total_value = {}

for key, value in item.items():
    print(key, ' ' * 10, value, ' ' * 10, value * menu.get(key))
    total_value[key] = value * menu.get(key)
print('-' * 40)
print('Total', ' ' * 22, sum(total_value.values()))
print('\nThank you for patronizing us!')