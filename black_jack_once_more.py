import random,os
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def blackjack():
    user_game_on=True
    user_cards=[]
    computer_cards=[]
    user_sum=0
    computer_sum=0
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
            
    for i in range(len(user_cards)):
        user_sum+=user_cards[i]
        
    for i in range(len(computer_cards)):
        computer_sum+=computer_cards[i]
            
    print(f"the user cards are {user_cards} and they sum up to {user_sum}")
    print(f"the first card of the computer is {computer_cards[0]}")
        
    
    while user_game_on:
        
        if user_sum==21:
            print('You have a blackjack hence you Won the game')
            return
        
        elif computer_sum==21:
            print('Computer has a blackjack it won you lost!')
            return
        
        else:
            if user_sum>21:
                
                if 11 in user_cards:
                    a=user_cards.index(11)
                    user_cards[a]=1
                    user_sum=user_sum-11+1
                    print(f'Now your cards are {user_cards}  and the updated user_sum is {user_sum}')
                
                else:
                    print('You lost the game return to main screen!\n')
                    return
                
                
            ask= input(" do you want to choose a card\n type 'y' for yes and 'n' for no\n")
            if ask=='n':
                user_game_on=False
            else:
                a=deal_card()
                user_cards.append(a)
                user_sum+=a
                print(f'Now ur cards are {user_cards}  and ur score became {user_sum}\n')
                
    computer_game_on=True
    while computer_game_on:
        if computer_sum>=17:
            computer_game_on=False
        
        else:
            a=deal_card()
            computer_sum+=a
            computer_cards.append(a)
            
    if computer_sum>21:
        print('Computer lost! you won!')
        
    elif computer_sum==21:
        print('Computer won the game!')
            
    elif user_sum>computer_sum:
        print(f'User Won! as score is computer is {computer_sum} and ur score is {user_sum}')
    
    elif user_sum==computer_sum:
        print(f'It\'s a draw! as score is computer is {computer_sum} and ur score is {user_sum}')
        
    else:
        print(f'Computer Won! as score is computer is {computer_sum} and ur score is {user_sum}')

    return            
                 
while input("Do you wanna play black jack game type 'y' for yes and 'n' for no ").lower()=='y':
    os.system('cls')
    blackjack()