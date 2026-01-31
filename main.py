import functions as fn
done_tasks = []
while True:
    user_actions = input("type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()

    # match user_actions:
    #     case "add":
    #         task = input("Enter the task to add: ") + "\n"
    #         # file = open('list.txt','r') 
    #         # todos = file.readlines()
    #         # file.close()
    #         ## this way we open a external file(list.txt). 'r' is read only permission.
    #         ## there is another way of doing this which is more efficient way to handle an external file.
    #         with open('list.txt','r') as file:
    #             todos = file.readlines()
    #         todos.append(task)
    #         ## open the file with the 'w' write permission.            
    #         # file = open('list.txt','w')  
    #         # file.writelines(todos)
    #         # file.close()
    #         with open('list.txt','w') as file:
    #             file.writelines(todos)

    #     case "show":
    #         # file = open('list.txt', 'r')
    #         # todos = file.readlines()
    #         # file.close()
    #         with open('list.txt','r') as file:
    #             todos = file.readlines()
    #         ## list comprihension : new_todos = [item.strip('\n') for i in todos]            
    #         for i, item in enumerate(todos):
    #             item = item.strip('\n')
    #             print(f"{i+1}: {item.title()}")

    #     case "edit":
    #         number = int(input("Enter the number: "))
    #         index = number - 1
    #         new_task = input("Enter new task: ") + '\n'

    #         with open('list.txt','r') as file:
    #             todos = file.readlines()
    #         todos[index]=new_task

    #         with open('list.txt','w') as file:
    #             file.writelines(todos)

    #     case "complete":
    #         number = int(input("Enter the task completed: "))
    #         index = number - 1
            
    #         with open('list.txt','r') as file:
    #             todos = file.readlines()
            
    #         done = todos.pop(index)
    #         done_tasks.append(done)

    #         with open('list.txt','w') as file:
    #             file.writelines(todos)

    #     case "exit":
    #         break
##### Better and optimized version of the code
    
    if user_actions.startswith("add"):
        task = user_actions[4:] + "\n"

        todos = fn.read_file()
        
        todos.append(task)
        
        fn.write_file(todos)
            
    elif user_actions.startswith("show"):
        todos = fn.read_file()
        ## list comprihension : new_todos = [item.strip('\n') for i in todos]            
        for i, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{i+1}: {item.title()}")

    elif user_actions.startswith("edit"):
        ## the error handling 
        try:
            number = int(user_actions[5:])
            index = number - 1
            new_task = input("Enter new task: ") + '\n'

            todos = fn.read_file()

            todos[index]=new_task
            
            fn.write_file(todos)

        except ValueError:
            print("Please add the S.no after 'edit' keyword")
            continue
    elif user_actions.startswith("complete"):
        try:
            number = int(user_actions[9:])
            index = number - 1
            
            todos = fn.read_file()
            
            done = todos.pop(index)
            done_tasks.append(done)

            fn.write_file(todos)

        except ValueError:
            print("Please add the S.no after 'complete' keyword")
            continue
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_actions.startswith("exit"):
        break
    else:
        print("unknown command")