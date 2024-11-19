sentence = "minhaz"
#
# for x in range(len(sentence), 0, -1):
#     print(sentence[x - 1], end="")

x = ''
for i in sentence:
    x = i + x
print(x)
