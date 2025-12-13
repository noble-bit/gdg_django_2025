sentence = input("Enter a sentence: ")


words = sentence.split()


freq = {}


for word in words:
    word = word.lower()  
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
