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