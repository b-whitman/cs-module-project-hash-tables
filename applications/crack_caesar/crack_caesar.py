# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt") as f:
    string = f.read()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
freq_alpha = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
length = len(string)
freq_dict = {}

# for c in alpha:
#     freq_dict[c] = 0

for c in string:
    if c in alpha:
        frequency = round((string.count(c) / length) * 100, 2)
        freq_dict[c] = frequency

sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
key = {}
for idx,c in enumerate(sorted_dict):
    key[c[0]] = freq_alpha[idx]

print(key)

