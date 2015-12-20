#Problem 3
'''

'''

def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

def Main():
  nums=primefactor(600851475143)
  print "Largest prime factor:",max(nums)

if __name__=="__main__":
  Main()
