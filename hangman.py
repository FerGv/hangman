import os, platform
wrong_letters = set()
assert_letters = set()
wrongs_counter = 0

os.system('cls') if platform.system() == 'Windows' else os.system('clear')
print("*" * 50)
print("{:^50}".format("JUEGO DEL AHORCADO"))
print("*" * 50)

word = input("\n\n\nIngresa la palabra secreta: ").lower()
os.system('cls') if platform.system() == 'Windows' else os.system('clear')

while True:
    print("\n\nPalabra secreta:", end=" ")
    for letter in word:
        print(letter, end=" ") if letter in assert_letters else print("_", end=" ")

    letter = input("\n\nIngresa una letra: ").lower()

    if letter in word and letter not in assert_letters:
        assert_letters.add(letter)
        if assert_letters == set(word):
            print("\n\t -- GANASTE --")
            print("\t La palabra secreta era: {word}".format(word=word))
            break
    else:
        wrongs_counter += 1
        wrong_letters.add(letter)
        print("\n\t ERROR.")

        if wrongs_counter == 1:
            print(""" 
                     () 
                """)
        elif wrongs_counter == 2:
            print(""" 
                     ()
                     || 
                """)
        elif wrongs_counter == 3:
            print(""" 
                     ()
                     ||\ 
                """)
        elif wrongs_counter == 4:
            print(""" 
                     ()
                    /||\ 
                """)
        elif wrongs_counter == 5:
            print(""" 
                     ()
                    /||\ 
                     /
                """)
        elif wrongs_counter == 6:
            print(""" 
                     ()
                    /||\ 
                     /\\
                """)
            print("\n\t -- PERDISTE --")
            break
