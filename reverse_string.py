word = 'ABCDEF'

print(word[::-1])

# reverse each word of a string

str = 'My Name is Rukaiya'

def reverse_word(sentence):
    words = sentence.split(' ')
    new_words_list = [word[::-1] for word in words]

    print(" ".join(new_words_list))


reverse_word(str)