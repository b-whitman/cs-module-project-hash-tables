import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

words = words.split()

# analyze which words can follow other words
# If word is in markov, append idx+1 to list of followers
# If word is not in markov, add to markov as key and init followers list with 
# idx+1
markov = {}
idx = 0
while idx < len(words)-1:
    word = words[idx]
    if word in list(markov):
        followers = markov[word]
        followers.append(words[idx+1])
        markov[word] = followers
    else:
        markov[word] = [words[idx+1]]
    idx += 1




# TODO: construct 5 random sentences


