# Simple To-Do List Program

tasks = []

while True:
    print("\n=== SIMPLE TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            try:
                remove_index = int(input("Which task number to remove? ")) - 1
                removed = tasks.pop(remove_index)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid choice.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option.")
