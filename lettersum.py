sent = input("Please enter a word: ")

results = {}

for letter in sent:
    results[letter] = 0

for letter in sent:
    results[letter] +=1


print(results)