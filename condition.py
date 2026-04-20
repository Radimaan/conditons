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

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    vote = input("Do you want to vote? (yes/no): ")
    if vote.lower() == "yes":
        print("Thank you for voting!")
    else:
        print("You chose not to vote.")
        print("please vote next time.")
else:    print("You are not eligible to vote.")