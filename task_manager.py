##=====importing libraries===========
import os
from datetime import date

##======= Classes =======


##======= Functions =======

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


##===== Functions END =====

# Clear screen on program launch
clear()

# ===== Login ===== #

# Set logged in state to false
loggedIn = False

# Create empty users list
users = []

# Get users from file and append to users list
with open('user.txt', 'r', encoding='utf-8') as f:
    for line in f:
        credentials = line.strip().replace(' ', '').split(',')
        users.append(credentials)

# Get user input username and password
username = input("Username: ")
password = input("Password: ")

# Check username is correct

# Create list of accepted users
usernames_accepted = []
for user in users:
    usernames_accepted.append(user[0])

while username not in usernames_accepted:

    # Alert user they entered incorrect username
    print(f"Username {username} is not recognised. Please try again!")

    # Ask for username and password again
    username = input("Username: ")
    password = input("Password: ")

else:

    # Check password
    while password != users[usernames_accepted.index(username)][1]:

        # Alert user they entered incorrect password
        print("Password entered is incorrect. Please try again!")

        # Ask for username and password again
        password = input("Password: ")

    else:

        # User logged in successfully
        # Clear Screen
        clear()

        # Print Success message
        print("Login Success!")

        # Set loggin in state to true
        loggedIn = True

        # Set global variable to contain users username
        global usr
        usr = username

# ===== Login End ===== #

while loggedIn:

    # If admin display admin menu
    if username == "admin":
        menu = input('''Select one of the following Options below:
r\t - \tRegistering a user
a\t - \tAdding a task
va\t - \tView all tasks
vm\t - \tView my task
s\t - \tDisplay Statistics
e\t - \tExit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r\t - \tRegistering a user
a\t - \tAdding a task
va\t - \tView all tasks
vm\t - \tView my task
e\t - \tExit
: ''').lower()
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.

    if menu == 'r':

        clear()

        # If user is not admin redirect back to home page
        if usr != 'admin':

            # Print error to user
            print("You must be admin to register new users.")

        else:

            # Get username and password input from user
            username = input("New Username: ")
            password = input("New Password: ")
            confirm_password = input("New Password: ")

            # Check password match
            if password == confirm_password:

                # Write user to file
                with open('user.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{username}, {password}\n")

                clear()

                print("User registered successfully!")

            else:

                clear()

                # Print error
                print("The passwords you entered do not match. Please try again!")

    elif menu == 'a':

        clear()

        # Get user inputs and format into single line string
        new_task = f"{input('Which user will complete task: ')}, " \
                   f"{input('Enter Task Title: ')}, " \
                   f"{input('Task Description: ').replace(',', ' ')}, " \
                   f"{date.today().strftime('%d/%m/%Y')}, " \
                   f"{input('Due Date (dd/mm/yyyy): ')}, " \
                   f"No\n"

        # Write to file
        with open('tasks.txt', 'a', encoding='utf-8') as f:
            f.write(new_task)

        clear()

        # Print success message
        print("Task Created!")

    elif menu == 'va':

        clear()

        # Screen Title
        print("All Tasks\n")

        # Open the tasks.txt file
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                # Split task into list
                task = line.split(',')

                # Print out formatted info
                print(f"Assigned to: {task[0]}\n"
                      f"Title:{task[1]}\n"
                      f"Description: {task[2]}\n"
                      f"Assigned: {task[3]}\tDue: {task[4]}\n"
                      f"Completed: {task[5]}")

        # Once all tasks have been printed give option to exit to main menu
        close = input("Press enter to exit to main menu...")
        clear()

    elif menu == 'vm':

        clear()

        # Screen Title
        print("My Tasks\n")

        # Open the tasks.txt file
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            for line in f:
                # Split task into list
                task = line.split(',')

                # Check if task is for user logged in
                if username == task[0]:

                    # Print out formatted info
                    print(f"Assigned to: {task[0]}\n"
                          f"Title:{task[1]}\n"
                          f"Description: {task[2]}\n"
                          f"Assigned: {task[3]}\tDue: {task[4]}\n"
                          f"Completed: {task[5]}")

        # Once all tasks have been printed give option to exit to main menu
        close = input("Press enter to exit to main menu...")
        clear()

    elif menu == 's':

        clear()

        # Check user has permissions to access statistics
        if username == 'admin':

            # Set default values to 0
            total_tasks = 0
            total_users = 0

            # Get total number of tasks
            with open('tasks.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    total_tasks += 1

            # Get total number of users
            with open('user.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    total_users += 1

            print(f"Statistics\n\n"
                  f"Total Users: {total_users}\n"
                  f"Total Tasks: {total_tasks}\n")

            # Give option to close to main menu
            close = input("Press enter to exit to main menu...")
            clear()

        else:

            # Return insufficient permissions error
            print("You do not have permission to access this feature.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
