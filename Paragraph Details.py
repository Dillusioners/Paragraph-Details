#Write a program to grab to a paragraph from the user and get all the words that starts with a vowel and also list all the count the number of words and number of letters in each words.

paragraph = input("Enter a paragraph: ")

words = []

for word in paragraph.split():
    words.append(word)

vowels_start = []

print("*********************************************************")
for i in range(len(words)):
    if words[i][0] in "aeiou":
        vowels_start.append(words[i])

if len(vowels_start) == 0:
    print("No words starts with a vowel in this paragraph.")
else:
    print(f'There are {len(vowels_start)} words in this paragraph that starts with vowels. They are: {vowels_start}')

print("*********************************************************")
print("Number of words in this paragraph: ", len(words))

print("*********************************************************")
for i in range(len(words)):
    has_symbol = False
    length_of_word = len(words[i])
    for j in range(len(words[i])):
        if words[i][j] in ".,/+*-()%$#@!&^}{[]|:;'?><~":
            has_symbol = True

    if has_symbol:
        print(words[i], "has", len(words[i]) - 1, "letters")
    else:
        print(words[i], "has", len(words[i]), "letters")
print("*********************************************************")