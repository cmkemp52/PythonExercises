sent = (input("Please enter a string: ").lower()).split(" ")


results = {}

for word in sent:
    results[word] = 0

for word in sent:
    results[word] +=1

end = results.copy()
sortedresl = []
while len(sortedresl)<3:
    top=0
    for thing in results:
        if(results[thing]>top):
            top=results[thing]
    for thing in results:
        if(results[thing]==top):
            sortedresl.append(thing)
            results.pop(thing)
            break

print("The top three words are:")
print(sortedresl[0], ": ", end[sortedresl[0]])
print(sortedresl[1], ": ", end[sortedresl[1]])
print(sortedresl[2], ": ", end[sortedresl[2]])
