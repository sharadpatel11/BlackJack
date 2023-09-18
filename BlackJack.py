import random
import os
import BlackJack_Art

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cardDeck = {"a": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
suits = ['♠', '♥', '♣', '♦']

replay = "yes"
while replay == "yes":
    replay = "none"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BlackJack_Art.logo)
    userCards = [random.choice(cards), random.choice(cards)]
    userCardSum = cardDeck[userCards[0]] + cardDeck[userCards[1]]
    print(f"\nYour Cards: [{userCards[0]}{random.choice(suits)}, {userCards[1]}{random.choice(suits)}]. Total: {userCardSum}")

    dealerCards = [random.choice(cards), random.choice(cards)]
    dealerCardSum = cardDeck[dealerCards[0]] + cardDeck[dealerCards[1]]
    print(f"\nDealer has [{dealerCards[0]}{random.choice(suits)}]. Total: {cardDeck[dealerCards[0]]}")

    userChoice = input("\nWould you like to Hit or Stay?: ")
    userChoice = userChoice.lower()
    while userChoice == "hit" and userCardSum <= 21:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BlackJack_Art.logo)
        userCards.append(random.choice(cards))
        userCardSum += cardDeck[userCards[len(userCards) - 1]]
        print(f"\nYour Cards: {userCards}. Total: {userCardSum}")
        if userCardSum > 21:
            print("Sorry BUST. You lose")
        else:
            userChoice = input("\nWould you like to Hit or Stay?: ")
            userChoice = userChoice.lower()
        print(f"\nDealer has [{dealerCards[0]}{random.choice(suits)}]. Total: {cardDeck[dealerCards[0]]}")


    if(userCardSum <= 21):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BlackJack_Art.logo)
        print(f"\nYour Cards: {userCards}. Total: {userCardSum}")
        while dealerCardSum < userCardSum:
            dealerCards.append(random.choice(cards))
            dealerCardSum += cardDeck[dealerCards[len(dealerCards) - 1]]
        
        print("\n")
        if dealerCardSum > 21:
            print(f"Dealer has {dealerCards}. Total: {dealerCardSum}")
            print("Dealer BUST! You WIN")
        elif dealerCardSum == userCardSum:
            print(f"Dealer has {dealerCards}. Total: {dealerCardSum}")
            print("Tie")
        else:
            print(f"Dealer has {dealerCards}. Total: {dealerCardSum}")
            print("You lose.")

        replay = input("\nWould you like to continue playing? Yes or No: ")
        replay.lower()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BlackJack_Art.logo)
        print(f"\nYour Cards: {userCards}. Total: {userCardSum}")
        while dealerCardSum < 21:
            dealerCards.append(random.choice(cards))
            dealerCardSum += cardDeck[dealerCards[len(dealerCards) - 1]]
        
        print("\n")
        print(f"Dealer has {dealerCards}. Total: {dealerCardSum}")
        replay = input("\nWould you like to continue playing? Yes or No: ")
        replay.lower()

os.system('cls' if os.name == 'nt' else 'clear')