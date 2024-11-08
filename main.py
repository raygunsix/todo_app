while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)    

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item.strip("\n")}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos.txt', 'r') as file:
                    todos = file.readlines()
            
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)  
        except ValueError:
            print("You command was not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open('todos.txt', 'r') as file:
                    todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)  

            message = f"Todo {todo_to_remove.strip('\n')} was removed"
            print(message)
        except ValueError:
            print("You command was not valid")
            continue
        except IndexError: 
            print("There is no item with that number")
            continue
        
    elif 'exit' in user_action:
        break

    else:
         print("The command is not valid")

print("Bye")
   