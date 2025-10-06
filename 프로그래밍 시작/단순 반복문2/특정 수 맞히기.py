while True:
    user_input=int(input())
    if user_input<25:
        print("Higher")
    elif user_input>25:
        print("Lower")
    else:
        print("Good")
        break