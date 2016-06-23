max = 100000
import time



start = time.time()
for i in range(1,max):
    if (i % 15 ==0):
        print i,"fizzbuzz"
    elif (i % 5 == 0):
        print i, "buzz"
    elif (i % 3 == 0):
        print i,"fizz"
    else:
        print i

sample1 = time.time()
for i in xrange(1, max):
    print("fizz"*(i % 3 == 0) + "buzz"*(i % 5 == 0) or i)    


sample2 = time.time()
for i in range(1,max):
    print [i,"buzz","fizz","fizzbuzz"][2*(i%3==0) + (i%5==0)]
    
sample3 = time.time()


print "Sample 1: ", (sample1 - start)
print "Sample 2: ", (sample2 - sample1)
print "Sample 3: ", (sample3 - sample2)

