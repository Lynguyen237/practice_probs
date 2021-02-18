# English tnt: Given any integer, print an English phrase that describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").

#ex:
# 1,234 => One Thousand, Two Hundred Thirty Four
# 123,456 => One Hundred Twenty Three Thousand, Four Hundred Fifty Six
# number < 1M
# return a string describing the number in english

def integer_to_english(number):
    
    number_string = ""
    
    number_dict = {1:"one",
               2:"two",
               3:"three",
               4:"four",
               5:"five",
               6:"six",
               7:"seven",
               8:"eight",
               9:"nine",
               10: "ten",
               20: "twenty",
               30: "thirty",
               40: "forty",
               50: "fifty",
               60: "sixty",
               70: "seventy",
               80: "eighty",
               90: "ninety"}
               
    list_of_digits = list(str(number))
    print(list_of_digits)
   #123
    counter = 1
    # i= 4 
    for i in reversed(range(len(list_of_digits))):
        # print(i)
        # print(list_of_digits[i])
        # print(number_dict[int(list_of_digits[i])])
        # second spot
        if (counter + 1) % 3 == 0:
            number_string = number_dict[int(list_of_digits[i])*10]+ " " + number_string 
                      
        # third spot
        elif (counter % 3) == 0:
            number_string = number_dict[int(list_of_digits[i])] + " hundred " + number_string
      
        # first spot
        else:
            number_string += number_dict[int(list_of_digits[i])]
                      
        counter +=1
    
    return number_string
                                    
print(integer_to_english(123))                                
                      
    # i = 3 = > 4 counter = 1= > str=Four
    # i = 2 => 3, counter = 2 => str= "thirty" + four
    # i = 1 = > 2, counter = 3 => stt = "two" + "hundred" + "four"
                      
    # number_dict[digits[-1]] # last digit
    # number_dict[digits[-2]] # the tens
    # number_dict[digits[-3]] + "hundred" # the hundreds
    # number_dict[digits[-4]] + "thousand" # the thousand
    
    # 1 digit: single number
    # 2 digits: the tens
    # 3 digits: the hundreds
    # 4 digits: the thousands
    
    
    
#     1000
#     200
#     30
#     4 # 0 - ignore
    
    # 11, 12, 13, 14, 15