import random


def hangman():
    word_list = ["python", 'letters', 'hacks', 'nothing', 'joke']
    word = word_list[random.randint(0, len(word_list))]
    wrong = 0
    board = ['_'] * len(word)
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\\     ", "|     / \\     ", "|"]
    msg = "Guess a letter\n"
    win = False
    letters = list(word)
    while wrong < len(stages):
        guess_char = input(msg)
        if guess_char in letters:
            char_index = letters.index(guess_char)
            board[char_index] = guess_char
            letters[char_index] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        end_index = wrong + 1
        print("\n".join(stages[0:end_index]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose ! it was {}".format(word))


class Orange:
    pass


if __name__ == '__main__':
    hangman()
