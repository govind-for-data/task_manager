import functions as fn
done_tasks = []
while True:
    user_actions = input("type add, show, edit, complete or exit: ")
    user_actions = user_actions.strip()
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