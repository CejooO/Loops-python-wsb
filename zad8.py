words = []

while True:
    word = input('Enter a word: ')

    if word:
        words.append(word.upper())
    else:
        break;

for word in words:
    print(word)