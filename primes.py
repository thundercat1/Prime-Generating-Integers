import time

startTime = time.time()


def sieve(n):
    #Return set of primes <= n
    candidates =range(1,n+1)
    i=1
    prime = candidates[i]
    while prime*prime <= n:
        prime = candidates[i]
        #print 'Removing multiples of ' + str(prime) + ' from candidates'
        multiple = 2
        candidates = set(candidates)
        while prime*multiple <= n:
            if prime*multiple in candidates:
                candidates.remove(prime*multiple)
            multiple += 1
        candidates = list(candidates)
        i += 1
    return candidates

primes = []
n = 1000000
startTime = time.time()
primes.extend(sieve(n))
stopTime = time.time()
#print primes
print 'Time to compute primes < ' + str(n) + ' :   ' + str(stopTime-startTime)


        

