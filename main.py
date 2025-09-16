import sys
import os 
import json
import datetime

# stores the command line arguments as a list 
arguments = sys.argv 

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
elif command == "updateDESC":

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
elif command == "checkID":

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
elif command == "update":

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
elif command == "delete":
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

##
# list all tasks 

elif command == "listALL":

    if len(arguments) < 2:
        print("Usage:  python main.py listALL")
        sys.exit()

    if not os.path.exists(task_file):
        print("There are NO tasks to List.")
        sys.exit()

    if not tasks:
        print("There are NO tasks to List.")
        sys.exit()    

    print("Listing all tasks:")
    print(tasks)

    for task in tasks:
        print(f"ID: {task['id']} \n Description: {task['description']} \n Status: {task['status']} \n Created At: {task['createdAt']} \n Updated At: {task['updatedAt']}")
        print("")


        
##
# list tasks by status to-do
elif command == "listTODO":
    if len(arguments) < 2:
        print("Usage:  python main.py listTODO")
        sys.exit()

    if not os.path.exists(task_file):
        print("There are NO tasks to-do List.")
        sys.exit()


    todo_tasks = []
    for task in tasks:
        if task["status"] == "todo":
            todo_tasks.append(task)

    if not todo_tasks:
        print("There are NO tasks with status 'todo'.")
        sys.exit()

    print("Listing all tasks with status 'todo':")
    for task in todo_tasks:
        print(f"ID: {task['id']} \n Description: {task['description']} \n Status: {task['status']} \n Created At: {task['createdAt']} \n Updated At: {task['updatedAt']}")
        print("")

##
# list tasks by status in-progress
elif command == "listINPROG":
    if len(arguments) < 2:
        print("Usage:  python main.py listINPROG")
        sys.exit()

    if not os.path.exists(task_file):
        print("There are NO tasks to List.")
        sys.exit()


    inprog_tasks = []
    for task in tasks:
        if task["status"] == "in-progress":
            inprog_tasks.append(task)

    if not inprog_tasks:
        print("There are NO tasks with status 'in-progress'.")
        sys.exit()

    print("Listing all tasks with status 'in-progress':")
    for task in inprog_tasks:
        print(f"ID: {task['id']} \n Description: {task['description']} \n Status: {task['status']} \n Created At: {task['createdAt']} \n Updated At: {task['updatedAt']}")
        print("")

##
# list tasks by status done
elif command == "listDONE":
    if len(arguments) < 2:
        print("Usage:  python main.py listDONE")
        sys.exit()

    if not os.path.exists(task_file):
        print("There are NO tasks to List.")
        sys.exit()


    done_tasks = []
    for task in tasks:
        if task["status"] == "done":
            done_tasks.append(task)

    if not done_tasks:
        print("There are NO tasks with status 'done'.")
        sys.exit()

    print("Listing all tasks with status 'done':")
    for task in done_tasks:
        print(f"ID: {task['id']} \n Description: {task['description']} \n Status: {task['status']} \n Created At: {task['createdAt']} \n Updated At: {task['updatedAt']}")
        print("")

##
# help command
elif command == "help":
    print("Task Management Application Commands:\n")
    print("1. Add a new task:")
    print("   python main.py add \"task description\" \n")
    print("2. Update task description:")
    print("   python main.py updateDESC task_id \"new description\" \n")
    print("3. Check task ID by description:")
    print("   python main.py checkID \"task description\" \n")
    print("4. Update task status:")
    print("   python main.py update task_id new_status (new_status must be one of: todo, in-progress, done) \n")
    print("5. Delete a task:")
    print("   python main.py delete task_id \n ")
    print("6. List all tasks:")
    print("   python main.py listALL \n")
    print("7. List tasks with status 'todo':")
    print("   python main.py listTODO \n ")
    print("8. List tasks with status 'in-progress':")
    print("   python main.py listINPROG \n")
    print("9. List tasks with status 'done':")
    print("   python main.py listDONE \n")
    print("10. Display this help message:")
    print("   python main.py help \n")

##
# invalid command
else: 
    print(f"Invalid command: {command}")
    print("Use 'python main.py help' to see the list of available commands.")
    sys.exit()







        


