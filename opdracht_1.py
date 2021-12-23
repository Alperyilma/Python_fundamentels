from random import *

def get_random_boolean():
    return round(random()) == 1

sick_days = randint(0,10)
calling_in_sick = False
break_the_loop = False

while not break_the_loop:
    actually_sick = get_random_boolean()
    kinda_sick = get_random_boolean()
    dont_feel_like = get_random_boolean()
    some_sick_days_exist = sick_days > 0

    if actually_sick and some_sick_days_exist:
        sick_days -= 1
        calling_in_sick = True
    elif kinda_sick and dont_feel_like and some_sick_days_exist:
        sick_days -= 1
        calling_in_sick = True
    else:
        pass
    break_the_loop = sick_days <= 0
    print(f"Calling in sick: {calling_in_sick}, remaining sickness days: {sick_days}")
else:
    print("No more sickness days..")






