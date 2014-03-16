import time
import sys

f = open('primes_to_100000000.txt')
primes = []
for line in f:
    primes.append(int(line.strip()))
primes = set(primes)

def primeGenerator(candidate, primes):
    divisors = []
    i = 2
    if i == 2 and (candidate/2)%2 == 0:
        return False
    while i*i <= candidate:
            if candidate % i == 0:
                #if i is a divisor
                if i + candidate/i not in primes:
                    return False
            i += 1
    return True

start = time.time()
primeGenerators = [1]
primesToCheck = len(primes)
checked = 0
for prime in primes:
    #sys.stdout.write('\r')
    #sys.stdout.write('Checking for qualifying candidates: ' + str(100*checked/primesToCheck) + '%     ')
    #sys.stdout.flush()
    candidate = prime - 1
    if primeGenerator(candidate, primes):
        primeGenerators.append(candidate)
     
    checked += 1

stopTime = time.time()
print 'sum of primeGenerators = ' + str(sum(primeGenerators))
print 'Computation time: ' + str(stopTime-start) 
print 'Writing results to file'
sys.stdout = open('prime_generators_to_100000000.txt','w')
for generator in primeGenerators:
    sys.stdout.write(str(generator) + '\n')

