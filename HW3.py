###Username and Password####

username = 'oguzhandogan'
password = 'password123'

user_name = input('Enter your username: ')
pass_word = input('Enter your password: ')

if username != user_name and password == pass_word:
    print('Invalid username!! Try again.')
elif username == user_name and password != pass_word:
    print('Invalid password!! Try again.')
elif username != user_name and password != pass_word:
    print('Invalid username and password!! Try again.')
else:
    print('You successfully logged in')

### With dictionary####

username_password = {'username' : 'oguzhandogan', 'password' : 'password123'}

user_name = input('Enter your username: ')
pass_word = input('Enter your password: ')

if  user_name != username_password['username'] and pass_word == username_password['password']:
    print('Invalid username!! Try again.')
elif user_name == username_password['username']  and  pass_word != username_password['password']:
    print('Invalid password!! Try again.')
elif user_name != username_password['username'] and pass_word != username_password['password'] :
    print('Invalid username and password!! Try again.')
else:
    print('You successfully logged in')

    