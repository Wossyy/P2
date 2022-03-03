"""

 Welcome to WAR! This game for the most part plays the same as the regular war card game (the instructions are below).
 The main difference is that when you both draw the same card you get to flip a coin instead of drawing again!

 Also, I had to look up how to print things in the same line on python. This is the source I used to figure
 out how to print things on the same line:
 https://www.geeksforgeeks.org/print-without-newline-python/

 Enjoy! - Alberto

"""

# ↓ Imports needed.
import random
import time

# ↓ Starting animation
time.sleep(1)
print("W", end ="")
time.sleep(.25)
print("e", end ="")
time.sleep(.25)
print("l", end ="")
time.sleep(.25)
print("c", end ="")
time.sleep(.25)
print("o", end ="")
time.sleep(.25)
print("m", end ="")
time.sleep(.25)
print("e", end ="")
time.sleep(.25)
print(" ", end ="")
time.sleep(.25)
print("t", end ="")
time.sleep(.25)
print("o", end ="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print("""                                    
  _____                 _____        _____   
 |\    \   _____    ___|\    \   ___|\    \  
 | |    | /    /|  /    /\    \ |    |\    \ 
 \/     / |    || |    |  |    ||    | |    |
 /     /_  \   \/ |    |__|    ||    |/____/ 
|     // \  \   \ |    .--.    ||    |\    \ 
|    |/   \ |    ||    |  |    ||    | |    |
|\ ___/\   \|   /||____|  |____||____| |____|
| |   | \______/ ||    |  |    ||    | |    |
 \|___|/\ |    | ||____|  |____||____| |____|
         \|____|/ 
""")
time.sleep(1.5)


# ↓ Greets the player, asks if they want to play and if they want to see the instructions again.
ai_top = 0
player_top = 0


def user_input(user_name):
    while True:
        y_n = input("Hi " + user_name + "! Want to play? y or n: ")
        if y_n == "y":
            print("Great!\n")
            time.sleep(1.5)
            while True:
                instructions = input("Do you want to see the instructions on how to play? y or n: ")
                if instructions == "y":
                    print("Ok!")
                    time.sleep(2)
                    print("\nIn this case there are only two players, you (" + user_name + ") and the AI. "
                    "Since theres only two players each player gets half a deck (26 cards) and "
                    "puts them face down.\nThen each player draws the top card of their own deck and "
                    "flips it up at the same time. The player with the highest card takes both "
                    "cards and puts them\n"
                    "face down at the bottom of their deck. If both players draw the same card you can just "
                    "flip a coin and call heads or tails.\n"
                    "The ascending order for the cards is 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K and A.\n")
                    time.sleep(5)
                    go_next = input(user_name + ", Ready to play now? y or n: ")
                    if go_next == "y":
                        print("Ok!")
                        time.sleep(2)
                        return
                    elif go_next == "n":
                        print("Ok.")
                        time.sleep(2)
                        print("Ending the program.")
                        time.sleep(2)
                        exit()
                    else:
                        print("Please enter y or n")
                elif instructions == "n":
                    print("Ok!")
                    time.sleep(2)
                    return
                else:
                    print("Please enter y or n")
        elif y_n == "n":
            print("Ok.")
            time.sleep(2)
            print("Ending the program.")
            time.sleep(2)
            exit()
        elif y_n == "d":
            break
        else:
            print("Please enter y or n")


user_name = input("Please enter your name: ")
user_input(user_name)


# ↓ Dealing animation.
def shuffle():
    print("\nThe deck is being shuffled!")
    time.sleep(2)


shuffle()

# ↓ Actually makes the deck and splits it.
nums = ["2 of ", "3 of ", "4 of ", "5 of ", "6 of ", "7 of ", "8 of ", "9 of ", "10 of ", "J of ", "Q of ",
        "K of ", "A of "]
suites = ["Spades", "Clubs", "Hearts", "Diamonds"]
game_deck = []
for suite in suites:
    for num in nums:
        game_deck.append(str(num) + str(suite))
        random.shuffle(game_deck)
player_half = (game_deck[:26])
ai_half = (game_deck[26:])


# ↓ Makes the deck and draws
def war():
    # ↓ I think I needed to use these global variables or else player_top and ai_top would be set to 0 each time
    # called this function
    global player_top, ai_top
    while True:
        player_top = player_top + 1
        ai_top = ai_top + 1
        player_drawing = input("Press d to draw: ")
        if player_drawing == "d":
            if len(player_half) <= player_top:
                player_top = 0
            else:
                player_card = player_half[player_top]
                print("\nYou drew a " + player_card + "!")
                time.sleep(2.5)
            if len(ai_half) <= ai_top:
                ai_top = 0
            ai_card = ai_half[ai_top]
            print("The AI drew a " + ai_card + "!")
            time.sleep(2.5)
            final_num_p = player_card[0:2]
            if final_num_p == "10":
                final_num_p = 10
            else:
                final_num_p = player_card[0:1]
                if final_num_p == "J":
                    final_num_p = 11
                elif final_num_p == "Q":
                    final_num_p = 12
                elif final_num_p == "K":
                    final_num_p = 13
                elif final_num_p == "A":
                    final_num_p = 14
                else:
                    pass
            final_num_ai = ai_card[0:2]
            if final_num_ai == "10":
                final_num_ai = 10
            else:
                final_num_ai = ai_card[0:1]
                if final_num_ai == "J":
                    final_num_ai = 11
                elif final_num_ai == "Q":
                    final_num_ai = 12
                elif final_num_ai == "K":
                    final_num_ai = 13
                elif final_num_ai == "A":
                    final_num_ai = 14
                else:
                    pass
            if int(final_num_p) == int(final_num_ai):
                print("You drew the same cards! Lets flip a coin to see who wins!")
                print("Lets flip a coin!")
                while True:
                    user_choice = input("Do you want to be heads or tails? h or t: ")
                    if user_choice == "h":
                        flip = random.randint(0, 1)
                        if flip == 0:
                            print("Its heads!")
                            player_half.append(player_card + ai_card)
                            ai_half.remove(ai_card)
                            if len(ai_half) == 0:
                                print("Congrats! You win!")
                                return
                            else:
                                print("You take both cards, you win this round!\n")
                                print("Your deck has " + str(len(player_half)) + " cards")
                                print("The AI's deck has " + str(len(ai_half)) + " cards\n")
                                return
                        else:
                            print("Its tails!")
                            ai_half.append(player_card + ai_card)
                            player_half.remove(player_card)
                            if len(player_half) == 0:
                                print("Oh no! You lost!")
                                return
                            else:
                                print("They take both cards, the AI wins this round!\n")
                                print("Your deck has " + str(len(player_half)) + " cards")
                                print("The AI's deck has " + str(len(ai_half)) + " cards\n")
                                return
                    elif user_choice == "t":
                        flip = random.randint(0, 1)
                        if flip == 0:
                            print("Its heads!")
                            ai_half.append(player_card + ai_card)
                            player_half.remove(player_card)
                            if len(player_half) == 0:
                                print("Oh no! You lost!")
                                return
                            else:
                                print("They take both cards, the AI wins this round!\n")
                                print("Your deck has " + str(len(player_half)) + " cards")
                                print("The AI's deck has " + str(len(ai_half)) + " cards\n")
                                return
                        else:
                            print("Its tails!")
                            player_half.append(player_card + ai_card)
                            ai_half.remove(ai_card)
                            if len(ai_half) == 0:
                                print("Congrats! You win!")
                                return
                            else:
                                print("You take both cards, you win this round!\n")
                                print("Your deck has " + str(len(player_half)) + " cards")
                                print("The AI's deck has " + str(len(ai_half)) + " cards\n")
                                return
                    else:
                        print("Please enter h or t")
            elif int(final_num_p) > int(final_num_ai):
                player_half.append(player_card + ai_card)
                ai_half.remove(ai_card)
                if len(ai_half) == 0:
                    print("Congrats! You win!")
                else:
                    print("You take both cards, you win this round!\n")
                    print("Your deck has " + str(len(player_half)) + " cards")
                    print("The AI's deck has " + str(len(ai_half)) + " cards\n")
            else:
                ai_half.append(player_card + ai_card)
                player_half.remove(player_card)
                if len(player_half) == 0:
                    print("Oh no! You lost!")
                else:
                    print("They take both cards, the AI wins this round!\n")
                    print("Your deck has " + str(len(player_half)) + " cards")
                    print("The AI's deck has " + str(len(ai_half)) + " cards\n")
            return
        else:
            print("Please enter d")


war()


# ↓ Asks the player if they want to have another turn.
while True:
    ans = input("Want another turn? y or n: ")
    if ans == "y":
        print("Great!\n")
        war()
        time.sleep(1)
    elif ans == "n":
        print("Ok.")
        time.sleep(2)
        print("Ending the program.")
        time.sleep(2)
        exit()
    else:
        print("Please enter y or n")
