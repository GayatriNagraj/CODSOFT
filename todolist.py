todo_list = []
while True :
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("=====================")

    choice = input("Enter your Choice(1-5): ")
      
    if choice == '1':
        task = input("Enter the Task :")
        todo_list.append(task)
        print("Task added Succesfully!!")

    elif choice =='2':
        if todo_list:
            print("\nTasks:")
            for index, task in enumerate (todo_list, start=1):
                print(f"{index}.{task}")
        else:
            print("No tasks Added yet.")
        
    elif choice == '3':
        if todo_list:
            print("\nTasks:")
            for index, task in enumerate(todo_list, start=1):
                print (f"{index}.{task}")
            task_number = int(input("Enter the task you want to Update: "))
            if 1 <= task_number <=len(todo_list):
                updated_task = input ("Enter the Updated task: ")
                todo_list[task_number - 1] = updated_task
                print("Task Updated Succesfully!!")
            else:
                print("Invalid Task Number..")
         
        else:
            print("No Tasks Added yet.")

    elif choice == '4':
        if todo_list:
            print("\nTasks:")
            for index, task in enumerate(todo_list, start=1):
               print(f"{index}.{task}")
            task_number = int(input("Enter the number of Task to delete:"))
            if 1<= task_number <= len(todo_list):
                del todo_list[task_number - 1]
                print ("Task Deleted Succesfully!!")
            else:
                print("Invalid task Number")
        else:
            print("No tasks Added")
    
    elif choice == '5':
        print("Exiting Program")
        break
    else:
        print("Invalid Choice..")
           