class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append({"description": task_description, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("\nTask Manager:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['description']}")
        print()

def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager Application")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            task_manager.add_task(task_description)
        elif choice == "2":
            task_manager.show_tasks()
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.complete_task(task_index)
        elif choice == "3":
            task_manager.show_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
