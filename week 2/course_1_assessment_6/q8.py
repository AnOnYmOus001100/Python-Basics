'''
Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).
'''

original_str = "The quick brown rhino jumped over the extremely lazy fox"

#code
str = original_str.split()
print (str)

num_words_list = []

for word in str:
    num_words_list.append(len(word))
    
print (num_words_list)

