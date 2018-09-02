from datetime import datetime
print("today is %02d/%02d/%04d" % (datetime.now().day, datetime.now().month, datetime.now().year))

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()


def greater_less_equal_5(answer):
    if ________:
        return 1
    elif ________:
        return -1
    else:
        return 0



# Make me false!
bool_two = 3 > 5
# Make me true!
bool_three = 3 == 3

# NOT AND OR
# not is evaluated first;
# and is evaluated next;
# or is evaluated last.
