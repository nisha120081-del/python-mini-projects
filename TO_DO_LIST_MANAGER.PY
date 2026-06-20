print("Welcome to To-Do List")

tasks = []
completed = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Mark Complete")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # View
    elif choice == "2":
        if tasks:
            print("\nTasks:")
            for task in tasks:
                if task in completed:
                    print(task, "✅")
                else:
                    print(task, "❌ incomplete")
        else:
            print("No tasks")

    # Remove
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed")
        else:
            print("Not found")

    # Mark complete
    elif choice == "4":
        task = input("Enter task to mark complete: ")
        if task in tasks:
            completed.append(task)
            print("Marked as complete ✅")
        else:
            print("Task not found")

    # Exit
    elif choice == "5":
        print("Bye 👋")
        break

    else:
        print("Invalid choice")