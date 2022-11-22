import random

fileptr = open('data.txt', 'w')

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

amount = int(input('Количество поролей '))
lenght = int(input('Длина пороля '))
digits_yes_or_no = input('Наличие цифр (да/нет) ')
lowers_letters_yes_or_no = input('Наличие прописных/заглавных букв (да/нет) ')
upper_letters_yes_or_no = input('Наличие строчных/маленьких букв (да/нет) ')
symbols_yes_or_no = input('Наличие символов ')
same_symbiols = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет) ')

if digits_yes_or_no == 'да':
    chars += digits
if lowers_letters_yes_or_no == 'да':
    chars += lowercase_letters
if upper_letters_yes_or_no == 'да':
    chars += uppercase_letters
if symbols_yes_or_no == 'да':
    chars += punctuation
if same_symbiols == 'да':
    for s in chars:
        if s == 'il1Lo0O':
            chars = chars.replace(s, '')


def generate_password(lei, cha):
    password = ''
    for j in range(lei):
        password += random.choice(cha)
    return password


for _ in range(amount):
    fileptr.write(generate_password(lenght, chars))

fileptr.close()
