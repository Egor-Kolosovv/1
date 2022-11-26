import random

password_lenght=11

characters = 'abcdefghijklmnopqrstuvwxyz'

password = ''

for index in range(password_lenght):
    password = password + random.choice(characters)

print('Password generated: {}'.format(password))

