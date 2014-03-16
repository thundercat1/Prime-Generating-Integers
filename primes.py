import time
import sys

startTime = time.time()


def sieve(n):
    #Return set of primes <= n
    candidates = [0,1,2]
    candidates.extend(range(3,n+1,2))
    #print 'candidates starting as ' + str(candidates)
    i=2
    prime = candidates[i]
    sys.stdout.write('\n')
    while prime*prime <= n:
        #print 'i = ' + str(i)
        #print 'candidates[i] = ' + str(candidates[i])
        if candidates[i]:
            prime = candidates[i]
            #print 'prime = ' + str(prime)
            sys.stdout.write('\r')
            sys.stdout.write('Removing multiples of ' + str(prime) + ' from candidates:      ')
            sys.stdout.flush()
            
            multiple = 2
            while prime*multiple < n:
                if prime*multiple % 2 == 1 and candidates[prime*multiple/2+2]:
                    #if 100*prime*multiple/n < 10:
                        #sys.stdout.write('\b\b\b')
                    #else:
                        #sys.stdout.write('\b\b\b\b')
                    #sys.stdout.write(str(100*prime*multiple/n) + '% ')
                    sys.stdout.flush()
                    candidates[prime*multiple/2+2] = None
                multiple += 1
            #print candidates
        i += 1
    return filter(None,candidates)

#primes = []
n = 1000000
startTime = time.time()
primes=sieve(n)
#print a
#primes.extend(sieve(n))
stopTime = time.time()
#print primes
print 'Time to compute primes < ' + str(n) + ' :   ' + str(stopTime-startTime)
print 'Writing primes to file'

sys.stdout = open('primes_to_1000000.txt', 'w')
for prime in primes:
    sys.stdout.write(str(prime) + '\n')
