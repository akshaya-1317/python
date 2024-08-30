#7. Print following pattern using repetition operator (*). Take number of lines from end user.
# *
# **
# ***
# ****
# *****


def pattern1(n):
    if n > 0:
        pattern1(n-1)
        print('*' * n)

rows = int(input("Enter number of rows: "))
pattern1(rows)




# 8. Print following pattern. Hint: Use nested loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def pattern(n):
    if n>0 :
        pattern(n+1)
        print('n' * n)

num = int(input("Enter number: "))
pattern(num)