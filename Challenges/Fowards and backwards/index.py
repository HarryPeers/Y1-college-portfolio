while True:
    word = input("Please enter a word\n   ")

    if word == "".join(reversed(list(word))):
        print("That is a palindrome")
    else:
        print("That is not a palindrome")

    print("\n")