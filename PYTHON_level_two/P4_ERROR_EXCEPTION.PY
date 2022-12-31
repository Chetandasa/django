# python p4_error_exception.py

# PRINT CHASADI UNTE 1 SUSADI UNTE 2,3 TEXT CHAY APUD PRINT VASADI
   # 2 SUSADI UNTE 1,3 TEXT CHAY 3 SUSADI UNTE 1,2 TEXT CHAY SUDU OK!

#  simple.txt ante oka file create chasena .py di yatla untadi atla .txt dicreate chasena simple.txt unde sudu.

# 1)
try:
    f = open('simple.txt','w')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
# # etla chase try la 'simple.txt','w' unde ga ante write unda susadi wrong unte except la type chasedi print aitadi leda corectunte
# # unte else print aitadi SUCCESS ani aniunkoti exam exmpal sudu kinda
print("hello world!")

# 2)
try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!")
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
# etla chase try la 'simple.txt','r' unte ga ante read chasadi ude ana laka print chasae ERROR vasadi read kadu except la unadi print aitadi

# 3)epud finally use chasdi sudu
try:
     f = open('simple.txt','r')
     f.write("Test write to simple text!")
except:
     print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
