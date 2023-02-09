# place above code in a function and run examples covering , print of male customer , female customer and a young customer.
# 7 minutes

def clubcheckin(age = 18,gender = "female"):
    if age >= 0 and age <= 17:
        return "Too young"
    elif age >= 18 and gender == "male":
        return "Can go in! But does not receive a free drink"
    elif age >= 18 and gender == "female":
        return "Can go in! Receives a free drink, it's ladies night"
    else:
        return "Invalid input"

age = int(input(" Enter your age "))
gender = input("Enter your gender(male,female)")

print(clubcheckin(age,gender))


