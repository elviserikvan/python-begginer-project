
DATABASE_FILE = 'database.txt'


def add_account_to_database(email, password):
    with open(DATABASE_FILE, 'a+') as file:
        file.write(f'{email}:{password}')
        file.write(f'\n')


def read_credentials_from_database(credentials):
    with open(DATABASE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
           
            db_creds = line.split(':') # Separate email and password into a list
            db_creds[1] = db_creds[1].replace("\n", '') # Set the password value of the list to the same value but without the break line

            user_creds = credentials.split(':')

            if db_creds[0] == user_creds[0] and db_creds[1] == user_creds[1]:
                print('Login sucessfull')
                break;
        else:
            print("Could not find your credentials in the database")


def login():
    email = input('Email: ')
    password = input('Password: ')

    credentials = f'{email}:{password}'

    read_credentials_from_database(credentials)

def register():
    email = input('Please enter your email: ')
    password = input('Enter password: ')
    password2 = input('Repeat password: ')

    if password == password2:
        add_account_to_database(email, password)
        print('Register successfull')
    else:
        print("Passwords do not match, please try again")

