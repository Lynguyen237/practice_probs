# "aabb" --> "cat cat dog dog" = true
# "aaba" -->"cat cat dog dog" = false
# "aaa" -->"dog cat cat" = false
# "abba" -->"cat dog dog cat" = true
# "bab" --> "cat dog cat" = true
# "123" --> "bat dog rat"
# "112" --> "bat bat rock"

# "112" --> "100 100 103"
# "1121" --> "100 100 103 100"
# abbacc 

# pattern can be any letters, the string can be anything

#if follows the pattern, return return true, else return false
#if empty, return false


class Pattern():
    def __init__(self, pattern, string):
        self.pattern = pattern
        self.string = string
        
        self.patternLst = []
        self.stringLst = []
        
        
    def checkValid(self):
        self.patternLst = list(self.pattern)
        self.stringLst = self.string.split(" ")
        
        if len(self.patternLst) != len(self.stringLst):
            return False
        
        return True
    
    
    def checkPattern(self):
        if not self.checkValid():
            return False
        else:
            
            mapping = {}
            p = self.patternLst
            s = self.stringLst

            for i in range(len(p)):
                if p[i] not in mapping:
                    if s[i] in mapping.values():
                        return False 
                    else:
                        mapping[p[i]] = s[i]
                else:
                    if mapping[p[i]] == s[i]:
                        continue
                    else:
                        return False

            return True
        

pattern1 = Pattern("aabc", "cat cat dog dog") #False
print(pattern1.checkValid()) #True
print(pattern1.checkPattern()) #False