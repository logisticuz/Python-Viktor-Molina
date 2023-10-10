from random import choice

SIGNS =  ["rock", "paper", "scissors"]

def main():
    print(f"Welcome to the {', '.join(SIGNS)} game.")
    print_rules()
    game_loop(3)

def print_rules():
    print("Rules: Each player picks a sign: ")
    for winner, loser in zip ([1, 2, 3], [2, 0, 1]):
        print(f"{SIGNS[winner],title()} wins over {SIGNS[loser]}.")

def game_loop(number_of_rounds):
            for current_rount in range (1, number_of_rounds + 1):
                print(f"\nRound {current_round}:")
                sign_player_a = get_sign_from_user()
                sign_player_b = get_sign_from_computer()
               
               if is_draw(sign_player_a, sign_player_b):
                  print("It's a draw!")
                  if sign in SIGNS:
                            return sign
                  else:
                        print("Computer wins!")

def get_sign_from_user():
     while True:
        sign = input("Pick a sign: ")

        if sign in SIGNS: 
                return sign
        else:
              print(f"You mist pick either")

def get_sign_from_computer():
      while True:
            sign = input("Pick a sign: ")
            if sign in SIGNS
                return sign
            else:
                  
def is_draw 
                  

main()