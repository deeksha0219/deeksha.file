def word_count_and_frequency(sentence):
    words = sentence.lower().split()  
    word_count = len(words)
    frequency = {}

    for word in words:
        word = word.strip('.,!?()[]{}"\'') 
        frequency[word] = frequency.get(word, 0) + 1

    return word_count, frequency


sentence = input("Enter a sentence: ")
count, freq_dict = word_count_and_frequency(sentence)

print(f"The number of words in the sentence is: {count}")
print("Word frequency:")
for word, frequency in freq_dict.items():
    print(f"  '{word}': {frequency}")