#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:33:07 2018

@author: anamikas
"""

list1 = ['x','y','z','a','b','c','d','e','f','g']
indices = [(0, 4), (5, 9)]
print ([list1[s:e+1] for s,e in indices])

test_str = 'ladjobealwe'
indices2 = [(0,3),(3,7),(7,11)]
print ([test_str[s:e] for s,e in indices2])

#list2 = ['l', 'a', 'd', 'j', 'o', 'b', 'e', 'a', 'l', 'w', 'e']
#print(''.join(list2))

test_str3 = 'diainodt'
indices3 = [(0,8)]
print ('output',[test_str3[s:e] for s,e in indices3])

# indices = [(0,3),(3,7),(7,11)]

def final_split_indices(indices_str):
    element_list = indices_str.split('|')
    output_list = []
    prev=0
    for i in element_list:
        output_list.append((int(prev),int(i)))
        prev = i
        print(output_list)
    return output_list
        

input_str = '3|7|11'
#final_split_indices(input_str)

def secondary_string(input_str,pos):
    out_str=''
    for a in pos:
        if a!='|':
            out_str+=input_str[int(a)-1]
            print(out_str)
    return out_str




    
