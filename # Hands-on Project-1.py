# Hands-on Project-1
## Commmand-line Task manager 
import os 

#file to store stasks
file_name = "tasks.txt"

#Load tasks from file 
def load_tasks():
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"Title": title, "Status": status}
    return tasks

# Save tasks to file 
def save_tasks(tasks):
    with open(file_name, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task["title"]} | {task['status']}\n")
            
# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default = 0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")

# View all tasks 
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

# Mark task as completed 
def mark_task_complete(tasks):
    task_id = int(input("Enter task Id to mark as completed: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "Complete"
        print(f"Task '{tasks[task_id]["title"]}' marked as complete.")
    else:
        print("Task Id not found.")
        
# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task[task_id]['title']}' marked as deleted.")
    else:
        print("Task ID not found.")
        
# Main Menu

def main():
    tasks = load_tasks()
    while True:
        print("\n Task manager menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. MArk task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice =="4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Good Bye. \n Thank You!!!")
            break
        else:
            print("Invalid Choice. Place try again.")
        
        
if __name__ == "__main__":
    main()