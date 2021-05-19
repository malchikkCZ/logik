import os
import random


LOGO = """
+--+                       +--+
|  |                   ++  |  |
|  |    /----\\ /----\\ +--+ |  | __
|  |    | /\\ | | /\\ | |  | |  |/ /
|  +--+ | \\/ | | \\/ | |  | |  |\\ \\
+-----+ \\----/ \\--+ | +--+ +--+ \\_\\
                  /_/
"""


def print_header():
    print(LOGO)
    print("You need to guess the 4-digit code composed of digits from 1 to 8. Individual digits can be repeated.")
    print("The computer will always evaluate your guess: X = correctly placed number, O = correctly guessed number.")
    print("You have a total of 10 attempts to guess the code.")
    print()


def evaluate_answer(logik, answer):
    bk_score = 0
    wh_score = 0
    temp_logik = []
    temp_answer = []

    for i in range(4):
        if logik[i] == answer[i]:
            bk_score += 1
        else:
            temp_logik.append(logik[i])
            temp_answer.append(answer[i])
  
    for j in range(len(temp_logik)):
        if temp_answer[j] in temp_logik:
            cnt_logik = temp_logik.count(temp_answer[j])
            cnt_answer = temp_answer.count(temp_answer[j])
            if cnt_answer > cnt_logik:
                temp_answer[j] = 0
            else:
                wh_score += 1

    hint = bk_score * "X" + wh_score * "O"
    return hint


def get_user_tip(attempt):
    user_answer = input(f"Attempt nr.{attempt:2} >>> ")
    try:
        listed_answer = [int(x) for x in user_answer]
        if len(listed_answer) != 4 or min(listed_answer) < 1 or max(listed_answer) > 8:
            raise ValueError
    except ValueError:
        print("Your answer has to contain exactly four digits from 1 to 8.")
        return None
    else:
        return listed_answer


def game():
    os.system('cls' if os.name=='nt' else 'clear')
    print_header()

    logik = [random.randint(1, 8) for _ in range(4)]

    for attempt in range(1, 11):
        answer = get_user_tip(attempt)
        while not answer:
            answer = get_user_tip(attempt)
        if answer == logik:
            print("                  XXXX")
            print(f"\nGreat, you won! You guessed the number: {''.join(map(str, logik))}")
            return
        else:
            print(f"                  {evaluate_answer(logik, answer)}")
    
    print(f"\nYou missed all attempts, the correct answer was: {''.join(map(str, logik))}")


game_is_on = True
while game_is_on:
    game()
    game_is_on = input("Do you want to play again? (Y/n) ").lower() != "n"

print("Thank you for playing my game!")
