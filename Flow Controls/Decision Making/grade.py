# Ask the user to enter the mark which is out of 100

# if the mark is above 90 >> A grade
# if the mark is above 75 and less than or equal to 90 >> Bgrade
# if the mark above or equal to 50 and less than or equal to 75 >> c grade
# mark below 50 >> failed

mark = int(input("Enter your mark: "))

if mark >= 0 and mark <= 100:
    if mark > 90:
        print("A grade")

    elif mark > 75 and mark <= 90:
        print("B grade")

    elif mark >= 50 and mark <= 75:
        print("C grade")

    else:
        print("Sorry, You failed the exam.")
else:
    print("The mark should be between 0 and 100")
