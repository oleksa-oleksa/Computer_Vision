import numpy as np
import matplotlib.pyplot as plt
import pylab

def make_lenghts_equal(func1, func2):
    # from matlab xcorr function: If x and y have different lengths, the function appends zeros 
    # to the end of the shorter vector so it has the same length as the other. 
    size_diff = np.size(func1) - np.size(func2) # positive if f1 > f2, negative if f1 < f2 
    nulls = np.zeros(size_diff)
    
    if size_diff < 0:
        func1 = np.append(func1, nulls)
    else:
        func2 = np.append(func2, nulls)
        
    return func1, func2

def myCrossCorrelation(func1, func2):
    # idea explanation: https://www.youtube.com/watch?v=ngEC3sXeUb4
    # https://anomaly.io/understand-auto-cross-correlation-normalized-shift/index.html    
    nom = func1 * func2
    
    sum1 = np.sum(func1**2)
    sum2 = np.sum(func2**2)
    
    dem = np.sqrt(sum1 * sum2)
    return np.sum(nom)/dem
    

foo1 = np.random.randint(0, 256, 10)
#print(foo1)
#foo2a = np.random.randint(0, 256, 10)
foo2a = np.array([1])
foo2b = np.array([1, 2, 1])

# ----- A -----
# compare lenghts and make them equal for crosscorrelation
foo1, foo2a = make_lenghts_equal(foo1, foo2a)

plt.plot(foo1, color='r')
plt.plot(foo2a, color='b')
print("function 1: {}".format(foo1))
print("function 2: {}".format(foo2a))
print("Normalized crosscorrelation: {}".format(myCrossCorrelation(foo1, foo2a)))
plt.show()

# ----- B -----
# compare lenghts and make them equal for crosscorrelation
foo1, foo2b = make_lenghts_equal(foo1, foo2b)

plt.plot(foo1, color='r')
plt.plot(foo2b, color='b')
print("function 1: {}".format(foo1))
print("function 2: {}".format(foo2b))
print("Normalized crosscorrelation: {}".format(myCrossCorrelation(foo1, foo2b)))
plt.show()

# ----- C1 -----
# compare lenghts and make them equal for crosscorrelation
foo2a, foo1 = make_lenghts_equal(foo2a, foo1)

plt.plot(foo2a, color='r')
plt.plot(foo1, color='b')
print("function 1: {}".format(foo2a))
print("function 2: {}".format(foo1))
print("Normalized crosscorrelation: {}".format(myCrossCorrelation(foo2a, foo1)))
plt.show()

# ----- C2 -----
# compare lenghts and make them equal for crosscorrelation
foo2b, foo1 = make_lenghts_equal(foo2b, foo1)

plt.plot(foo2b, color='r')
plt.plot(foo1, color='b')
print("function 1: {}".format(foo2b))
print("function 2: {}".format(foo1))
print("Normalized crosscorrelation: {}".format(myCrossCorrelation(foo2b, foo1)))
plt.show()