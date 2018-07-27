import argparse
from itertools import permutations
import json

#parser = argparse.ArgumentParser(description='Solver for Jumble')
#parser.add_argument('jumbledwords', nargs='+',
#                    help='One or more jumbled words')
#argv = parser.parse_args()

input_file = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/puzzle2.json')
input_data = json.load(input_file)
data1 = input_data['jumble']
data2 = list(input_data['finalspace'])
input_file.close()

f = open('/Users/anamikas/Project/sparkdemo/SparkExcercise/freq_dict.json')
data = json.load(f)
words=set(data.keys())
print(words)
#print(data)
f.close()
# Now you can use data as a normal dict:

#for (k, v) in data.items():
#   print("Key: " + k)
#   print("Value: " + str(v))


#with open('/Users/anamikas/Project/sparkdemo/SparkExcercise/freq_dict.json') as f:
#    data = json.load(f)
#    words = {line.rstrip() for line in f}
#
final_sentence=''
for (jumbledword, charPositions) in data1.items():
    perms = set([''.join(p) for p in permutations(jumbledword)])
#    print(perms)
    print(len(perms))
    legal_words = perms & words
    
    print('Legal Words',legal_words)
    
    chosen_word = ''
    max_useage = 0
    for iter_values in legal_words:
        if chosen_word == '':
            chosen_word=iter_values
        if(data[iter_values]>max_useage):
            max_useage = data[iter_values]
            chosen_word = iter_values
    print('ChosenWord=',chosen_word) 
   
    # Construct the final sentence
    print('charPositions',charPositions)
    print('data2',data2)
    

    for i in charPositions:
        print(chosen_word[i-1])
        final_sentence +=chosen_word[i-1]
        print('final_sentence=',final_sentence)
        


def insert_space(mystring, position):
    mystring   =  mystring[:position] + ' ' + mystring[position:] 
    return mystring   


k=0
for j in data2:
    final_sentence = insert_space(final_sentence, j+k)
    k=k+1
    
print('final_sentence=',final_sentence)
    
    
    
        
    
#    print(jumbledword, legal_words)
    
