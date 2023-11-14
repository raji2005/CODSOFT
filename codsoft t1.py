class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            print("Tasks:")
            todo_list.show_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
