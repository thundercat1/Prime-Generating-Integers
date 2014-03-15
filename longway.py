import time
import sys


def divisors(n):
    divisors = []

    i = 1
    if n not in divisorHistory:
        while i <= n/i:
            if n % i == 0:
                if i == n/i:
                    divisors.append(i)
                else:
                    divisors.extend([i,n/i])
            i += 1
    divisors.sort()
    if len(divisors) == 2:
        #n is prime
        primes.append(n)
    divisorHistory[n] = divisors

    #new stuff
    #for divisor in divisors:
    #    divisorHistory[divisor] = divisors[0:divisors.index(divisor)+1]
    #    print 'divisors of ' + str(divisor) + ' are ' + str(divisorHistory[divisor]

start = time.time()
#out = divisors(30)
#out.sort()

divisorHistory = {}
primes = []
limit = 1000000
z = limit + 1 
print 'Finding divisors:  '
while z > 0:
    divisors(z)
    sys.stdout.write('\r')
    sys.stdout.write(' ' + str(100*(limit-z)/limit) + '%     ')
    sys.stdout.flush()
    z -= 1
sys.stdout.write('\n')

divisorTotal = 0
for key in divisorHistory:
   divisorTotal += sum(divisorHistory[key])

primeGenerators = []
progress = 1
print 'Checking for prime generators'
for n in divisorHistory:
    sys.stdout.write('\r')
    sys.stdout.write(' ' + str(100*progress/limit) + '%   ')
    progress += 1
    sys.stdout.flush()
    candidate = True
    #print 'Evaluating ' + str(n) + ' as primeGenerator candidate.'
    for d in divisorHistory[n]:
    #    print 'For divisor ' + str(d) + ' of generator candidate ' + str(n) + ':  d + n/d = ' + str(d + n/d)
        if (d + n/d) not in primes:
            #no longer a candidate
            candidate = False
    if candidate == True:
        primeGenerators.append(n)

sys.stdout.write('\n')

if limit+1 in primeGenerators:
    primeGenerators.remove(limit)
stopTime = time.time()
print divisorHistory
print 'Divisor total check: ' + str(divisorTotal)
print 'Identified the following primes: ' + str(primes)
print 'Prime Generators found: ' + str(primeGenerators)
print 'Sum of prime generators: ' + str(sum(primeGenerators))
print 'Computation time: ' + str(stopTime-start) 
