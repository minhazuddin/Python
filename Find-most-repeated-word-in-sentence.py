sentence = "This is a common interview question"
most_repeated = {}

for x in sentence:
    most_repeated[x] = most_repeated.get(x, 0) + 1

most_repeated_sorted = sorted(most_repeated.items(), key=lambda item: item[1], reverse=True)

print(f"Most sorted word is '{most_repeated_sorted[0][0]}' which is repeated {most_repeated_sorted[0][1]} times")


# Or

sentence2 = "This is a common interview question"
print(max(set(sentence2), key=sentence2.count))
