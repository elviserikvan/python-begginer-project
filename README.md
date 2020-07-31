# Begginer Python Project

This is a simple python project to test my begginer knowledge. In this project I try to mimic a simple register/login app where the user is asked for an email and
a password, depending on what the user choose to do, the credentials will be either read or written to a database. Now, this app does not connect to any actual
database, where it will be actually storing the credentials is a simple `.txt` file located in the same directory along with the whole app. 

## Highlights

	- Modularity
	- For loops
	- Variables
	- String and file manipulation

## Usage

Execute the `app.py` file from the command line calling the python executable before it
```
$ python app.py
```

It's worth to mention this project was made with `Python 3.8` as the pre-compiler, but as it is a simple project there shouldn't be any compatibility problem.

Once the application starts a very simple prompt will apppear.
```
>
```

That prompt means you can enter a command now, enter the `help` command to see a list of all available commands and a short description of what they do.
``` 
> help
```


As you could see, four options will appear, one for `login`, one for `register`, one for showing all the commands and the last one to exit out of the application and terminate the python process.

If we enter the `register` command the app will ask for a email and a password.
```
> register
```

For this command to complete successfull the to passwords you enter sould be the same.
Once this command completes, it'll open the file where we are going to store all the credentials, in the case of this example, the file is `database.txt` and will store the credentials that the user just entered in a common seen formar
```
# databse.txt file

email1@gmail.com:password
email2@gmail.com:password
email3@gmail.com:password
...

```

Once this is done, the app will take us to the main manu where you can enter any of the command you saw earlier, this time, let's try to log in.
```
> login
```

The app will ask for an email and a password to look in the database file. if it finds a similar combination in that file it'll show us a `Login Successfull` message.
Otherwise, we'll see a `Could not find your credentials in the database` message

