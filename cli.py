# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d %b, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.rstrip("\n")
            print(f"{index + 1}-{item.title()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            todos[number - 1] = input("Enter new todo: ") + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[8:])

            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

        print(f"Todo \"{todo_to_remove}\" was removed from the list.")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")
print("Bye!")
