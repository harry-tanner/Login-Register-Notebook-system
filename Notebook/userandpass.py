import re
import os
BASE_PATH = r"C:\Users\hrytn\OneDrive - Willow Learning Trust\Year 10\Computer Science\Python2\userandpassword"
MASTER_FOLDER= os.path.join(BASE_PATH, "User_Data")
userpass_path=os.path.join(BASE_PATH, "Userpass.txt")
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(pattern, email) is not None
def login():
    file = open(userpass_path, "r")
    checkuser = input("What is your username: ").lower().strip()
    checkpass = input("What is your password: ").strip()
    
    success = False
    
    for line in file:
        # Split the line by ", " to get each part
        parts = line.strip().split(", ")
        # parts[0] = "Name: Bob"
        # parts[1] = "Username: bobb1"
        # parts[2] = "Email: bob@test.com"
        # parts[3] = "Password: Bobob1234!"
        
        # Now extract just the values (after the ": ")
        try:
            stored_username = parts[1].replace("Username: ", "")
            stored_password = parts[3].replace("Password: ", "")
        except IndexError:
            continue  # Skip lines that don't have the right format
        
        # Check for EXACT match
        if stored_username == checkuser and stored_password == checkpass:
            success = True
            break
    
    file.close()
    
    if success:
        print("Login successful!")
        
        user_folder = os.path.join(MASTER_FOLDER, checkuser)
        notebook_path = os.path.join(user_folder, "notebook.txt")
        
        if not os.path.exists(notebook_path):
            os.makedirs(user_folder, exist_ok=True)
            with open(notebook_path, "w") as notebook:
                notebook.write(f"Welcome to your notebook, {checkuser}!\n")
        
        with open(notebook_path, "a") as notebook:
            note = input("Write a note: ")
            notebook.write(note + "\n")
        print("Note saved!")
    else:
        print("Login Failed. Incorrect username or password")
    
            
    

def register():
    file = open(userpass_path, "r")
    name = input("What is your name? ")
    print("Hello", name)

    while True:
        username = input("What would you like your username to be? ").lower().strip()
        if len(username) <= 4:
            print("Username is too short")
            continue
        # Reset file to top before searching
        file.seek(0)
        
        # Check if username is taken
        taken = False
        for line in file:
            if username in line:
                taken = True
                break
        # Decides what to do
        if taken == True:
            print("Username already taken, try again")
        else:
            print("Username accepted")
            break
    while True:
        email=input("What is your email").lower().strip()
        if not is_valid_email(email):
            print("Invalid email format")
            continue
        taken= False
        file.seek(0)
        for line in file:
            if email in line:
                taken= True
                break
        if taken == True:
            print("Email already taken, try again")
        else:
            print("Email accepted")
            break
            
    while True:
        password=input("What would you like your password to be. Must have atleast 8 characters, contain atleast 1 capital and lowercase letter, and a symbol").strip()
        if len (password)>=8 and any(c.islower()for c in password) and any (c.isupper() for c in password) and any(c.isdigit() for c in password) and any (not c.isalnum()for c in password):
            print("Password accepted")
            break
        else:
            print("Password not accepted, make sure it has 8 characters, atleast 1 capital and lowercase letter, and a symbol")
        file.seek(0)
    while True:
        password2=input("Re-enter your password").strip()
        if password==password2:
            print("Account created")
            break
        else:
            print("Passwords don't match, please try again")
            continue
    file.close()
    file=open(userpass_path,"a")
    file.write(f"Name: {name}, Username: {username}, Email: {email}, Password: {password}\n")
    file.close()
    user_folder=os.path.join(MASTER_FOLDER, username)
    os.makedirs(user_folder, exist_ok=True)
    notebook_path=os.path.join(user_folder, "notebook.txt")
    with open(notebook_path, "w") as notebook:
        notebook.write(f"Welcome to your notebook, {name}!\n")
    print("Account created and folder made!")

while True:
    answer = input("Would you like to login or register? ").strip().lower()
    if answer == "register":
        register()
        print("Now please log in with your new account.")
    elif answer == "login":
        login()
        break
    else:
        print("Please type login or register")
        
            
                
    
    
    

