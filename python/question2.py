#Test case 1


def get_len_of_most_freq_word_count(text):
    words_lst = text.lower().split(" ")
    unique_words = set(words_lst)

    most_freq_word_count = 0
    most_freq_word = ""
    for word in unique_words:
        count = words_lst.count(word)
        if count > most_freq_word_count:
            most_freq_word_count = count
            most_freq_word = word
    print(most_freq_word)
    return len(most_freq_word)


test1 = "write write write write all the number from from 1 to 100"
print("Length of most frequent word is ",get_len_of_most_freq_word_count(test1))
"""
Explaination : 
"test1" has 2 most frequent words "write" and "from" where  "write" appears 4 times and "from" appears 2 times. 
The length of the word "write" is 5 so function should return 5
"""
#############
test2 = "Today today today today we have exam exam exam in ineuron institute."
print("Length of most frequent word is ",get_len_of_most_freq_word_count(test2))
"""
Explaination : 
"test2" has 2 most frequent words "today" and "exam" where  "write" appears 4 times and "exam" appears 3 times. 
The length of the word "today" is 5 so function should return 5
"""