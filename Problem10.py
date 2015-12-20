#Problem10
'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def prime_no(num):
  for j in range(2,num):
    if num%j==0:
      return False
  return True


def Main():
  print "Program started"
  num=2000000
  h=[]
  for i in range(2,num):
    if prime_no(i):
      h.append(i)
  print "Program ended and the sum is:",sum(h)


if __name__=="__main__":
  Main()
  
