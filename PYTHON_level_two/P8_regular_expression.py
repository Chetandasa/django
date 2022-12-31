# one edi print la I'm searching for: term1
#                  MATCH!
#                  I'm searching for: term2
#                  NO MATCH!
import re
patterns = ['term1','term2']
text = 'this is a strigwith term1, not the other!'

for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern,text):
        print("MATCH!")
    else:
        print("NO MATCH!")

# two edi print la <class 're.match'> etla vasadi
import re

text = 'this is a strigwith term1, not the other!'

match = re.search('term1',text)

print(type(match))

# three edi print la 20 vasadi
import re

text = 'this is a strigwith term1, not the other!'

match = re.search('term1',text)

print(match.start())

# four edi print la 0 vasadi
import re

text = 'term1'

match = re.search('term1',text)

print(match.start())

# five edi print la ['user', 'gmail.com'] etla vasadi @ split aitadi @ tishe anta print aitadi
import re

split_term = '@'

email = 'user@gmail.com'

print(re.split(split_term,email))

# seven edi print la ['match','match'] vasadi yani sarlaa match untadi ga ani sarla vasadi
import re

print(re.findall('match','test phrase match in match middle'))

# eight * unte print la s side ku d yani sarla unte ane sarla ddd vasadi only s unte leda sss etla unte seprate vasdi s s s etla space vasadi
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['sd*']

multi_re_find(test_patterns,test_phrase)

# nine + unte print la d mungata s untadi ha apud s print aitadi dan mungata d yanipan unteprint aitadi single s print kadu sdsd, leda sddd , sdddddd
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['sd+']

multi_re_find(test_patterns,test_phrase)

# ten ? unte print la s yani pan unte print aitadi pan s mungata d unte onlu one sarla print aitadi sd,s,s,sdetla
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['sd?']

multi_re_find(test_patterns,test_phrase)

# eleven {3} bracket la yanta pan number undani ani matla d print aitadi for example 3 unte 3 d lu print aitadi ddd etla gani s mungatane aitadi
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['sd{3}']

multi_re_find(test_patterns,test_phrase)

# 12) {1,3} bracket la numbers unte 1 d ani 3 dddlu yani unte ani print aitadi sd , sddd, sd ,sd ,sddd sdetla
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['sd{1,3}']

multi_re_find(test_patterns,test_phrase)

# 13) ['s[sd]+'] etla unte print la sssss unte pan print aitadi sd, sssddd , sds
#                       gani dsds unte print kadu only sds prit aitadi dsds la
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns =['s[sd]+']

multi_re_find(test_patterns,test_phrase)

# 14) ['[^!.?]'+] print la edi ani idshe print vasadi ^!.? evi ravu print la baki words vasavi.
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

test_patterns =['[^!.?]+']

multi_re_find(test_patterns,test_phrase)

# 15) ['[a-z]'] a-z chasa ane small letters vasavi a to z yani small lettersunavi ante print aitavi
#          [A-Z] ETLA CHASAE A TO Z ANI BIG LETTERS PRINT AITADI
import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

test_patterns =['[a-z]+']

multi_re_find(test_patterns,test_phrase)

# 16) [r'\d+'] etla \d small d unte ani numbers print aitadi 12312 etla words print kadu
#     [r'\D+'] etla \d unte big D numbers idshe only sentens word print aitadi
#     [r'\s+'] etla \s small s unte ani idshe words yani unte ani ' ' , ' ', ' ' ani etla comas print aitadi dinki white space antaru ' '
#     [r'\S+'] ETLA \S big S unte edi comas sarta ani words ku comas vasadi 'hello' , 'hii' etla dinki Non white space antaru.
#     [r'\w+'] etla \w small w unte words and numbers printaitadi commas sarta gani # @ ! % atla am print kavu only words and numbers.
#     [r'\W+'] etla \W big W unte words and number am print kavu only @ # % $ etla print aitadi commas sarta .

import re
def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}",format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'

test_patterns =[r'\w+']

multi_re_find(test_patterns,test_phrase)
