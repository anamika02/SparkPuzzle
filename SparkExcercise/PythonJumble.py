import argparse
from itertools import permutations
import json

input_file = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/PythonInput/puzzle1.json')
input_data = json.load(input_file)
data1 = input_data['jumble']
data2 = list(input_data['finalspace'])
input_file.close()

f = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/freq_dict.json')
data = json.load(f)
words=set(data.keys())
#print(words)
print(data)
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


###############Comment this section for performance###################

#perm = set([''.join(p) for p in permutations(final_sentence)])
##print('',perm)
#print('Permutations=',len(perm))
#
#for each_permin in perm:
#    final_list = []
#    prev_pos=0
#    test_list=[]
#    for j in data2:
##        print(each_permin[prev_pos:j])
#        if(each_permin[prev_pos:j] in words):
#            test_list.append(each_permin[prev_pos:j])
#        else:
#            del test_list[:]
#            break;
#        prev_pos=j
#    if len(test_list)>0:
#        final_list.append(test_list)
#        print(test_list)
#
#print(final_list)
#        
