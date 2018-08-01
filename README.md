# Jumble Solver:
The jumble puzzle is a common newspaper puzzle, it contains a series of anagrams
 that must be solved (see https://en.wikipedia.org/wiki/Jumble). To solve, one 
 must solve each of the individual jumbles. The circled letters are then used 
 to create an additional anagram to be solved. In especially difficult versions
 , some of the anagrams in the first set can possess multiple solutions. To get
  the final answer, it is important to know all possible anagrams of a given 
  series of letters.

The challenge is to solve the five Jumble puzzles using Spark, where it makes 
sense to do so. If the final puzzle has multiple possible 
answers, you are to include an algorithm to determine the most likely one. A dictionary is provided 
where the "most common" English words are scored 
(1=most frequent, 9887=least frequent, 0=not scored due to infrequency of use).
 For each puzzle, produce the "most likely" (as you determine it) final anagram
  produced from solving all the other anagrams.

Also included:
freq_dict - keys are English Dictionary words to be used in your solving of the
 jumbles. Non-zero values are the frequency rankings (1=most frequent). Zero 
 values mean that the word is too infrequent to be ranked.
pictures of the jumbles we provided for you to solve. You can put these in 
whatever data format you'd like for your program to read in
