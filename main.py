from todo_functions import add_todo, remove_todo, mark_todo, view_todo


file_name = "list.csv"

try:
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
except FileNotFoundError:
 
    todo_file = open(file_name, "w")
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

print("welcome our to do list")

def create_menu():
    print("1. Enetr 1 to add")
    print("2. Enetr 2 to remove")
    print("3. Enetr 3 to mark")
    print("4. Enetr 4 to view to do")
    print("5. Enetr 1 to add")
    print("1. Enetr 5 to exit")
    choice = input("Enetr your selection: ")
    
    return choice

users_choice = ''

while users_choice != '5':
    users_choice = create_menu()
    if users_choice == "1":
        add_todo(file_name)
    elif users_choice == "2":
        remove_todo(file_name)
    elif users_choice == "3":
        mark_todo(file_name)
    elif users_choice == "4":
        view_todo(file_name)
    elif users_choice == "5":
        continue
    else:
        print("Invalid Input")
        
print("Thasnk you for using too do list")
        
    