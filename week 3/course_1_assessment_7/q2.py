'''
The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

Hard-coded answers will receive no credit.
'''

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

#code
sentence = sentence.split()

# Write your code here.
same_letter_count = 0
for word in sentence:
    if word[0] == word[-1]:
        same_letter_count += 1
        
print (same_letter_count)

