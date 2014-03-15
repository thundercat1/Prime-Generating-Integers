import time
import sys


def divisors(n):
    divisors = []
    i = 1
    if n not in divisorHistory:
        while i < n/i:
            if n % i == 0:
                divisors.extend([i,n/i])
            i += 1
    divisors.sort()
    divisorHistory[n] = divisors

    #new stuff
    #for divisor in divisors:
    #    divisorHistory[divisor] = divisors[0:divisors.index(divisor)+1]
    #    print 'divisors of ' + str(divisor) + ' are ' + str(divisorHistory[divisor]

start = time.time()
#out = divisors(30)
#out.sort()

divisorHistory = {}
z = 30 
while z > 0:
    divisors(z)
    sys.stdout.write('\r')
    sys.stdout.write(str(z))
    sys.stdout.flush()
    z -= 1
sys.stdout.write('\n')

divisorTotal = 0
for key in divisorHistory:
   divisorTotal += sum(divisorHistory[key])

stopTime = time.time()
print divisorHistory
print divisorTotal

print 'Computation time: ' + str(stopTime-start)

