import CRUD_DATABASE


"""
Currenly working on a small app that:
VIEWS
ADDS
UPDATES
DELETES
already made customer data
"""

#Adding the data that was given
def add_items():
    CRUD_DATABASE.add_items()


#viewing all the data OR one per time OR a certian no. per time
def view_all_data():
    CRUD_DATABASE.viewall_customer_data()

#update first_name
def update_first_name() :
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        new_first_name = input("Enter a new first name:\n")
        CRUD_DATABASE.update_first_name(row_id, new_first_name)
    except Exception as e:
        print(f"❌ Error: {e}")

#update last name
def update_last_name() :
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        new_last_name = input("Enter a new first name:\n")
        CRUD_DATABASE.update_last_name(row_id, new_last_name)
    except Exception as e:
        print(f"❌ Error: {e}")

#update email
def update_email() :
    try:
        row_id = int(input("Enter the ID you want to update:\n"))
        email = input("Enter a new email:\n")
        CRUD_DATABASE.update_email(row_id, email)
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_row_input():
    try:
        print("🔥 DELETE FUNCTION CALLED")
        CRUD_DATABASE.viewall_customer_data()
        row_id = int(input(f"\nThis is the data choose which rowID to remove:\n"))
        CRUD_DATABASE.delete_row(row_id)
    except Exception as e:
        print(f"❌ Error: {e}")

title = "Welcome"
print(title.center(60, "="))

quit_out = True

#exitout function
def exitout():
    global quit_out
    quit_out = False
    print()
    print("Closing Databse backend goodbye!")
    goodbye = ""
    print(goodbye.center(60, "="))
    exit = False

while quit_out:

        heading =""
        print(heading.center(60, "="))
        choice = int(input("Welcome to your Database backend, what would you like to do?\n1.Add the assignment data " \
        "\n2.View all the data in table\n3.Remove a row of data\n4.Update first name\n5.Update last name\n6.Update email\n7.Exit\nInput here: "))
        #ADDING THE LOGIC CONTROLERS
        if choice == 1:
            add_items()
        elif choice == 2:
            view_all_data()
        elif choice == 3:
            delete_row_input()
        elif choice == 4:
            update_first_name()
        elif choice == 5:
            update_last_name()
        elif choice == 6:
            update_email()
        elif choice == 7:
            exitout()
        else:
            print("Please enter a valid option!!")
    