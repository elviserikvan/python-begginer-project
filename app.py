from utils import login, register

def show_help():
    print('login -> prompt login screen')
    print('register -> prompt register screen')
    print('help -> show this help message')
    print('quit -> quit\n')

while True:
    user_input = input('> ').lower()

    if user_input == 'login':
       login() 


    elif user_input == 'register':
        register()

    elif user_input == 'help':
       show_help()

    elif user_input == 'quit':
        break;
