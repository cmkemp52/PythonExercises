sent = ((input("Please enter a word: ")).lower()).split(" ")

results = {}

for word in sent:
    results[word] = 0

for word in sent:
    results[word] +=1


print(results)