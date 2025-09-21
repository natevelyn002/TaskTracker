# TaskTracker  

A Python-based Command Line Interface (CLI) and Graphical User Interface (GUI) application for tracking tasks with JSON storage. 

## Description 

The user can add, update, and delete tasks using simple command-line commands. You can also list all your tasks, filter them by status, or search by description. The GUI lets you visually check your to-do list and see task progress in real time.

## Features  

### Command-Line Interface  
- Add new tasks with descriptions  
- Update task descriptions and statuses (`todo`, `in-progress`, `done`)  
- Delete tasks by ID  
- List all tasks or filter by status  
- Check a task’s ID by its description  
- A `help` command for usage instructions  

### Storage  
- Tasks are saved to and loaded from a `tasks.json` file for easy management and data persistence  

### GUI Viewer  
- Basic Tkinter interface (`viewer.py`) displays all tasks with graphical status indicators  
- Automatically refreshes every 2 seconds  

<img src="Screenshot 2025-09-20 at 9.17.19 PM.png" alt="GUI" width="400">

## GIF

![gif](<tasktracker - HD 720p.gif>)