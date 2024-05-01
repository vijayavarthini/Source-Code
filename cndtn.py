# month=input("Enter a Month:  ")

# month="April"

# if month== "January":
#     print("You are in January")
# elif month==" February":
#     print("You are in February")
# elif month== "March":
#     print("You are in March")
# elif month== "April":
#     print("You are in April")
# else:
#     print("Unknown Month")

good_emotion=["good","great","happy"]
bad_emotion=["sad","angry","upset"]
user_emotion=input("How are Feeling Today: ")
if user_emotion in good_emotion:
    print(f"Glad that you're feeling well {user_emotion}")
elif user_emotion in bad_emotion:
    print(f"I am sorry you are feeling {user_emotion}")
else:
    print("I don't know how you are feeling well")