def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)  

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")
        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item.strip("\n")}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")
            
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            write_todos("todos.txt", todos)
        except ValueError:
            print("You command was not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos("todos.txt", todos)

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
   