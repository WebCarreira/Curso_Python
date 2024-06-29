username = str(input('What is your username? '))
password = str(input('Password: '))

password_check = len(password)

print(f'{username}, your password {'*' * password_check} is {password_check} letters long.')