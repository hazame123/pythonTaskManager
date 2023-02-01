# =============== START =============== #

##=====importing libraries===========
import os
import time
from datetime import date

##======= Functions =======

## Clear Screen ##
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

## User register ##
def reg_user():

    clear()

    # If user is not admin redirect back to home page
    if usr != 'admin':

        # Print error to user
        print("You must be admin to register new users.")

    else:

        # Get username and password input from user
        username = input("New Username: ")

        # Check if username has been used already
        with open('user.txt', 'r', encoding='utf-8') as f:
            for line in f:
                while username == line.split(',')[0]:
                    print(f"The username {username} already exists please choose a new one!")
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

## Add Task ##
def add_task():

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


## View All Tasks ##
def view_all():

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


## View Mine ##
def view_mine():

    clear()

    # Screen Title
    print("My Tasks\n")

    # List to store users tasks
    my_tasks = []
    all_tasks = []

    # Open the tasks.txt file
    with open('tasks.txt', 'r', encoding='utf-8') as f:
        for line in f:
            # Split task into list
            task = line.split(',')

            # Add task to all_tasks list
            all_tasks.append(task)

            # Check if task is for user logged in
            if username == task[0]:

                # Add to my_tasks list
                my_tasks.append(task)

    for i, task in enumerate(my_tasks):
        # Print out formatted info
        print(f"Task {i+1}\nAssigned to: {task[0]}\n"
              f"Title:{task[1]}\n"
              f"Description: {task[2]}\n"
              f"Assigned: {task[3]}\tDue: {task[4]}\n"
              f"Completed: {task[5]}")

    if not my_tasks:
        print("You're all up to date!\n")

    # Once all tasks have been printed give option to exit to main menu
    task_selection = int(input("Input -1 to return to main menu\nSelect a task (e.g. 2): "))

    if task_selection == -1:
        clear()
        pass
    else:

        clear()

        # Show task selected
        current_task = my_tasks[task_selection - 1]
        print(f"Assigned to: {current_task[0]}\n"
              f"Title:{current_task[1]}\n"
              f"Description: {current_task[2]}\n"
              f"Assigned: {current_task[3]}\tDue: {current_task[4]}\n"
              f"Completed: {current_task[5]}")

        option = int(input("[1] Mark Task as Complete\n"
                       "[2] Edit Task\n"
                           "[3] Back\n\n"
                       ": "))

        if option == 1:

            # Set task complete to yes
            my_tasks[task_selection - 1][5] = " Yes\n"

            # re write task data with updated task completion
            with open('tasks.txt', 'w', encoding='utf-8') as f:
                for task in all_tasks:
                    f.write(','.join(task))

            # Print success message
            print(f"Task marked as completed")
            time.sleep(2)

            # Back to users tasks
            view_mine()

        elif option == 2:

            if my_tasks[task_selection - 1][5] != " Yes\n":

                clear()

                # Reset user assign
                new_assign = input(f"Edit user to complete task (leave blank to keep current) [{my_tasks[task_selection - 1][0].replace(' ', '')}]: ")
                if new_assign == "":
                    pass
                else:
                    my_tasks[task_selection - 1][0] = new_assign

                # change due date
                new_due_date = input(f"Change due date (leave blank to keep current) [{my_tasks[task_selection - 1][4].replace(' ', '')}]: ")
                if new_due_date == "":
                    pass
                else:
                    my_tasks[task_selection - 1][4] = new_due_date

                # re write task data with updated info
                with open('tasks.txt', 'w', encoding='utf-8') as f:
                    for task in all_tasks:
                        f.write(','.join(task))

                print("Task Updating...")
                time.sleep(2)

                view_mine()

            else:

                # Print error message
                print("This task has already been marked as complete. You cannot edit it...")

                # Pause for 2 seconds
                time.sleep(2)

                # Back to task list
                view_mine()

        elif option == 3:

            # Run view my tasks function
            view_mine()

        else:

            # Output Error and get them to re enter valid option
            pass


## Generate task statistics
def task_stats():

    # Define variables that will hold stats

    total = 0
    total_comp = 0
    total_not_comp = 0
    total_overdue = 0


    with open('tasks.txt', 'r', encoding='utf-8') as taskfile:

        # For every line in taskfile add 1 to total
        for line in taskfile:

            # Total Tasks
            total += 1

            if line.split(',')[5].strip() == "Yes":

                # Total completed
                total_comp += 1

            else:

                # Total not completed
                total_not_comp += 1

            # Get due date and current date a split into list
            task_due = line.split(',')[4].strip().split('/')
            current_date = date.today().strftime('%d/%m/%Y').split('/')

            # Create date object with data from previous lists made
            first_date = date(int(task_due[2]), int(task_due[1]), int(task_due[0]))
            second_date = date(int(current_date[2]), int(current_date[1]), int(current_date[0]))

            # Subtract current date from due date
            delta_difference = first_date - second_date

            # And if number of days left to complete tast is less that 1
            if delta_difference.days < 1:

                # If not completed
                if line.split(',')[5].strip() != "Yes":
                    # Add one to total overdue tasks
                    total_overdue += 1

    # Calculate percentages

    percentage_not_comp = (total_not_comp / total) * 100
    percentage_overdue = (total_overdue / total) * 100

    file_output = f'''
=== Task Statistics ===

Total:\t\t\t {total}
Completed:\t\t {total_comp}
Not Completed:\t {total_not_comp}
Overdue:\t\t {total_overdue}

Percent Not Complete:\t {round(percentage_not_comp, 2)}%
Percent Overdue:\t\t {round(percentage_overdue, 2)}%

== Task Statistics END ==
'''

    with open('task_overview.txt', 'w', encoding='utf-8') as task_overview:
        task_overview.write(file_output)

    clear()
    print("Task Statistics Report Generated.")
    time.sleep(1)
    clear()


## Generate user statistics
def user_stats():

    # Define variables that will hold stats

    total_users = 0
    total_tasks = 0

    user_stat_list = []

    with open('user.txt', 'r', encoding='utf-8') as users:

        # For every user
        for user in users:

            # Add 1 to total_users
            total_users += 1

            # Create list to hold users stats
            user_statistics = {
                "username": str(),
                "total": 0,
                "percent": 0,
                "complete_percentage": 0,
                "not_complete_percentage": 0,
                "overdue_percentage": 0
            }

            # Create vars to hold data we need to calculate percentages
            all_tasks = 0
            users_tasks = 0
            tasks_complete = 0
            tasks_not_complete = 0
            tasks_overdue = 0

            with open('tasks.txt', 'r', encoding='utf-8') as tasks:

                # For each task
                for task in tasks:

                    # Count number of all tasks
                    all_tasks += 1

                    # If the user assigned to task is same as the current user being iterated
                    if task.split(',')[0].strip() == user.split(',')[0]:

                        # Add one to users tasks
                        users_tasks += 1

                        # If task is complete
                        if task.split(',')[5].strip() == "Yes":

                            # Add one to tasks complete
                            tasks_complete += 1

                        else:

                            # If task not complete add too tasks not complete
                            tasks_not_complete += 1

                            # Get due date and calculate if is overdue

                            # Get due date and current date a split into list
                            task_due = task.split(',')[4].strip().split('/')
                            current_date = date.today().strftime('%d/%m/%Y').split('/')

                            # Create date object with data from previous lists made
                            first_date = date(int(task_due[2]), int(task_due[1]), int(task_due[0]))
                            second_date = date(int(current_date[2]), int(current_date[1]), int(current_date[0]))

                            # Subtract current date from due date
                            delta_difference = first_date - second_date

                            # If task is overdue
                            if delta_difference.days < 1:

                                # Add one to tasks overdue
                                tasks_overdue += 1

            if users_tasks > 0:

                # Set username in user_statistics
                user_statistics["username"] = user.split(',')[0]

                # Define values in dictionary
                user_statistics["total"] = users_tasks

                # Calculate Percentages and assign the values to the users stat dictionary
                user_statistics["percent"] = (users_tasks / all_tasks) * 100
                user_statistics["complete_percentage"] = (tasks_complete / users_tasks) * 100
                user_statistics["not_complete_percentage"] = (tasks_not_complete / users_tasks) * 100
                user_statistics["overdue_percentage"] = (tasks_overdue / users_tasks) * 100

            else:
                user_statistics["username"] = user.split(',')[0]

            # Push user stats to users list
            user_stat_list.append(user_statistics)

    # Create list to hold file output content
    content = []

    # Loop through each users stats and append to content list
    for user in user_stat_list:
        data = f'''
=== {user['username']} ===
Total Tasks:\t\t\t\t\t\t\t {user['total']}
Percent of all tasks assigned to user:\t {round(user['percent'], 2)}%
Percent Complete:\t\t\t\t\t\t {round(user['complete_percentage'], 2)}%
Percent NOT Complete:\t\t\t\t\t {round(user['not_complete_percentage'], 2)}%
Percent Overdue:\t\t\t\t\t\t {round(user['overdue_percentage'], 2)}%
== {user['username']} END ==
'''
        # Append section to content list
        content.append(data)

    # Join content for final output
    file_output = f'''
=== User Statistics ===
{' '.join(content)}

== User Statistics END ==
'''
    with open('user_overview.txt', 'w', encoding='utf-8') as task_overview:
        task_overview.write(file_output)

    clear()
    print("User Statistics Report Generated.")
    time.sleep(1)
    clear()

# Display task Statistics
def display_task_statistics():

    try:

        output = []

        with open('task_overview.txt', 'r', encoding='utf-8') as task_stat:
            for line in task_stat:
                output.append(line.replace('\t', ''))

        print(' '.join(output))

    except:

        # If files don't exist then run the generate stats function

        # Generate task tats
        task_stats()

        # Re try function
        display_task_statistics()


# Display user Statistics
def display_user_statistics():

    try:

        output = []

        with open('user_overview.txt', 'r', encoding='utf-8') as user_stat:
            for line in user_stat:
                output.append(line.replace('\t', ''))

        print(' '.join(output))

    except:

        # If files don't exist then run the generate stats function

        # Generate User stats
        user_stats()

        # Re try function
        display_user_statistics()


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

        # Set login in state to true
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
gr\t - \tGenerate Report
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

        # Call register user function
        reg_user()

    elif menu == 'a':

        # Call add task function
        add_task()

    elif menu == 'va':

        # Call view all function
        view_all()

    elif menu == 'vm':

        # Call view mine function
        view_mine()

    elif menu == 's':

        clear()

        # Check user has permissions to access statistics
        if username == 'admin':

            # Display task stats
            display_task_statistics()

            # Tell user that pressing enter will take them to user stats
            close = input("Press enter to view user stats...")

            # Display user stats
            display_user_statistics()

            # Tell user that pressing enter will take them to main menu
            close = input("Press enter for main menu...")

            clear()

        else:

            # Return insufficient permissions error
            print("You do not have permission to access this feature.")

    elif menu == 'gr':

        if username == 'admin':

            # Generate task statistics
            task_stats()

            # Generate user statistics
            user_stats()

        else:

            # Print insufficient permissions error
            print("You do not have permission to access this feature.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")



# =============== END =============== #