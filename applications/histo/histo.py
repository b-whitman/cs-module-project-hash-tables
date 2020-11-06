from word_count import word_count

with open("robin.txt") as f:
    words = f.read()

count = word_count(words)

print(count)

# Print a histogram showing the word count for each word, one hash mark
# for every occurrence of the word.

# Output will be first ordered by the number of words, then by the word
# (alphabetically).

# The hash marks should be left justified two spaces after the longest
# word.

# organize the dict by count then alphabetically
# track length of longest word
# for each item in dict, print key, then spaces * longest - len(key), then a # for range(value)
