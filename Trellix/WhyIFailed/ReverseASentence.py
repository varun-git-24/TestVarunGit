
s = 'This is an amazing'


def revere(input_String):
    words = input_String.split()
    reverse_words = words[::-1]
    reversed = ' '.join(reverse_words)


    return reversed



print(revere(s))
