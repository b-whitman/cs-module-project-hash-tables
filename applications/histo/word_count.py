def word_count(s):
    # Remove ignored characters from string
    # Split string on whitespace
    # Create dict by iterating over set(s)
    # Initialize all values to 0
    # Iterate over s and update counts as you go

    r = '":;,.-+=/\|[]{}()*^&'
    for c in r:
        s = s.replace(c, "")
    
    s = s.split()
    counts = {}
    for w in set(s):
        w = w.lower()
        counts[w] = 0

    for w in s:
        w = w.lower()
        counts[w] += 1

    return counts



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))