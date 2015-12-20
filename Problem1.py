#Problem1
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.'''

def Main():
  nums=range(0,1000)
  s=filter(lambda x:x%3==0 or x%5==0,nums)
  print "Sum of multiples of 3 and 5 below 1000:",sum(s)

if __name__=="__main__":
  Main()
  
