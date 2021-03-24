# https://leetcode.com/problems/word-ladder/
# A transformation sequence from word beginWord to word endWord using a dictionary wordList 
# is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# - Every adjacent pair of words differs by a single letter.
# - Every si for 1 <= i <= k is in wordList. Note that beginWord 
# does not need to be in wordList.
# - sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, 
# return the number of words in the shortest transformation sequence from beginWord to endWord, 
# or 0 if no such sequence exists.

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

#==== ATTEMPT ====
def ladderLength0(source: str, target: str, words: list):

    import string 

    if target not in words:
        return 0
    
    wordset = set(words)

    queue = [(source, 1)]
    
    while queue:
        word, step = queue.pop(0)
        if word == target:
            return step
        for i in range(len(target)):
            for char in string.ascii_lowercase:
                newword = word[:i] + char + word[i+1:]
                if newword in wordset:
                    wordset.remove(newword)
                    queue.append((newword, step+1))
    
    # Instead of while loop, for loop can be used as well like below
    # for (word, step) in queue:
    #     if word == target:
    #         return step
    #     for i in range(len(target)):
    #         for char in string.ascii_lowercase:
    #             newword = word[:i] + char + word[i+1:]
    #             if newword in wordset:
    #                 wordset.remove(newword)
    #                 queue.append((newword, step+1))
    return 0

print(ladderLength0("hit", "cog", ["hot","dot","dog","lot","log","cog"])) #5



#==== SOLUTION ==== Breath first search O(n)
# https://zhenyu0519.github.io/2020/03/24/lc127/

import collections

def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    wordset = set(wordList)
    queue = collections.deque()
    queue.append((beginWord, 1))
    word_length = len(beginWord)
    while queue:
        word, step = queue.popleft()
        if word == endWord:
            return step
        for i in range(word_length):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i]+c+word[i+1:]
                if newWord in wordset:
                    wordset.remove(newWord)
                    queue.append((newWord, step+1))
    return 0

# print(ladderLength("bit", "dog", ["but", "put", "big", "pot", "pog", "dog", "lot"])) #6
# print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) #5