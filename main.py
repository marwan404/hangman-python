import random

words = ("apple", "banana", "cherry", "date", "elderberry", "game", "goat", "boat")
secret_word = random.choice(words)

hangman_art = {
    0: (
        "   ",
        "   ",
        "   ",
    ),

    1: (
        " o ",
        "   ",
        "   ",
    ),

    2: (
        " o ",
        " | ",
        "   ",
    ),

    3: (
        " o ",
        "/| ",
        "   ",
    ),

    4: (
        " o ",
        "/|\\",
        "   ",
    ),

    5: (
        " o ",
        "/|\\",
        "/  ",
    ),

    6: (
        " o ",
        "/|\\",
        "/ \\",
    )
}

def display_hangman(tries):
    print("************************")
    for line in hangman_art[tries]:
        print(line)
    print("************************")

def display_hint(hint):
    print(" ".join(hint))

def display_word(secret_word):
    print(" ".join(secret_word))

def main():
    hint = ["_"] * len(secret_word)
    guessed_letters = set()
    tries = 0
    is_running = True

    while is_running:
        display_hangman(tries)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
    
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue


        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess :
                    hint[i] = guess
        else:
            tries += 1

        if tries >= 6:
            display_hangman(tries)
            display_word(secret_word)
            print("YO LOOSSEE")
            is_running = False

        if "_" not in hint:
            display_hangman(tries)
            display_word(secret_word)
            print("you win!!!!")
            is_running = False


if __name__ == "__main__":
    main()