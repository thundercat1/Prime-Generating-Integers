import time
import sys

startTime = time.time()


def sieve(n):
    #Return set of primes <= n
    candidates =range(0,n+1)
    i=2
    prime = candidates[i]
    sys.stdout.write('\n')
    while prime*prime <= n:
        if candidates[i]:
            prime = candidates[i]
            sys.stdout.write('\r')
            sys.stdout.write('Removing multiples of ' + str(prime) + ' from candidates:      ')
            sys.stdout.flush()
            
            multiple = 2
            while prime*multiple <= n:
                if candidates[prime*multiple]:
                    if 100*prime*multiple/n < 10:
                        sys.stdout.write('\b\b')
                    else:
                        sys.stdout.write('\b\b\b')
                    sys.stdout.write(str(100*prime*multiple/n) + '%')
                    sys.stdout.flush()
                    candidates[prime*multiple] = None
                multiple += 1
        i += 1
    return filter(None,candidates)

primes = []
n = 100000000
startTime = time.time()
a=sieve(n)
#print a
#primes.extend(sieve(n))
stopTime = time.time()
#print primes
print 'Time to compute primes < ' + str(n) + ' :   ' + str(stopTime-startTime)


        

