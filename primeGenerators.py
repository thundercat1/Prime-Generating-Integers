import time
import sys

f = open('primes_to_100000000.txt')
primes = []
for line in f:
    primes.append(int(line.strip()))
primes = set(primes)

def primeGenerator(candidate, primes):
    #!!!  12 is definitely not a prime generator!
    divisors = []
    i = 1
    while i*i <= candidate:
            if candidate % i == 0:
                #if i is a divisor
                if i not in primes:
                    return False
            i += 1
    #print 'Found prime generator: ' + str(candidate)
    return True

start = time.time()
primeGenerators = []
primesToCheck = len(primes)
checked = 0
for prime in primes:
    sys.stdout.write('\r')
    sys.stdout.write('Checking for qualifying candidates: ' + str(100*checked/primesToCheck) + '%     ')
    sys.stdout.flush()
    candidate = prime - 1
    if primeGenerator(candidate, primes):
        primeGenerators.append(candidate)
     
    checked += 1

stopTime = time.time()
print 'sum of primeGenerators = ' + str(sum(primeGenerators))
print 'Writing results to file'
sys.stdout = open('prime_generators_to_100000000.txt','w')
for generator in primeGenerators:
    sys.stdout.write(str(generator) + '\n')

print 'Computation time: ' + str(stopTime-start) 
