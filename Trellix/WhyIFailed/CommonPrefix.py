s=['ac','ad','abgc']
def prefix(inp):
    inp.sort()
    first = inp[0]
    last = inp[-1]

    char = 0
    while char < len(first) and char < len(last) and first[char] == last[char]:
        char = char + 1

    return last[:char]

print(prefix(s))

x = r'[A-Z]'
print(x)