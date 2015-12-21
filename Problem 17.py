#Problem 17
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.The use of "and" when writing
out numbers is in compliance with British usage.
'''
# To install inflect "$pip install  inflect"

import inflect
import re

def lenofnumber(num):
  p=inflect.engine()
  s=p.number_to_words(num)
  #print s
  new= re.split('and ',s)
  #print new
  q="".join(new)
  #print q
  return len(q)

def Main():
  summation=[]
  for i in range(1,9):
    h=lenofnumber(i)
    summation.append(h)
  print "total number of letters used:",sum(summation)
  
if __name__=="__main__":
  Main()
  
