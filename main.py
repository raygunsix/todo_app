import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item.strip("\n")}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("You command was not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos(todos)

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
   