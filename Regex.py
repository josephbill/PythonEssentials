# regex function exists as a module
import re
# Regular Expressions (RegEx) : sequence of characters that form a search pattern
# using Regex to check if strings contain a pattern
text = "It is quite sunny today"
# search regex method : returns a match object if there is match in the string
# metacharacters : characters with special meaning
# in regex ^ start with
# $ indicates end with
# * indicates that there zero or more occurances
# . indicates Any character
x = re.search("^It.*$", text)
print(x)
# find all
# returns a list containing all possible matches
x = re.findall("raining",text)
print(x)
#split : returns a lists where the string has been split at each match
x = re.split("\t",text)
print(x)
x = re.split("\s",text,1)
print(x)
# sub : replaces the searched term with a word of choice
x = re.sub("\s","4",text)
print(x)
# match : equivalent to search