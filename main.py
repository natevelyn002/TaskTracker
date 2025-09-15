import sys
import os 
import json
import datetime


# stores the command line arguments as a list 
arguments = sys.argv 

# checks if there are enough arguments. 
if len(arguments) < 3:
    # if there are not enough arguments and error message is printed
    print("Usage: python main.py <command> arguments ... example: python main.py add \"your task description\"")
    sys.exit()

command = arguments[1]
task_file = 'tasks.json'
# gets the current time and date
current_time_and_date = datetime.datetime.now().isoformat()

# reads and loads tasks from the file 
if os.path.exists(task_file):
    with open(task_file, 'r') as file:
        tasks = json.load(file) # reads the file and puts all of the tasks into a list 
        
##
# creates a new task 
if command == "add":
    # checks if there are enough arguments 
    if len(arguments) < 3:
        print("Usage: python main.py add \"your task description\"")
        sys.exit()

    # checking for and creating the json file if it does not exist
    if not os.path.exists(task_file): # checks to see if file exists
        with open(task_file, 'w') as file:
            json.dump([], file) # creates the file and adds an empty list to it

        # confirms program is working if file gets deleted or is being ran for the first time
        print(f"Created new task file {task_file}")

    # reads and loads tasks from the file 
    with open(task_file, 'r') as file:
        tasks = json.load(file) # reads the file and puts all of the tasks into a list 
        task_description = arguments[2]
 

    new_id = 1 
    if tasks:
        new_id = max(task['id'] for task in tasks) + 1 

    new_task = {

        'id': new_id,
        'description': task_description,
        'status': 'todo', 
        'createdAt': current_time_and_date,
        'updatedAt': current_time_and_date 
    }  

    # adding a new task 
    tasks.append(new_task)

    with open(task_file, 'w') as file:
        json.dump(tasks, file, indent=3) # saves all tasks in file

    # print success statement 
    print(f"Task {new_id} was added successfully!!")  

##
# update tasks descripton 
# make all elif / else 
if command == "updateDESC":

    # checks if there are enough arguments 
    if len(arguments) < 4:
        print("Usage: python main.py updateDESC task_id \'new description\'")
        sys.exit()

    # checking if json file does not exist
    if not os.path.exists(task_file):
        print("There are NO tasks to update.")
        sys.exit() 
           
    try:
        task_id = int(arguments[2]) 
        task_description = arguments[3]

        is_found = False

        # going through tasks to find the task with the given ID to update its description
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = task_description
                task['updatedAt'] = current_time_and_date
                is_found = True
                break
        if is_found:
            with open(task_file,'w') as file:
                json.dump(tasks, file, indent=3)
            print(f"Task {task_id} description was updated successfully!!")
        else:
            print(f"Task with id {task_id} was not found!!")
    except ValueError:
        print('Task ID must be an integer.')
        sys.exit()

##
# check task ID 
if command == "checkID":

    # checks if there are enough arguments
    if len(arguments) < 3:
        print("Usage: python main.py checkID 'description' ")
        sys.exit()

    # checking if json file does not exist
    if not os.path.exists(task_file):
        print("There are NO tasks yet.")
        sys.exit()

    task_description = arguments[2]
    found_ID = None

    # going through tasks to find the task with the given description to get its ID
    for task in tasks:
        if task['description'] == task_description:
            found_ID = task['id']
            break

    if found_ID is not None:
        print(f"The task ID is: {found_ID}")
    else:
        print("Task not found.")


##
# update task status 
if command == "update":

    # checks if there are enough arguments
    if len(arguments) < 4:
        print("Usage: python main.py update <task ID> <new status>")
        sys.exit()

    # checking if json file does not exist    
    if not os.path.exists(task_file):
        print("There are NO tasks to update.")
        sys.exit()

    try:
        task_id = int(arguments[2])
        new_status = arguments[3]

        # making the new status is valid
        if new_status not in ["todo", "in-progress", "done"]:
            print("Status must be one of: todo, in-progress, done")
            sys.exit()

        is_found = False 

        # going through tasks to find the task with the given ID to update its status
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = new_status 
                task['updatedAt'] = current_time_and_date
                is_found = True
                break

        if is_found:
            with open(task_file, 'w') as file:
                json.dump(tasks, file, indent=3)
                print(f" Task {task_id} status was updated to {new_status}!")

        else:
            print(f"Task with id {task_id} was not found!!")

    except ValueError:
        print("Task ID must be an integer.")
        sys.exit()                            

##
# delete a task
if command == "delete":
    if len(arguments) < 3:
        print("Usage: python main.py delete <ID>")
        sys.exit()

    if not os.path.exists(task_file):
        print("There are NO tasks to Delete.")
        sys.exit()

    try:
        task_id = int(arguments[2])
        task_found = False

        for task in tasks:

            if task['id'] == task_id:
                tasks.remove(task)
                task_found = True
                break 

        if task_found:
            with open(task_file, 'w') as file:
                json.dump(tasks, file, indent=3)
                print(f"Task {task_id} was deleted successfully!!")
        else:
            print(f"Task with id {task_id} was not found!!")
    except ValueError:
        print("Task ID must be an integer.")
        sys.exit()



        


