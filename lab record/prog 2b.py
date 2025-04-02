def word_count(sentance):
    words = sentance.split()
    return len(words)
sentence = input("Enter a sentence: ")
print(f"The number of words in the sentence is: {word_count(sentence)}")
