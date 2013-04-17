str1 = "one, two, three, four, five, six, seven, eight, nine, ten"
# after babelfish.altavista.com  English to French translation
str2 = "un, deux, trois, quatre, cinq, six, sept, huit, neuf, dix"
engList = str1.split(", ")
frenList = str2.split(", ")
eng2frenDict = {}
k = 0
for eng in engList:
    eng2frenDict[eng] = frenList[k]
    k += 1
    
print eng2frenDict

""" result =
{'seven': 'sept', 'ten': 'dix', 'nine': 'neuf', 'six': 'six', 'three': 'trois', 
'two': 'deux', 'four': 'quatre', 'five': 'cinq', 'eight': 'huit', 'one': 'un'}
"""