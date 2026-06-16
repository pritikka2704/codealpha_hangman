import random

WORDS=["hangman","python","network","signal","program"]

HANGMAN=[
    """
       +---+
       |   |
           |
           |
           |
           |
     =========""",

      """
       +---+
       |   |
       0   |
           |
           |
           |
     =========""",

      """
       +---+
       |   |
       0   |
       |   |
           |
           |
     =========""",

     """
       +---+
       |   |
       0   |
      /|   |
           |
           |
     =========""",

     """
       +---+
       |   |
       0   |
      /|\\  |
           |
           |
     =========""",

      """
       +---+
       |   |
       0   |
      /|\\  |
      /    |
           |
     =========""",

      """
       +---+
       |   |
       0   |
      /|\\  |
      / \\  |
           |
     ========="""
]
def display_state(wrong_count,guessed_letters,word):
    print(HANGMAN[wrong_count])

    lives_left = 6 - wrong_count
    hearts = "❤️ " * lives_left + "🖤 " * wrong_count
    print(f"\n  Lives : {hearts}")

    print(f"  ❌ Wrong Guesses left : {lives_left}")
    print(f"  🔤 Letters Guessed   : {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")

    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\n  📝 Word : {display_word}\n")


def get_guess(guessed_letters):
    while True:
        guess = input("  👉 Guess a letter : ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠️  Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"  ⚠️  You already guessed '{guess}'. Try again!")
        else:
            return guess
def play():
    word=random.choice(WORDS)
    guessed_letters=set()
    wrong_count=0
    max_wrong=6
    
    print("\n===============================")
    print("     WELCOME TO HANGMAN!")
    print("\n===============================")

    while True:
         display_state(wrong_count,guessed_letters,word)

         if all(letter in guessed_letters for letter in word):
             print(f"  🎉 Congratulations! You guessed the word '{word}'! 🎊")
             break
         
         if wrong_count>=max_wrong:
                print(f"  💀 Game Over! The word was : '{word}'")
                break

         guess=get_guess(guessed_letters)
         guessed_letters.add(guess)

         if guess in word:
                print(f"\n  ✅ Nice! '{guess}' is in the word! 🎯")
         else:
                wrong_count+=1
                print(f"\n  ❌ '{guess}' is not in the word! 😬")
    print()       
    again = input("  🔄 Play again? (y/n) : ").strip().lower()
    
    if again=="y":
        play()
    else:
        print("\n  👋 Thanks for playing! Bye! 😊\n")
if __name__=="__main__":
    play()

        






    


        
        






    
