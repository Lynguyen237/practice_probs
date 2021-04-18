'''
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. 
Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
'''

#==== Revised solution ====
def LongestWord(sen):

  nw = ""

  for c in sen:
    if c.isalnum():
      nw += c
    else:
      nw += " "
  
  nw = nw.split()

  return max(nw, key = len)


#==== First rough solution ====
def LongestWord(sen):

  sen = sen.split(" ")
  longest_len = 0
  longest_word = ""

  for word in sen:
    clean_word = ""
    for c in word:
      if c.isalnum():
        clean_word += c
    
    if len(clean_word) > longest_len:
      longest_len = len(clean_word)
      longest_word = clean_word

  return longest_word
