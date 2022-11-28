import random
import time

card_value = {"Ace":[1,11],"2":2, "3":3, "4":4 , "5":5, "6":6, "7":7, "8":8 , "9":9 , "10":10 , "Jack":10 ,"Queen":10 ,"King":10}

#These are the keys to obtain an integer for the cards
deck_keys = ["Ace","2","3",'4','5','6','7','8','9','10','Jack','Queen','King']

# The kill variable is what ends the program after the user is done playing.
kill = 1
while kill != 0:
    deck = deck_keys *4
    random.shuffle(deck)

    # user_name = input("Hello, welcome to minimalist blackjack! What is your name?: ")
    # time.sleep(2)
    # print(f"Welcome {user_name}! Standard blackjack rules apply.")
    # time.sleep(2)

    # This assigns cards and gets rid of duplicates to accurately simulate odds

    user_card_1 = deck[0]
    del(deck[0])
    dealer_card_1 = deck[0]
    del(deck[0])
    user_card_2 = deck[0]
    del(deck[0])
    dealer_card_2 = deck[0]
    del(deck[0])

    user_name = "Frankie"

    #How an Ace is treated via code, assumed to be 11 initially

        #USER
    if user_card_1 == "Ace":
        user_card_1_int = card_value[user_card_1][1]
    else: 
        user_card_1_int = card_value[user_card_1]

    if user_card_2 == "Ace":
        user_card_2_int = card_value[user_card_2][1]
    else: 
        user_card_2_int = card_value[user_card_2]

        #DEALER

    if dealer_card_1 == "Ace":
        dealer_card_1_int = card_value[dealer_card_1][1]
    else: 
        dealer_card_1_int = card_value[dealer_card_1]

    if dealer_card_2 == "Ace":
        dealer_card_2_int = card_value[dealer_card_2][1]
    else: 
        dealer_card_2_int = card_value[dealer_card_2]

    # The combined value of the card values

    user_total = user_card_1_int + user_card_2_int
    dealer_total = dealer_card_1_int + dealer_card_2_int

    print(f"Your hand: {user_card_1}")
    time.sleep(1)
    print(f"Dealers hand: {dealer_card_1}")
    time.sleep(1)
    print(f"Your hand: {user_card_1} {user_card_2}")
    time.sleep(1)
    print(f"Dealers hand:  {dealer_card_1} {dealer_card_2} ")
    time.sleep(1)

    # If Else statements that push forward the game

        #Dealer value checks to see if a 'push' occurs or the dealer auto wins. 

    if dealer_total and user_total == 21:
        print("That's a push!")
        kill = 0
    elif dealer_total == 21:
        print("The house always wins.")
        kill = 0
    else:
        pass

        #Player value checks to look for automatic win or defaulting two Aces to 1.

    if user_total == 21:
        print(f"{user_name} won the hand!!!")
        
    elif user_total > 21:
        if user_card_1 and user_card_2 == "Ace":
            user_card_1_int = 1
        elif user_card_1 == "Ace":
            user_card_1_int = 1
        elif user_card_2_int == "Ace":
            user_card_2_int = 1

    user_total = user_card_1_int + user_card_2_int
    dealer_total = dealer_card_1_int + dealer_card_2_int

    # This next section of code is me fixing an issue that I could have prevented if I did not represent a card by variables but rather lists. 
    # I need a list to be able to add a card from the top and to track what each player has without needing a new variable with each new card that is hit.

    user_card_list = []
    dealer_card_list = []

    user_card_list.append(user_card_1)
    user_card_list.append(user_card_2)
    dealer_card_list.append(dealer_card_1)
    dealer_card_list.append(dealer_card_2)

# I had to use two separate variables for hit and stand for outside the loop and inside the loop which is why I have two user answer variables.
    user_answer = input("Hit or Stand? Press 1 for Hit, press 2 for Stand.: ")
    user_answer_2 = 1

# The if user__answer = 1 this begins the continous "hit me" program. Otherwise it skips to dealers turn. 
    if user_answer == '1':
        while user_answer_2 != 2:
            # X variable has to exist to keep adding user_total integer. Notice after each 
            x = 0
            user_card_list.append(deck[0])
            del(deck[0])
            time.sleep(2)

            # This portion of user getting greater than 21 has to account for if a player has Aces that can drop to a 1 integer. 
            if sum(card_value.values[user_card_list]) > 21:
            # if user_total + card_value[deck[2 + x]] > 21:
                if user_card_1 or user_card_2 == "Ace":
                    if user_card_1 == "Ace":
                        if user_card_1_int != 1:
                            user_card_1_int = 1
                    elif user_card_2 == "Ace":
                        if user_card_2_int != 1:
                            user_card_2_int = 1
                if sum(card_value.values[user_card_list]) > 21:
                # if user_total + card_value[deck[2 + x]] > 21:
                    print("Bust")
                    time.sleep(2)
                    kill = 0
                    #user answer 2 has to equal 2 to stop the loop
                    user_answer_2 = 2
            elif sum(card_value.values[user_card_list]) == 21:
                print("Blackjack!!!")
                kill = 0
                user_answer_2 = 2
            elif sum(card_value.values[user_card_list]) < 21:
                x + 1
                user_answer_2 = input("Hit or Stand? Press 1 for Hit, press 2 for Stand.: ")
    else:
        pass

    if dealer_total < 17:
        dealer_card_list.append(deck[0])
        del(deck[0])
    else:
        pass

print("End")