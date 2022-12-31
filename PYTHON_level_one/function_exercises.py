# answer no 1 questions book la unavi sudu Dt.06.10.2022
def arrayCheck(nums):

    for i in range(len(num)-2):
        if nums[i]==1 and num[i+1]==2 and num[i+2]==3:
            return True
    return False

# answer no 2
def stringBits(mystring):

    result = ""

    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]

    return result

# answer no 3
def end_other(a,b):
    a = a.lower()
    b = b.lower()

    # return (b.endswith(a) or a.endswith(b)) edi pan vasadi answer unko typelapan vasadi answer
    return a[-(len(b)):] == b or a == b[-len(a):]

# answer no 4
def doubleChar(mystring):

    result = ''
    for char in mystring:
        result += char*2
    return result

# answer no 5
def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

    if n [13,14,17,18,19]:
        return 0
    return n

# answer no 6
def count_evens(nums):
    count = 0

    for element in nums:
        if element % 2 == 0:
            count += 1
        return count
