import argparse
from itertools import permutations
import json

input_file = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/puzzle2.json')
input_data = json.load(input_file)
data1 = input_data['jumble']
data2 = list(input_data['finalspace'])
input_file.close()

f = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/freq_dict.json')
data = json.load(f)
words=set(data.keys())
#print(words)
#print(data)
f.close()


#with open('/Users/anamikas/Project/sparkdemo/SparkExcercise/freq_dict.json') as f:
#    data = json.load(f)
#    words = {line.rstrip() for line in f}
#
def word_selection(legal_words):
    chosen_word = ''
    max_useage = -1
    for iter_values in legal_words:
        if(data[iter_values]==1):
            return data[iter_values]
        if(chosen_word == ''):
            chosen_word=iter_values
            max_useage = data[iter_values]
        if(data[iter_values]>0 and max_useage<data[iter_values]):
            max_useage = data[iter_values]
            chosen_word=iter_values
    return chosen_word

def insert_space(mystring, position):
    mystring   =  mystring[:position] + ' ' + mystring[position:] 
    return mystring   


final_sentence=''
for (jumbledword, charPositions) in data1.items():
    perms = set([''.join(p) for p in permutations(jumbledword)])
#    print(perms)
    print('Jumbled Word=',jumbledword)
    print('Permutations=',len(perms))
    legal_words = perms & words
    
    print('Legal Words',legal_words)
    
    chosen_word = word_selection(legal_words)
    print('Correct Word=',chosen_word)
    print()
   
    # Construct the final sentence
#    print('charPositions',charPositions)
#    print('data2',data2)
    

    for i in charPositions:
#        print(chosen_word[i-1])
        final_sentence +=chosen_word[i-1]
#        print('final_sentence=',final_sentence)

print('final_sentence=',final_sentence)
     
#k=0
#for j in data2:
#    final_sentence = insert_space(final_sentence, j+k)
#    k=k+1
#    
#
#
#final_words = final_sentence.split()
## for each word in the line:
#for word in final_words:
#    print('word',word)
#    perm = set([''.join(p) for p in permutations(word)])
##   print(perms)
#    print(len(perm))
#    legal_words = perm & words
#    print('Legal Words',legal_words)
#    chosen_word = word_selection(legal_words)
#    print('ChosenWord=',chosen_word) 
