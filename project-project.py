import time
import random
from collections import Counter


def print_pause(message_to_print):
    # function to print text with a pause afterwards
    print(message_to_print)
    time.sleep(1)


def intro():
    # the story befind the game and the basic objective og the player
    print_pause("\nAs you slowly wake up from a deep sleep, your mind starts")
    print_pause("to think about what your day is going to be like.  As an")
    print_pause("apprentice healer, normal days are filled with chores,")
    print_pause("books and lessons but not today!  Your teacher is off to")
    print_pause("visit colleagues in a neighboring village for the next few")
    print_pause("days so this will be a vacation for you too.  Your only")
    print_pause("responsibility is to keep the cottage in order and take")
    print_pause("care of Clare, your teacher’s pet goat.  As you get ready")
    print_pause("to start your first day of fun, you head outside and")
    print_pause("immediately know there's a problem.  There's a terrible")
    print_pause("stench coming from the attached barn.  Walking over, your")
    print_pause("already sure you know what it is, but you need to confirm")
    print_pause("it.\n")
    time.sleep(5)
    print_pause("There's Clare, happily chewing on some hay.  She pauses as")
    print_pause("you enter, looks at you and bleats happily.  Then, a moment")
    print_pause("later, you hear what sounds like a trumpet come out of her")
    print_pause("other end.  Moments later, the smell hits you and you leave")
    print_pause("the barn nauseous and trying to get a breath of fresh")
    print_pause("air.\n")
    time.sleep(5)
    print_pause("Clare has had this condition before and in no danger.")
    print_pause("Your teacher can remedy this by just feeding her a few")
    print_pause("herbs.  You really don't want to deal with this smell, so")
    print_pause("you come up with a plan.\n")
    time.sleep(5)
    print_pause("You'll need to get some basic supplies in order to hike to")
    print_pause("the nearby hills and get the herbs.  You can work at some")
    print_pause("jobs in town to get the supplies.  The weather is always a")
    print_pause("concern, so you'll need to keep that in mind as well.")
    print_pause("There are three herbs you’ll need but it takes a day to")
    print_pause("hike to each one so that means at least three trips to")
    print_pause("town and three to the hills.  Time to get moving, though")
    print_pause("even with the smell, you’d still rather stay at home.\n")
    time.sleep(5)


def ending(game_status):
    # this is the results of completting the game - win or lose
    if game_status == "win":
        print_pause("You did it!  Clare smells great and now you can relax")
        print_pause("until your teacher returns.  You’re very proud of")
        print_pause("yourself.\n")
    else:
        print_pause("Your teachers happy face slowly turns to a frown upon")
        print_pause("getting the first whiff of Clare.  Reaching into a")
        print_pause("satchel, your teacher feeds Clare some herbs – you")
        print_pause("know by that look your in for a lecture.\n")


def play_again():
    # prompts the player to play again or not and returns that result
    play_again_answer = input("play again? (yes/no): ")
    if play_again_answer == "yes":
        return True
    elif play_again_answer == "no":
        return False
    play_again()


def weather_check():
    # randomply determins what the weather conditions are and retuns it
    types_of_weather = ["good", "good", "good", "good", "good", "bad", "bad"]
    return random.choice(types_of_weather)


def hurbs_check(backpack):
    # counts the number of times the word "hurbs" appears in the
    # backpack list varable
    return backpack.count("hurbs")


def supplies_check(backpack):
    # checks to see if the word "supplies" is in the backpack varable
    # and returns a True or False for yes/no
    if "supplies" in backpack:
        return True
    return False


def hills(backpack):
    # randomly determins if the player finds the hurbs and if so
    # adds them to the backpack
    chance_of_hurbs = random.randint(1, 10)
    if chance_of_hurbs > 3:
        print_pause("Great!  You found some hurbs.  Time to head "
                    "home")
        backpack.append("hurbs")
    else:
        print_pause("sorry, no luck today.  May as well head home.")


def town(backpack):
    # randomly determins if the player is able to work to get
    # supplies added to the backpack
    chance_of_work = random.randint(1, 10)
    if chance_of_work > 3:
        print_pause("Great!  You've earned your surplies for a day.  "
                    "Time to head home")
        backpack.append("supplies")
    else:
        print_pause("sorry, no work today")


def options_check(backpack, weather):
    # determins, based on wweather and what is in the backpack, were
    # the player can go next.  The cottage is always an option
    options = ["cottage"]
    if not supplies_check(backpack):
        options.append("town")
    elif weather == "good":
        options.append("hills")
    return options


def choose_option(options):
    # lets the player decide where to go based on the available options
    if len(options) == 1:
        print_pause("You already have supplies but the weather is to bad ")
        print_pause("to go searching the hills.  You just have to stay home.")
    else:
        print_pause("so you have the folloing options:")
        print_pause(options[0]+" or "+options[1])
        choice = input("please type one in: ")
        if choice not in options:
            choose_option(options)
        return choice


def cottage(backpack):
    # home base for the player.  This will be where the statues of
    # the player is shown and what can come next.
    options = []
    choice = []
    weather = weather_check()
    number_of_hurbs = hurbs_check(backpack)

    print_pause("\n at the start of a new day, review your stats.\n")
    print_pause("Weather is "+weather)
    print_pause("I have "+str(number_of_hurbs)+" hurbs")
    print_pause("I have supplies - "+str(supplies_check(backpack))+"\n")

    options = options_check(backpack, weather)
    choice = choose_option(options)

    if choice == "hills":
        backpack.remove('supplies')
        hills(backpack)
    elif choice == "town":
        town(backpack)


def the_game():
    # the game core, determins the random return date, win/lose stats
    # and starts the game process.
    day_count = 0
    return_day = random.randint(15, 30)
    backpack = []
    game_status = "playing"

    intro()

    while game_status == "playing":
        day_count += 1
        print_pause("\ncurent day count: "+str(day_count))
        print_pause("return day: "+str(return_day)+"\n")
        print_pause("you have "+str(return_day-day_count)+" days left\n")
        if hurbs_check(backpack) == 3:
            game_status = "win"
        elif day_count == return_day:
            game_status = "loss"
        cottage(backpack)

    ending(game_status)

    if play_again():
        the_game()


the_game()
