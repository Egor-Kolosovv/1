import random

password_lenght=11

characters = 'abcdefghijklmnopqrstuvwxyz'
characters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '1234567890'
password = ''

for index in range(password_lenght):
    password = password + random.choice(characters)

print('Password generated: {}'.format(password))

