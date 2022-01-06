import random



digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def generate_password(length, chars):
    newPWSRD = ''
    for i in range(length):
        newPWSRD += random.choice(chars)
    return newPWSRD


totalPSWRD = input('Укажите количество паролей для генерации:')
lenPSWRD = input('Укажите длину одного пароля:')
digPSWRD = input('Включать ли цифры 0123456789? (y/n)')
ABCpswrd = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcPSWRD = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chPSWRD = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excPSWRD = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

if digPSWRD.lower() == 'y':
    chars += digits
if ABCpswrd.lower() == 'y':
    chars += lowercase_letters
if abcPSWRD.lower() == 'y':
    chars += uppercase_letters
if chPSWRD.lower() == 'y':
    chars += punctuation
if excPSWRD.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
print(chars)
for _ in range(int(totalPSWRD)):
    print(generate_password(int(lenPSWRD), chars))

