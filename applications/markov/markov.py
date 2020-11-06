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
# A word is a start word if its first char is uppercase or "uppercase
# A word is a stop word if its last char is .!? or .!?"
# Make start and stop word lists by iterating over markov keys
# Starting from randomly chosen start word, choose random word from followers, place in list, get new followers
# If word is stop, break out of loop
# Iterate over list, print(s, end=" ") each string. /n after stop.

start = []
stop = '.!?'

for word in list(markov):
    if len(word) > 2 and word[-1] != '"':
        if word[0].isupper() or word[1].isupper():
            start.append(word)

for i in range(5):
    idx = random.randint(0, len(start))
    sentence = [start[idx]]
    while sentence[-1][-1] not in stop and sentence[-1][-2] not in stop:
        followers = markov[sentence[-1]]
        idx = random.randint(0, len(followers)-1)
        sentence.append(followers[idx])
    
    print(sentence)
