import time
time.sleep(2)
print ("This is a quiz to test your knowlege of the alphabet.")
print("")
time.sleep(1.75)
print("All answers must use the words that you have learnt from the alphabet game.")
print("")
time.sleep(1.75)
print("Only write in lower case please. ")
print("")
time.sleep(1.75)
print("Type your answer next to the question.")
print("")
time.sleep(2)
print("Ready?")

dictionary = {

    "a": "apple",
    "b": "bandits",
    "c": "cat",
    "d": "dog", 
    "e": "egg",
    "f": "food",
    "g": "garden",
    "h": "hat",
    "i": "ice",
    "j": "jail", 
    "k": "key",
    "l": "lego",
    "m": "milk",
    "n": "night",
    "o": "outside",
    "p": "police",
    "q": "quick",
    "r": "rice",
    "s": "sun", 
    "t": "toys", 
    "u": "up", 
    "v": "vegetables", 
    "w": "water",
    "x": "x-ray",
    "y": "yellow",
    "z": "zebra" }


print ("")
print ("")

time.sleep(3)

for letter in dictionary:
    ans = input(f"What word starts with: '{letter}' ? ")
    while ans != dictionary[letter]:
        print ("")
        print ("")
        print("WRONG. Try again")
        print ("")
        print ("")
        ans = input(f"What word starts with: '{letter}' ? ")
    print ("")
    print ("")
    time.sleep(0.5)
    print("CORRECT. Well Done!")
    print ("")
    print ("")
    time.sleep(0.5)
