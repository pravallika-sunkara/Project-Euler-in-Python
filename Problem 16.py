#Problem 16

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? '''

def sum_digits(n):
  sum_no=0
  while n:
    sum_no + =n%10
    n/=10
  return s
  
def Main():
 pow=2**1000
 print "The sum of the digits of the number 2^1000: ",sum_digits(pow)
 
if __name__=="__main__":
  Main()
 
