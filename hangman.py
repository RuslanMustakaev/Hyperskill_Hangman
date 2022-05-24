import random
words_list = ["python", "java", "swift", "javascript"]
win_counter = 0
lost_counter = 0


def open_letter(symbol):
    global word_to_print
    global intended_word
    global word_to_print_set
    word_to_print_list = list(word_to_print)
    for i, v in enumerate(intended_word):
        if v == symbol:
            word_to_print_list[i] = symbol
    word_to_print = "".join(word_to_print_list)
    word_to_print_set = set(word_to_print)
    return word_to_print


print("H A N G M A N")
while True:
    menu_choice = str.lower(input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: > "))
    if menu_choice == "exit":
        break
    elif menu_choice == "results":
        print(f"You won: {win_counter} times.")
        print(f"You lost: {lost_counter} times.")
        continue
    else:
        intended_word = random.choice(words_list)
        intended_word_set = set(list(intended_word))  # For fast find letter in intended word
        user_letters = set()  # For reduce attempt if letter has been already entered
        word_to_print = '-' * len(intended_word)  # First print of hidden word
        word_to_print_set = set(word_to_print)  # For fast determine that word guessed
        print()
        attempt = 8
        while attempt > 0:
            if word_to_print_set == intended_word_set:
                print(f"""You guessed the word {word_to_print}!
You survived!""")
                win_counter += 1
                break
            else:
                print(word_to_print)
                letter = str(input("Input a letter: > "))
                if len(letter) != 1:
                    print("Please, input a single letter.")
                elif not letter.islower() or not letter.isascii():
                    print("Please, enter a lowercase letter from the English alphabet.")
                elif letter in user_letters:
                    print("You've already guessed this letter.")
                elif letter in intended_word_set:
                    user_letters.add(letter)
                    open_letter(letter)
                else:
                    attempt -= 1
                    print("That letter doesn't appear in the word.")
                    user_letters.add(letter)
        else:
            print()
            print("You lost!")
            lost_counter += 1
