# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#------------------
2 + 2
#4
50 - 5*6
#20
(50 - 5*6) / 4
#5.0
8 / 5  # division always returns a floating point number
#1.6
17 / 3  # classic division returns a float
#5.666666666666667
17 // 3  # floor division discards the fractional part
#5
17 % 3  # the % operator returns the remainder of the division
#2
5 * 3 + 2  # result * divisor + remainder
#17
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
#------------------

##s = 'First line.\nSecond line.'  # \n means newline
##s  # without print(), \n is included in the output
##print(s)  # with print(), \n produces a new line
##
##print('C:\some\name')  # here \n means newline!
##print(r'C:\some\name')  # note the r before the quote
#------------------

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to www
""")


