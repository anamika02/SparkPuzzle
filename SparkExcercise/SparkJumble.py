#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 00:02:30 2018

@author: anamikas
"""

from __future__ import print_function

import sys
import argparse
from itertools import permutations
import json
import re
import itertools

from pyspark.sql import SparkSession
#-----------------------------------

def jumble_permutations(jumbledword):
    perms = set([''.join(p) for p in permutations(jumbledword)])
#    print(perms)
    print('Jumbled Word=',jumbledword)
    print('Permutations=',len(perms))
    return (perms)

def regex_util(input_str,regex_fn):
    match = re.search(regex_fn, input_str)
# If-statement after search() tests if it succeeded
    if match:
#        print('found', match.group())
        return match.group()
    
    
def word_selection(input_str):
    legal_words = input_str & words
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

def secondary_string(input_str,pos):
    out_str=''
    for a in pos:
        if a!='|':
            out_str+=input_str[int(a)-1]
            print(out_str)
    return out_str

def final_split_indices(indices_str):
    element_list = indices_str.split('|')
    output_list = []
    prev=0
    for i in element_list:
        output_list.append((int(prev),int(i)))
        prev = i
        print(output_list)
    return output_list
#def final_split_indices(indices_str):
    
    
    
if __name__ == "__main__":

    # create an instance of a SparkSession as spark
    spark = SparkSession\
        .builder\
        .appName("JumblePuzzle")\
        .getOrCreate()

    dict_inputPath = "/Users/anamikas/git/SparkPuzzle/SparkExcercise/freq_dict.json"
    puzzle_inputPath = "/Users/anamikas/git/SparkPuzzle/SparkExcercise/SparkInput/puzzle3.csv"

    # create SparkContext as sc
    sc = spark.sparkContext
    
    f = open('/Users/anamikas/git/SparkPuzzle/SparkExcercise/freq_dict.json')
    data = json.load(f)
    words=set(data.keys())
    #print(words)
    #print(data)
    f.close()



#    textfileRDD = sc.textFile(dict_inputPath)
#    filteredtextfileRDD = textfileRDD.filter(lambda line: line.strip() !=('{')).filter(lambda line: line.strip() !=('}'))    
#    textfilePairRDD = filteredtextfileRDD.map(lambda line: (regex_util(line,'[a-zA_Z]+'),int(regex_util(line,'\d+'))))
#    textfileKeyRDD = textfilePairRDD.map(lambda line: line[0])

    
    puzzlefileRDD = sc.textFile(puzzle_inputPath)
    puzzlefilePairRDD = puzzlefileRDD.map(lambda line: ((line.split(',')[0]).replace('"',''),line.split(',')[1]))
#    for a in puzzlefilePairRDD.collect():
#        print('line is',a)
    puzzlePairRDD = puzzlefilePairRDD.filter(lambda line: line[0]!='finalspaces')
    fullStringRDD = puzzlefilePairRDD.filter(lambda line: (line[0]=='finalspaces')).map(lambda line: line[1])
    for a in fullStringRDD.collect():
        print('line(fullStringRDD) is a=',a)
    
    puzzlePermRDD = puzzlePairRDD.map(lambda line: (line[0],jumble_permutations(line[0]),line[1]))
#    for a in puzzlePairRDD.collect():
#        print('line is a=',a)
        
    se = puzzlePermRDD.map(lambda line: (line[0],word_selection(line[1]),line[2]))
    for a in se.collect():
        print('Unjumbled string is =',a)

    
    ader = se.map(lambda line: (line[0],secondary_string(line[1],line[2])))
    for a in ader.collect():
        print('line on selecting specific chars is =',a)
    
    baderrdd = ader.flatMap(lambda val: val[1])
        
    bader = baderrdd.reduce(lambda x,y:x+y)
    print('Jumbled final line is a=',bader)
      
    perm = set([''.join(p) for p in permutations(bader)])
    jumbleRdd = sc.parallelize(perm)
#    for a in jumbleRdd.collect():
#        print('line is a=',a)
    
#    indices = [(0,3),(3,7),(7,11)]
    indices = final_split_indices(fullStringRDD.collect()[0])
    splitStringRDD = jumbleRdd.map(lambda line: ([line[s:e] for s,e in indices]))
#    splitStringRDD.take(100).foreach(print)
    filterStringRDD = splitStringRDD.filter(lambda line: ((line[0]) in words and line[1] in words and line[2] in words))
    filterStringRDD.saveAsTextFile("SparkOutput/puzzle3.solution.text")
    
#    spark.stop()
        
#        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#        print(sc.parallelize(a).map(lambda lin: lin).collect())

#    intersection = textfileKeyRDD.intersection(se)
#    for a in intersection.collect():
#        print('line is',a)

#    puzzlePermRDD = puzzlefilePairRDD.flatMap(lambda line: (set([''.join(p) for p in permutations(line[0])])))
#    for a in puzzlePermRDD.collect():
#        print('line is',a)
#    print(textfileKeyRDD.intersection(puzzlePermRDD).collect())
#    for a in puzzlePermRDD.collect():
#        print('line is',a)

    

