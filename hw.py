text = ["H","e","l","l","o"," ","W","o","r","l","d","!"]
l = len(text)

print("".join(text))

for i in range(int(l/2)):
	temp = text[i]
	text[i] = text[l-1-i]
	text[l-1-i] = temp

words2 = "".join(text)

print(words2)
