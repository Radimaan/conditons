# marks = 8
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B") 
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:    print(type("Grade: F"))

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
#     vote = input("Do you want to vote? (yes/no): ")
#     if vote.lower() == "yes":
#         print("Thank you for voting!")
#     else:
#         print("You chose not to vote.")
#         print("please vote next time.")
# else:    print("You are not eligible to vote.👋")

stored_USerNAme = "Admin"
Stored_password = "1234"
Account_Active = True
login_Attrmpts = 3

username = input("inter your user name")
password = input("inter your passwod")

user_matching = username == stored_USerNAme
password_matching = password == Stored_password

Login_seccess = user_matching and password_matching and Account_Active

account_loked = login_Attrmpts <= 0

if account_loked:
    print("Your account is locked. Please contact support.")
elif Login_seccess:
    print("✅✅Login successful! Welcome, Admin.")
    you_can_access = True
    print("You can access the admin dashboard.")
    print("You can manage users, view reports, and configure settings.")
    print("Remember to log out after your session for security.")
    print("your balance : $ 12908.00")
    print("your last login : 2024-06-15 14:30:00")
else:
    login_Attrmpts -= 1
    print(f"Login failed. You have {login_Attrmpts} attempts left.")
    while login_Attrmpts > 0 and not Login_seccess:
        username = input("inter your user name")
        password = input("inter your passwod")
        user_matching = username == stored_USerNAme
        password_matching = password == Stored_password
        Login_seccess = user_matching and password_matching and Account_Active
        if Login_seccess:
            print("✅✅Login successful! Welcome, Admin.")
            you_can_access = True
            print("You can access the admin dashboard.")
            print("You can manage users, view reports, and configure settings.")
            print("Remember to log out after your session for security.")
            print("your balance : $ 12908.00")
            print("your last login : 2024-06-15 14:30:00")
            break
        else:
            login_Attrmpts -= 1
            print(f"Login failed. You have {login_Attrmpts} attempts left.")
